
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Student {self.sno} - {self.first_name} {self.last_name}>"

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Create (C in CRUD)
        first_name = request.form.get("first_name", "").strip()
        last_name  = request.form.get("last_name", "").strip()
        email      = request.form.get("email", "").strip()
        phone      = request.form.get("phone", "").strip()

        if not first_name or not last_name or not email:
            flash("First name, last name and email are required.", "danger")
            return redirect(url_for("index"))

        try:
            student = Student(first_name=first_name, last_name=last_name, email=email, phone=phone)
            db.session.add(student)
            db.session.commit()
            flash("Student added successfully.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding student: {e}", "danger")
        return redirect(url_for("index"))

    # Read (R in CRUD)
    q = request.args.get("q", "").strip()
    if q:
        # simple search by name or email
        like = f"%{q}%"
        students = Student.query.filter(
            (Student.first_name.ilike(like)) |
            (Student.last_name.ilike(like))  |
            (Student.email.ilike(like))
        ).order_by(Student.created_at.desc()).all()
    else:
        students = Student.query.order_by(Student.created_at.desc()).all()

    return render_template("index.html", students=students, q=q)

@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    student = Student.query.get_or_404(sno)

    if request.method == "POST":
        # Update (U in CRUD)
        student.first_name = request.form.get("first_name", student.first_name).strip()
        student.last_name  = request.form.get("last_name", student.last_name).strip()
        student.email      = request.form.get("email", student.email).strip()
        student.phone      = request.form.get("phone", student.phone).strip()

        try:
            db.session.commit()
            flash("Student updated successfully.", "success")
            return redirect(url_for("index"))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating student: {e}", "danger")
            return redirect(url_for("update", sno=sno))

    # GET -> show the form prefilled
    return render_template("update.html", student=student)

@app.route("/delete/<int:sno>", methods=["POST"])
def delete(sno):
    # Delete (D in CRUD)
    student = Student.query.get_or_404(sno)
    try:
        db.session.delete(student)
        db.session.commit()
        flash("Student deleted.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting student: {e}", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Allow host override via env var for containers, default 127.0.0.1
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port, debug=True)
