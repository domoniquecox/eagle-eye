import cv2
from flask import Flask, render_template, session, redirect, request, url_for, Response
import os
import firebase_admin
import firebase
import pyrebase
import sys
from subprocess import run,PIPE
from firebase_admin import credentials, firestore
from functools import wraps




config = {
    "apiKey": "AIzaSyDd7CWwzX-cxTMk1tH-pzDEl21-FK6fUsI",
    "authDomain": "eagle-eye-f3a0d.firebaseapp.com",
    "databaseURL": "https://eagle-eye-f3a0d.firebaseio.com",
    "projectId": "eagle-eye-f3a0d",
    "storageBucket": "eagle-eye-f3a0d.appspot.com",
    "serviceAccount": "eagle-eye-f3a0d-firebase-adminsdk-f8rcz-5d151faa13.json",
    "messagingSenderId": "1020036625253"
    }
    
    
    
firebase = pyrebase.initialize_app(config)
db2 = firebase.database()
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


@app.route("/attendance", methods=["GET", "POST"])
@is_logged_in
def faces_recognized():
    if request.method == "POST":
        allposts = db2.child("Students_Present").get()
        faces = allposts.val()
        return render_template("attendance.html", n = faces.values())
    return render_template("attendance.html")

#@app.route("/submit_attendance", methods=["GET" ,"POST"])
#@is_logged_in
#def submit_attendance():
 #   if request.method == "POST":
 #       DomPres = request.form["attendance"]
 #       print(DomPres)
        
#    return render_template("attendance.html")
    
#db_events = db2.child("MyTestData").get().val().values()
#return render_template("attendance.html", MyTestData = db_events)


@app.route("/math4212", )
@is_logged_in
def math():
    
    return render_template("attendance.html")
    
@app.route("/psyc1001" , methods=["GET", "POST"])
@is_logged_in
def psyc():
    return render_template("attendance.html")
    
@app.route("/hlth2223", methods=["GET", "POST"])
@is_logged_in
def hlth2003():
    return render_template("attendance.html")
    
@app.route("/hlth2003", methods=["GET", "POST"] )
@is_logged_in
def hlth2223():
    return render_template("attendance.html")

@app.route("/camera_on")
def camera_on():
    os.system("python face_recognition.py")
    return "hi"

@app.route("/logout")
@is_logged_in
def logOut():
    return render_template("logout.html")


if __name__ == "__main__":
   app.secret_key = "pvamu"
   app.run(debug = True)
