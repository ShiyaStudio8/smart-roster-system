import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from logic import (EMPLOYEES, BRANDS, generate_roster, add_leave, 
                   apply_backup_fix, apply_manual_override, reset_schedule, 
                   set_month_length, get_process_view, get_employee_view,
                   add_new_employee, add_new_brand)

app = Flask(__name__)
app.secret_key = "datastraw_assessment_secret_key"

@app.route('/')
def welcome():
    return render_template('welcome.html', employees=EMPLOYEES, brands=BRANDS)

@app.route('/dashboard')
def dashboard():
    schedule, conflicts = generate_roster()
    process_data = get_process_view()
    employee_data = get_employee_view()
    
    pods = {}
    for emp in EMPLOYEES:
        p = emp["pod"]
        if p not in pods:
            pods[p] = []
        pods[p].append(emp)

    return render_template('dashboard.html', 
                           employees=EMPLOYEES, 
                           brands=BRANDS, 
                           schedule=schedule, 
                           conflicts=conflicts,
                           pods=pods,
                           process_data=process_data,
                           employee_data=employee_data)

@app.route('/set-month', methods=['POST'])
def set_month():
    days = request.form.get('days', 30)
    set_month_length(days)
    flash(f"Roster calendar updated to {days}-day cycle.", "info")
    return redirect(url_for('dashboard'))

@app.route('/request-leave', methods=['POST'])
def request_leave():
    emp_id = request.form.get('emp_id')
    day = request.form.get('day')
    if emp_id and day:
        success, message = add_leave(emp_id, day)
        if not success:
            flash(message, "danger")
        else:
            flash(message, "success")
    return redirect(url_for('dashboard'))

@app.route('/manual-override', methods=['POST'])
def manual_override():
    brand_id = request.form.get('brand_id')
    day = request.form.get('day')
    replacement_emp_id = request.form.get('replacement_emp_id')
    if brand_id and day and replacement_emp_id:
        apply_manual_override(brand_id, day, replacement_emp_id)
        flash("Manual override applied successfully!", "info")
    return redirect(url_for('dashboard'))

@app.route('/apply-fix', methods=['POST'])
def apply_fix():
    apply_backup_fix()
    flash("Auto-backup assigned successfully!", "success")
    return redirect(url_for('dashboard'))

@app.route('/reset', methods=['POST'])
def reset():
    reset_schedule()
    flash("Roster reset to default state.", "info")
    return redirect(url_for('dashboard'))

@app.route('/add-employee', methods=['POST'])
def add_employee_route():
    name = request.form.get('name')
    pod = request.form.get('pod')
    role = request.form.get('role')
    if name and pod and role:
        add_new_employee(name, pod, role)
        flash(f"Employee {name} added successfully!", "success")
    return redirect(url_for('dashboard'))

@app.route('/add-brand', methods=['POST'])
def add_brand_route():
    name = request.form.get('name')
    brand_type = request.form.get('type')
    process = request.form.get('process')
    rule = request.form.get('rule')
    emp_id = request.form.get('emp_id')
    if name and process and emp_id:
        add_new_brand(name, brand_type, process, rule, emp_id)
        flash(f"Brand {name} added and mapped successfully!", "success")
    return redirect(url_for('dashboard'))

@app.route('/export-csv')
def export_csv():
    schedule, _ = generate_roster()
    si = StringIO()
    writer = csv.writer(si)
    
    headers = ["Brand Name", "Model", "Rule"] + [f"Day {i}" for i in range(1, 31)]
    writer.writerow(headers)
    
    for row in schedule:
        row_data = [row["brand_name"], row["type"], row["rule"]]
        for d in range(1, 31):
            row_data.append(row["daily_status"].get(d, "-"))
        writer.writerow(row_data)
        
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=monthly_roster_matrix.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == '__main__':
    app.run(debug=True)
    