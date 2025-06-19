from flask import Flask, request, render_template, redirect, flash
#from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'secret123'

# MongoDB config
#client = MongoClient("mongodb+srv://murirufranklinw:p2hzS3RbSr2k6L9s@clusterlearning.ab9rzkd.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLearning") #Connects to Mongo
#db = client["tausit&t"] #Use the database specified
#bookings = db["tausibookings"] #Use collection specified


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')


if __name__ == '__main__':
    app.run(debug=False)