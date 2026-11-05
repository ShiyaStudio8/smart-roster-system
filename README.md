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

## 📝 Approach Note & Architecture Answers

### 1. How did you model employees, brands, processes, pods, and their relationships?
Employees are modeled as dictionaries containing IDs, names, pods, and roles (Pod Lead vs. Agent). Brands maintain a structured portfolio containing their operational model (Single-Resource vs. Multi-Resource), assigned processes, resource ID mappings, and operating rules (365 Days vs. Mon–Sat). Pods group employees dynamically for team-level visibility.

### 2. How does your system generate a roster and determine whether it satisfies required constraints?
The generator loops through configured days in a monthly cycle, checking brand calendars against individual employee leave logs and manual overrides. It flags rule violations—such as unstaffed single-resource brands or days exceeding the maximum leave capacity threshold of 4—into a centralized conflict array before rendering.

### 3. How did you handle single-resource vs. multi-resource brands?
Single-resource brands rely on 1 dedicated employee managing all core processes. Multi-resource brands map multiple employees across specific discrete processes (e.g., Customer Support vs. NDR Management). The engine evaluates multi-resource brands dynamically so that a single absence flags a partial coverage gap without necessarily halting all brand operations.

### 4. What happens when an employee managing all processes for a brand is unavailable?
The engine instantly identifies the coverage failure, flags an `Unstaffed` status on the monthly matrix, triggers a red warning banner in the manager dashboard, and allows the operations manager to apply an automated backup cover or manual override.

### 5. If the company doubled its team and brand count, what would you change?
I would migrate the in-memory Python data structures and lists to a relational database (such as PostgreSQL) using SQLAlchemy ORM to ensure persistent storage, faster indexing, and scalable concurrent user sessions.