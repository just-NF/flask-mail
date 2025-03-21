from flask import Flask, render_template, request 
import mysql.connector


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate")
def validate():
    return render_template("page.html")




app.run(host="0.0.0.0", port=80, debug=True)