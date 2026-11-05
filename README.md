# Smart Roster Management System ⚡
*DataStraw Tech Internship Assignment*

A browser-based, enterprise-grade roster management application built to help operations managers plan, generate, validate, and manage monthly rosters across multiple brands, processes, and pods.

---

## 🚀 Live Demo & Repository
* **Live Application URL:** [Insert Render/Deployment URL Here]
* **GitHub Repository:** [Insert GitHub Repo URL Here]

---

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Jinja2
* **Frontend:** Bootstrap 5, Custom Neo-Glass CSS, FontAwesome
* **Architecture:** Deterministic constraint-satisfaction scheduling engine with real-time validation.

---

## 📋 Core Features
1. **Central Architecture:** Manages 30 employees across 6 pods, 12 D2C brands (single and multi-resource models), and multiple processes (Customer Support, NDR, Cart Recovery).
2. **Strict Operating Rules:** Supports 365-day operations, Mon–Sat schedules, and process-specific calendars.
3. **Monthly Roster Matrix:** Full 30-day/7-day cycle generation showing daily status for every brand.
4. **Advanced Conflict Detection:** Real-time flagging for unstaffed brand coverage gaps, multi-resource leave dropouts, and daily leave capacity limits (max cap: 4 leaves/day).
5. **5 Mandatory Stakeholder Views:** Company-wide/Brand Matrix, Pod-wise, Process-wise, and Employee-wise views.
6. **Change Management:** Instant leave simulation, manual overrides, and automated backup assignment workflows.

---

## 📝 Approach Note

### 1. System Architecture
The system is built using Flask (Python) for the deterministic scheduling engine and Bootstrap/CSS for a data-dense Neo-Glass dashboard. The architecture strictly separates data modeling (`logic.py`), HTTP route orchestration (`app.py`), and UI presentation (`dashboard.html`).

### 2. Core Scheduling & Constraint Satisfaction Logic
* **Operating Rules vs. Employee Calendars:** The engine distinguishes between brand operational rules (e.g., 365-day vs. Mon–Sat) and individual agent schedules.
* **Conflict Validation Engine:** The matrix evaluates 30-day cycles for single-resource unstaffed gaps, multi-resource coverage drops, and daily leave capacity limits (capped at max 4 leaves/day).
* **Automated & Manual Override Workflows:** When a single-resource coverage gap occurs due to approved leave, the manager can trigger an automated support-pool backup or manually assign an alternate agent without altering the core codebase.

### 3. Key Design Decisions
* **Deterministic Matrix Engine:** Prioritized predictable, rule-based constraint checking over probabilistic AI generation to guarantee 100% compliance with hard client coverage rules.
* **Modular Stakeholder Views:** Tabbed views (Company, Pod, Process, Employee) provide actionable visibility for Pod Leads and Operations Managers alike.

---

## 🧠 Architectural Approach & Design Decisions Q&A

### 1. How did you model employees, brands, processes, pods, and their relationships?
Employees are modeled as structured dictionaries containing a unique integer `id`, full `name`, operational `pod` affiliation, and role (`Pod Lead` vs. `Agent`). Brands maintain a structured portfolio containing their operational model (`Single-Resource` vs. `Multi-Resource`), assigned processes, resource ID mappings, and operating rules (`365 Days` vs. `Mon–Sat`). Pods group employees dynamically for team-level administrative oversight.

### 2. How does your system generate a roster and determine whether it satisfies required constraints?
The roster generator runs on a deterministic rule-based engine (`logic.py`). It iterates through each day of the configured monthly cycle (7, 15, or 30 days) and evaluates operating rules (skipping Sundays for `Mon–Sat` brands), cross-references employee leave logs and manual overrides, and compares aggregate daily leave counts against hard limits (max cap: 4 leaves/day) to flag unstaffed single-resource gaps into a centralized conflict array.

### 3. How did you handle the difference between single-resource brands and brands with multiple employees?
* **Single-Resource Brands:** Mapped to exactly 1 dedicated employee responsible for the brand's core process. If that individual is on leave, the engine immediately flags an unstaffed coverage failure for that specific day.
* **Multi-Resource Brands:** Mapped to multiple employees across discrete parallel processes (e.g., Customer Support + NDR). The engine validates each resource independently; if one team member is absent, it flags a partial coverage gap without halting the entire brand's operations.

### 4. What happens when an employee manages all processes for a brand but is unavailable on a required working day?
When an exclusive resource is unavailable due to an approved leave:
1. The monthly matrix explicitly flags the day with a red `⚠️ Unstaffed` status.
2. A prominent warning banner appears at the top of the manager's command center detailing the exact coverage gap.
3. The manager can instantly deploy an automated support-pool backup or execute a manual override to reassign coverage.

### 5. How does your system handle conflicting requirements or insufficient staffing?
When conflicting requirements occur (such as exceeding the daily maximum leave cap of 4 employees or simultaneous absences on critical single-resource brands), the system **fails transparently** rather than silently ignoring the rule. It aggregates all constraint breaches into an explicit list of validation conflicts displayed on the dashboard, allowing operations managers to review and resolve them via automated backups or manual overrides.

### 6. Which parts of the process did you automate, and which did you leave under human control? Why?
* **Automated:** Monthly calendar grid generation, Sunday rule skipping, leave capacity threshold tracking, conflict detection, and CSV report formatting. This eliminates tedious manual spreadsheet calculations and human error.
* **Human-Controlled:** Leave approvals, manual overrides, and backup assignments. This is intentional because workforce management requires managerial discretion to handle nuanced business priorities, client escalations, and unexpected operational emergencies.

### 7. If the company doubled its team and brand count, what would you change about your solution?
* **Data Storage:** Migrate from in-memory Python dictionaries and lists to a relational database (such as PostgreSQL) utilizing an ORM (like SQLAlchemy) for persistent, ACID-compliant storage.
* **Backend Scalability:** Decouple the scheduling engine into microservices or asynchronous task queues (e.g., Celery) to handle heavier computational matrix loads without blocking HTTP server threads.
* **Frontend Pagination:** Implement virtualized tables and pagination on the matrix grid to maintain sub-second rendering speeds across large data sets.

### 8. If you had one additional week to work on this, what would you improve first?
I would implement **Preference-Based Automated Shift Optimization** using constraint-satisfaction solvers (such as Google OR-Tools). This would allow agents to submit preferred weekly off-days or shift preferences, and have the engine mathematically optimize fair distribution of workloads while automatically balancing team coverage and operational constraints.

---

## ⚙️ Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-roster-system.git](https://github.com/YOUR_USERNAME/smart-roster-system.git)
   cd smart-roster-system
   