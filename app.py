from flask import Flask, render_template, request 
from flask_mail import *
from random import *
import mysql.connector


app = Flask(__name__)

app.config["MAIL_SERVER"] = "stmp.gmail.com" #sending emails
app.config["MAIL_PORT"] = 465 #secure channel
app.config["MAIL_USERNAME"] = "@gmail.com" 
app.config["MAIL_PASSWORD"] = "ojoukrigdwnofixq"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
mail = Mail(app) #initializes Flask-mail with app configuration

otp = randint(0000,9999) #generate a random otp


@app.route("/verify", methods = ["POST"])
def verify():
   email = request.form["email"]
   msg = Message("OTP", sender="codingaltestmail@gmail.com", recipients=[email])
   msg.body = str(otp)
   mail.send(msg)
   return render_template("page.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate")
def validate():
    user_otp = request.form["otp"]
    if otp == int(user_otp):
        return "<h3>Email Verification Successfull</h3>"
    else:
        return "<h3>verification failed.otp does not match</h3>"
    
    
    return render_template("page.html")




app.run(host="0.0.0.0", port=80, debug=True)