# logic.py - Enterprise-Grade Smart Roster Management Engine

EMPLOYEES = [
    {"id": 1, "name": "Aarav Sharma", "pod": "Pod A", "role": "Pod Lead"},
    {"id": 2, "name": "Aditi Verma", "pod": "Pod A", "role": "Agent"},
    {"id": 3, "name": "Amit Patel", "pod": "Pod A", "role": "Agent"},
    {"id": 4, "name": "Ananya Iyer", "pod": "Pod A", "role": "Agent"},
    {"id": 5, "name": "Arjun Nair", "pod": "Pod A", "role": "Agent"},
    {"id": 6, "name": "Bhavya Rao", "pod": "Pod B", "role": "Pod Lead"},
    {"id": 7, "name": "Chirag Joshi", "pod": "Pod B", "role": "Agent"},
    {"id": 8, "name": "Deepika Sen", "pod": "Pod B", "role": "Agent"},
    {"id": 9, "name": "Dhruv Kapoor", "pod": "Pod B", "role": "Agent"},
    {"id": 10, "name": "Divya Menon", "pod": "Pod B", "role": "Agent"},
    {"id": 11, "name": "Esha Roy", "pod": "Pod C", "role": "Pod Lead"},
    {"id": 12, "name": "Gaurav Kulkarni", "pod": "Pod C", "role": "Agent"},
    {"id": 13, "name": "Harshita Das", "pod": "Pod C", "role": "Agent"},
    {"id": 14, "name": "Isha Pillai", "pod": "Pod C", "role": "Agent"},
    {"id": 15, "name": "Kabir Mehta", "pod": "Pod C", "role": "Agent"},
    {"id": 16, "name": "Kavya Reddy", "pod": "Pod D", "role": "Pod Lead"},
    {"id": 17, "name": "Manish Kumar", "pod": "Pod D", "role": "Agent"},
    {"id": 18, "name": "Meera Joshi", "pod": "Pod D", "role": "Agent"},
    {"id": 19, "name": "Nikhil Warrier", "pod": "Pod D", "role": "Agent"},
    {"id": 20, "name": "Pooja Hegde", "pod": "Pod D", "role": "Agent"},
    {"id": 21, "name": "Rahul Deshmukh", "pod": "Pod E", "role": "Pod Lead"},
    {"id": 22, "name": "Riya Sen", "pod": "Pod E", "role": "Agent"},
    {"id": 23, "name": "Rohit Sharma", "pod": "Pod E", "role": "Agent"},
    {"id": 24, "name": "Sameer Khan", "pod": "Pod E", "role": "Agent"},
    {"id": 25, "name": "Sneha Patil", "pod": "Pod E", "role": "Agent"},
    {"id": 26, "name": "Tanvi Shah", "pod": "Pod F", "role": "Pod Lead"},
    {"id": 27, "name": "Varun Dhawan", "pod": "Pod F", "role": "Agent"},
    {"id": 28, "name": "Vidya Balan", "pod": "Pod F", "role": "Agent"},
    {"id": 29, "name": "Yash Malhotra", "pod": "Pod F", "role": "Agent"},
    {"id": 30, "name": "Zoya Akhtar", "pod": "Pod F", "role": "Agent"}
]

BRANDS = [
    {"id": "b1", "name": "LushSkin D2C", "type": "Single-Resource", "processes": ["Customer Support"], "assignments": {2: "Customer Support"}, "rule": "365 Days"},
    {"id": "b2", "name": "VedaGlow Organics", "type": "Single-Resource", "processes": ["Customer Support"], "assignments": {3: "Customer Support"}, "rule": "Mon-Sat"},
    {"id": "b3", "name": "UrbanFit Gear", "type": "Single-Resource", "processes": ["Abandoned Cart"], "assignments": {4: "Abandoned Cart"}, "rule": "365 Days"},
    {"id": "b4", "name": "SnackNation", "type": "Single-Resource", "processes": ["NDR Management"], "assignments": {5: "NDR Management"}, "rule": "Mon-Sat"},
    {"id": "b5", "name": "BrewCoffee Co.", "type": "Single-Resource", "processes": ["Customer Support"], "assignments": {7: "Customer Support"}, "rule": "365 Days"},
    {"id": "b6", "name": "PetPals Direct", "type": "Single-Resource", "processes": ["Retention"], "assignments": {8: "Retention"}, "rule": "Mon-Sat"},
    {"id": "b7", "name": "HomeVibe Living", "type": "Single-Resource", "processes": ["Customer Support"], "assignments": {9: "Customer Support"}, "rule": "365 Days"},
    {"id": "b8", "name": "ZestApparel", "type": "Single-Resource", "processes": ["Abandoned Cart"], "assignments": {10: "Abandoned Cart"}, "rule": "Mon-Sat"},
    {"id": "b9", "name": "Nomad Footwear", "type": "Single-Resource", "processes": ["Customer Support"], "assignments": {12: "Customer Support"}, "rule": "365 Days"},
    {"id": "b10", "name": "NutriBite", "type": "Single-Resource", "processes": ["NDR Management"], "assignments": {13: "NDR Management"}, "rule": "Mon-Sat"},
    {"id": "b11", "name": "AuraLux Watches", "type": "Multi-Resource", "processes": ["Customer Support", "NDR Management"], "assignments": {14: "Customer Support", 15: "NDR Management"}, "rule": "365 Days"},
    {"id": "b12", "name": "Blissful Botanicals", "type": "Multi-Resource", "processes": ["Customer Support", "Cart Recovery"], "assignments": {17: "Customer Support", 18: "Cart Recovery", 19: "Cart Recovery"}, "rule": "365 Days"}
]

CURRENT_MONTH_DAYS = 30
LEAVES = [{"emp_id": 2, "day": 10}]
OVERRIDES = {}

def set_month_length(days):
    global CURRENT_MONTH_DAYS
    CURRENT_MONTH_DAYS = int(days)

def add_leave(emp_id, day):
    emp_id = int(emp_id)
    day = int(day)
    
    if any(l["emp_id"] == emp_id and l["day"] == day for l in LEAVES):
        return False, "Employee is already on leave on this date."
        
    leaves_on_day = sum(1 for l in LEAVES if l["day"] == day)
    if leaves_on_day >= 4:
        return False, f"Daily limit reached! Day {day} already has 4 employees on leave (Max cap: 4)."
        
    LEAVES.append({"emp_id": emp_id, "day": day})
    emp_name = next(e["name"] for e in EMPLOYEES if e["id"] == emp_id)
    return True, f"Leave approved for {emp_name} on Day {day}."

def apply_manual_override(brand_id, day, replacement_emp_id):
    day = int(day)
    key = f"{brand_id}_{day}"
    emp_obj = next((e for e in EMPLOYEES if e["id"] == int(replacement_emp_id)), None)
    if emp_obj:
        OVERRIDES[key] = f"{emp_obj['name']} (Override)"

def apply_backup_fix():
    for l in LEAVES:
        brand = next((b for b in BRANDS if l["emp_id"] in b["assignments"]), None)
        if brand:
            key = f"{brand['id']}_{l['day']}"
            if key not in OVERRIDES:
                OVERRIDES[key] = "Support Pool Backup"
    return True

def reset_schedule():
    LEAVES.clear()
    LEAVES.append({"emp_id": 2, "day": 10})
    OVERRIDES.clear()

def add_new_employee(name, pod, role):
    new_id = max(e["id"] for e in EMPLOYEES) + 1
    EMPLOYEES.append({"id": new_id, "name": name, "pod": pod, "role": role})

def add_new_brand(name, brand_type, process, rule, emp_id):
    new_id = f"b{len(BRANDS) + 1}"
    emp_id = int(emp_id)
    BRANDS.append({
        "id": new_id,
        "name": name,
        "type": brand_type,
        "processes": [process],
        "assignments": {emp_id: process},
        "rule": rule
    })

def generate_roster():
    days = list(range(1, CURRENT_MONTH_DAYS + 1))
    schedule = []
    conflicts = []

    day_counts = {}
    for l in LEAVES:
        d = l["day"]
        day_counts[d] = day_counts.get(d, 0) + 1
    for d, count in day_counts.items():
        if count > 4:
            conflicts.append(f"Capacity Violation: Day {d} has {count} leaves recorded (Exceeds max limit of 4).")

    for brand in BRANDS:
        brand_status = {
            "brand_id": brand["id"],
            "brand_name": brand["name"],
            "type": brand["type"],
            "rule": brand["rule"],
            "daily_status": {}
        }
        
        for day in days:
            key = f"{brand['id']}_{day}"
            is_sunday = (day % 7 == 0)
            
            if brand["rule"] == "Mon-Sat" and is_sunday:
                brand_status["daily_status"][day] = "Off (Sunday Rule)"
                continue

            if key in OVERRIDES:
                brand_status["daily_status"][day] = f"Active ({OVERRIDES[key]})"
            elif brand["type"] == "Single-Resource":
                emp_id = list(brand["assignments"].keys())[0]
                emp_name = next((e["name"] for e in EMPLOYEES if e["id"] == emp_id), "Unknown")
                is_on_leave = any(l["emp_id"] == emp_id and l["day"] == day for l in LEAVES)
                
                if is_on_leave:
                    brand_status["daily_status"][day] = f"⚠️ Unstaffed ({emp_name} on Leave)"
                    conflicts.append(f"Coverage Gap: {brand['name']} unstaffed on Day {day} due to {emp_name}'s leave.")
                else:
                    brand_status["daily_status"][day] = f"Active ({emp_name})"
            else:
                active_res = []
                missing_res = []
                for eid, proc in brand["assignments"].items():
                    ename = next((e["name"] for e in EMPLOYEES if e["id"] == eid), "Unknown")
                    if any(l["emp_id"] == eid and l["day"] == day for l in LEAVES):
                        missing_res.append(f"{ename} ({proc})")
                    else:
                        active_res.append(f"{ename} ({proc})")
                
                if missing_res:
                    brand_status["daily_status"][day] = f"⚠️ Partial ({', '.join(missing_res)} on leave)"
                    conflicts.append(f"Multi-Resource Gap: {brand['name']} missing personnel on Day {day}: {', '.join(missing_res)}")
                else:
                    brand_status["daily_status"][day] = f"Covered ({', '.join(active_res)})"
                    
        schedule.append(brand_status)

    return schedule, conflicts

def get_process_view():
    processes_map = {}
    for brand in BRANDS:
        for proc in brand["processes"]:
            if proc not in processes_map:
                processes_map[proc] = []
            assigned_emps = [e["name"] for e in EMPLOYEES if e["id"] in brand["assignments"]]
            processes_map[proc].append({
                "brand_name": brand["name"],
                "rule": brand["rule"],
                "assigned": ", ".join(assigned_emps)
            })
    return processes_map

def get_employee_view():
    days = list(range(1, CURRENT_MONTH_DAYS + 1))
    emp_schedules = []
    for emp in EMPLOYEES:
        emp_leaves = [l["day"] for l in LEAVES if l["emp_id"] == emp["id"]]
        assigned_brands = [b["name"] for b in BRANDS if emp["id"] in b["assignments"]]
        emp_schedules.append({
            "id": emp["id"],
            "name": emp["name"],
            "pod": emp["pod"],
            "role": emp["role"],
            "assigned_brands": ", ".join(assigned_brands) if assigned_brands else "Support Pool",
            "leaves": emp_leaves
        })
    return emp_schedules
