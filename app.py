import cv2
from flask import Flask, render_template, session, redirect, request, url_for, Response
import os
import firebase_admin
import sys
from subprocess import run,PIPE
from firebase_admin import credentials, firestore
from functools import wraps




cred = credentials.Certificate("eagle-eye-f3a0d-firebase-adminsdk-f8rcz-5d151faa13.json")
firebase_admin.initialize_app(cred, {"projectId":"eagle-eye-f3a0d"})
db = firestore.client()




app = Flask(__name__)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("index"))
    return wrap

def log_out():
    session.clear()
    return redirect(url_for("index"))
    
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        user = db.collection(u"login-users")
        
        results = user.where(u"email", u"==", username).stream()
        for result in results:
           # print("{}".format(result.to_dict()))
           # print(result.to_dict()["email"])
            if username == result.to_dict()["email"] and password == result.to_dict()["pass"]:
                session["logged_in"] = True
                session["username"] = username
                session["uid"] = result.id
                return redirect(url_for("courses"))
                
        
        
        
        
    return render_template("index.html")
    
@app.route("/courses")
@is_logged_in
def courses():
    return render_template("courses.html")


@app.route("/math4212")
@is_logged_in
def math():
    return render_template("attendance.html")

@app.route("/camera_on")
def camera_on():
    out = run([sys.executable,"C://Users//jrrod//Documents//SDproject//eagle-eye//static//face_recognition.py"], shell=False, stdout=PIPE)


if __name__ == "__main__":
   app.secret_key = "pvamu"
   app.run(debug = True)
