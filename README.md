# 🧑‍💼 Job Search App

This is a simple Job Search web application built with **Django**. It demonstrates basic **CRUD (Create, Read, Update, Delete)** operations for job listings.

## 🔧 Features

- 📝 Create a job post
- 📄 View all job posts
- ✏️ Update existing job posts
- ❌ Delete job posts
- 🔍 Simple homepage and job detail view

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap optionally)
- **Database**: SQLite3 (default)


## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/jobsearch_project.git
cd jobsearch
```
2. Create A virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. Install Dependencies
```bash
pip install django
```
4.Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5.Start the server
```bash
python manage.py runserver
```
6.Access the app
```bash
Visit http://127.0.0.1:8000/ in your browser.
```

🙌 Acknowledgements
This project is made as a learning example to understand Django CRUD operations.


