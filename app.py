from flask import Flask, render_template, url_for ,request, redirect, flash
import os,random
from pymongo import MongoClient
from flask_cors import CORS

app= Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "ghsdgfbyusgfbyujhfgbj"

client = MongoClient("mongodb+srv://harshitgadhiya8980:harshitgadhiya8980@cluster0.xradpzd.mongodb.net/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submitdata', methods=["GET", "POST"])
def submitdata():
    fullname = request.form.get("fullname", "")
    email = request.form.get("email", "")
    phone = request.form.get("phone", "")
    question = request.form.get("question", "")
    db = client["marketwisebhargav"]
    coll = db["userdata"]
    coll.insert_one({"full_name": fullname, "email": email, "phone": phone, "question": question})
    flash("Your request submitted successfully...", "success")
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
