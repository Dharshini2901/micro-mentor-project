
# Micro-Mentor Project 🚀
**A Peer-to-Peer Mentorship Platform built with Django**

### 🌟 Overview
Micro-Mentor is a full-stack web application designed to connect students (Mentees) with industry professionals (Mentors). It simplifies the process of finding guidance through role-based access, professional profiles, and a streamlined request system.

### 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** Django 5.x
* **Database:** SQLite (Development) 
* **Environment:** Virtual Environments (venv) & python-decouple
* **Image Processing:** Pillow

### 🔑 Key Features
* **Dual-Role Authentication:** Specialized signup for Mentors and Mentees using a Custom User Model.
* **Mentorship Requests:** Mentees can send connection requests which Mentors can approve or decline via their dashboard.
* **Dynamic Profiles:** Users can manage biographies, skills, and profile pictures.
* **Security First:** Implemented environment variables (`.env`) to protect sensitive API keys and secrets.
* **Admin Dashboard:** Built-in Django Admin integration for site-wide data management.

### 🚀 How to Run Locally
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Dharshini2901/micro-mentor-project.git](https://github.com/Dharshini2901/micro-mentor-project.git)
   ```
2. **Create & Activate Virtual Environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup Environment Variables:**
   Create a `.env` file and add your `SECRET_KEY`.
5. **Run Migrations & Start Server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
