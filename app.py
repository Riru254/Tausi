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

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    # When User Submits Form
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        package = request.form['package']
        date = request.form['date']
        notes = request.form['notes']

        if not all (name and email and phone and package and date):
            flash("Please fill in all required fields.", "danger")
            return redirect('/booking')

        bookings.insert_one({
            'name': name,
            'email': email,
            'phone': phone,
            'package': package,
            'date': date,
            'notes': notes
        })
        flash("Success on booking, we will reach you with more details", "success")
        return redirect('/booking')
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=False)