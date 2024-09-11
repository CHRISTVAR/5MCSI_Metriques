from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comm2
  
@app.route("/contact/")
def contact():
    return "<h2>Ma page de contact</h2>"  # Cette nouvelle route affiche "Ma page de contact"
  
if __name__ == "__main__":
  app.run(debug=True)
