import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from functools import cache   

app = Flask(__name__)


# DATABASE CONNECTION

def get_db():
    conn = sqlite3.connect("resume.db")
    conn.row_factory = sqlite3.Row  
    return conn

# CACHED FUNCTION

@cache
def get_resume_data(resume_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT users.name, users.email,
               resumes.phone, resumes.education,
               resumes.skills, resumes.projects
        FROM resumes
        JOIN users ON resumes.user_id = users.id
        WHERE resumes.id = ?
    """, (resume_id,))

    resume = cursor.fetchone()
    db.close()
    return resume

# HOME PAGE

@app.route("/")
def home():
    return render_template("home.html")

# CREATE 

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        education = request.form["education"]
        skills = request.form["skills"]
        projects = request.form["projects"]
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        db = get_db()
        cursor = db.cursor()

        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            user_id = cursor.lastrowid
        else:
            user_id = user["id"]

        # Check if resume exists
        cursor.execute("SELECT id FROM resumes WHERE user_id = ?", (user_id,))
        resume = cursor.fetchone()

        if resume:
            #  Get old projects
            cursor.execute("SELECT projects FROM resumes WHERE user_id = ?", (user_id,))
            old_data = cursor.fetchone()
            old_projects = old_data["projects"] if old_data and old_data["projects"] else ""

            #  Convert old and new projects into lists
            old_list = old_projects.split("\n") if old_projects else []
            new_list = projects.split("\n") if projects else []

            #  Combine both lists
            combined = old_list + new_list

            #  Remove duplicates and empty lines 
            cleaned_projects = []
            for p in combined:
                p = p.strip()
                if p and p not in cleaned_projects:
                    cleaned_projects.append(p)

            #  Convert back to string
            updated_projects = "\n".join(cleaned_projects)

            cursor.execute("""
                UPDATE resumes
                SET phone = ?, education = ?, skills = ?, projects = ?
                WHERE user_id = ?
            """, (phone, education, skills, updated_projects, user_id))

            resume_id = resume["id"]

        else:
            # First time resume creation
            cleaned_projects = []
            for p in projects.split("\n"):
                p = p.strip()
                if p and p not in cleaned_projects:
                    cleaned_projects.append(p)

            final_projects = "\n".join(cleaned_projects)

            cursor.execute("""
                INSERT INTO resumes (user_id, phone, education, skills, projects, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, phone, education, skills, final_projects, created_at))

            resume_id = cursor.lastrowid

        db.commit()
        db.close()

        # Clear cache after updating database
        get_resume_data.cache_clear()

        return redirect(url_for("preview", id=resume_id))

    return render_template("create.html")

# PREVIEW RESUME

@app.route("/preview/<int:id>")
def preview(id):

    resume = get_resume_data(id)

    if not resume:
        return "Resume not found", 404

    return render_template("preview.html", resume=resume)


if __name__ == "__main__":
    app.run(debug=True)
