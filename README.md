# Smart Roster Management System ⚡
*DataStraw Tech Internship Assignment*

A web application designed for operations managers to create, track, and manage monthly work schedules across different brands, teams, and business processes.

---

## 🚀 Live Demo & Repository
* **Live Application URL:** [Insert Render/Deployment URL Here]
* **GitHub Repository:** [Insert GitHub Repo URL Here]

---

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Jinja2
* **Frontend:** Bootstrap 5, Custom CSS, FontAwesome
* **Logic:** Custom rule-based scheduling engine with instant validation.

---

## 📋 Core Features
1. **Central Dashboard:** Manages 30 employees, 6 teams (pods), 12 client brands, and key daily tasks.
2. **Workplace Rules:** Supports 7-day operations, Mon–Sat working schedules, and team-specific calendars.
3. **Monthly View:** Generates full 30-day schedule grids showing daily staff coverage for every brand.
4. **Automatic Issue Detection:** Instantly flags understaffed brands, missing staff on single-person accounts, and days where too many people are on leave (max 4 leaves per day).
5. **Clear Manager Views:** Switch between Company-wide, Pod-wise, Process-wise, and Employee-wise views.
6. **Easy Schedule Changes:** Simple forms to request leave, assign cover staff, and override shifts manually.

---

## 📝 Approach Note

### 1. System Design
The app uses Python (Flask) to run the schedule calculations and a clean HTML/CSS web layout for the manager dashboard. Data setup, page routes, and visual designs are kept clearly separate so the code stays easy to manage.

### 2. Schedule Calculation & Constraint Logic
* **Business Rules vs. Employee Days Off:** The system tracks company working days separately from individual employee leave days.
* **Smart Issue Checking:** The app automatically checks for short-staffed brands or days where leave limits are exceeded.
* **Backup Handling:** If an employee managing a brand is absent, the manager can assign a backup cover staff with a single click.

### 3. Key Design Choices
* **Rule-Based Engine:** Built with strict logic rules to ensure client working requirements are always met accurately.
* **Multi-Tab Layout:** Designed tabbed views so managers can quickly check overall company status or focus on a single team member.

---

## 🧠 Approach & Design Q&A

### 1. How are employees, brands, processes, and teams organized?
Each employee has a profile with their name, team (pod), and job title. Each brand has set rules (working days, required tasks, and assigned staff). Teams group employees together so managers can view and supervise specific groups easily.

### 2. How does the system build the schedule and check for mistakes?
The system loops through all 30 days of the month. It skips non-working days (like Sundays for 6-day brands), checks who is on leave, counts total daily absences, and highlights any day that goes over the 4-person leave limit or leaves a brand without staff.

### 3. How are single-person brands handled compared to multi-person brands?
* **Single-Person Brands:** Managed by 1 primary employee. If that person takes leave, the system immediately flags the brand as understaffed for that day.
* **Multi-Person Brands:** Managed by several employees handling different tasks. If one person is away, the system flags the missing role without stopping the entire brand's operations.

### 4. What happens when the only person managing a brand is absent?
When an exclusive brand manager goes on leave:
1. The 30-day schedule grid marks that day in red as `⚠️ Unstaffed`.
2. A red alert banner appears at the top of the manager's dashboard.
3. The manager can click to assign a backup staff member right away.

### 5. How does the app handle scheduling conflicts or shortage of staff?
Instead of ignoring errors or guessing solutions, the app shows clear warning alerts on the dashboard. This lets operations managers quickly see every issue and decide how to resolve it.

### 6. Which parts are automated, and which parts are left for humans to decide?
* **Automated:** Creating the monthly schedule grid, skipping Sundays, counting daily leaves, flagging understaffed brands, and exporting reports.
* **Human-Controlled:** Approving leave requests and deciding which backup staff member covers a shift. This leaves important decision-making in the hands of managers.

### 7. What would change if the company doubled its size?
* **Database:** Move from temporary in-memory data to a dedicated database (like PostgreSQL) to store larger amounts of staff and brand information safely.
* **Performance:** Upgrade the background calculations so large monthly schedules load without slowing down the webpage.
* **Table Pagination:** Add page numbers to tables so managers can navigate long staff lists comfortably.

### 8. What would be improved first with one extra week of development time?
I would add **Smart Shift Preferences**, allowing employees to submit their preferred days off so the system can automatically balance fair shift distribution while keeping brands fully staffed.

---

## ⚙️ Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/ShiyaStudio8/smart-roster-system.git](https://github.com/ShiyaStudio8/smart-roster-system.git)
   cd smart-roster-system
   