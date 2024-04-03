from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['job_database']
collection = db['job_collection']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page1')
def page1():
    # Retrieve job data from MongoDB
    jobs_data = collection.find()
    return render_template('page1.html', jobs_data=jobs_data)

@app.route('/page2')
def page2():
    # Retrieve job data from MongoDB
    jobs_data = collection.find()
    return render_template('page2.html', jobs_data=jobs_data)

if __name__ == '__main__':
    app.run(debug=True)
