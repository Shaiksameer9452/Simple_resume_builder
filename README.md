#  Simple Resume Builder

A web-based Resume Builder application built using **Flask, SQLite, HTML, CSS, and Jinja2**.  
This application allows users to create, preview, and download a professional resume easily.



##  Features

- Create a resume with personal details
- Add multiple skills
- Add multiple projects
- Prevent duplicate project entries
- Update existing resume without changing user ID
- Resume preview page
- Print / Download as PDF
- Clean and modern UI
- Basic caching using `functools.cache`



##  Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
- functools.cache (for performance optimization)



##  Project Structure
~~~~
resume-builder/
│
├── app.py
├── resume.db
├── requirements.txt
│
├── templates/
│ ├── layout.html
│ ├── home.html
│ ├── create.html
│ └── preview.html
│
└── static/
└── style.css
~~~~


##  Database Design

### Users Table
- id (Primary Key)
- name
- email

### Resumes Table
- id (Primary Key)
- user_id (Foreign Key)
- phone
- education
- skills
- projects
- created_at



##  How Resume Updating Works

- If a user submits the same email again:
  - The existing resume is updated
  - New projects are appended
  - Duplicate projects are automatically removed
  - Resume ID remains unchanged



##  Caching

The preview route uses:

This improves performance by caching resume data.  
Cache is cleared automatically when the resume is updated.



##  Learning Objectives

- Flask routing
- SQL database integration
- CRUD operations
- Jinja templating
- Form handling
- Caching optimization
- Clean UI design



##  Future Improvements

- User authentication system
- Edit mode with pre-filled form
- Delete project feature
- Multiple resume templates
- Export directly to PDF
- Deployment on cloud



##  Author

Developed as a learning project to practice full-stack web development using Flask.



##  License

This project is for educational purposes.




