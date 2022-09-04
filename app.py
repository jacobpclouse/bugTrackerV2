from email.policy import default
import sqlite3
from markupsafe import escape
from flask import Flask, render_template, abort, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'

# Init the Database
db = SQLAlchemy(app)

# Create Database model
class Issues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueReporter = db.Column(db.String(200), nullable=False)
    issueDate = db.Column(db.DateTime, default=datetime.utcnow)
    issueTitle = db.Column(db.String(200), nullable=False)
    issueDescription = db.Column(db.String(2000), nullable=False)
    issueLocation = db.Column(db.String(200), nullable=False)
    issueType = db.Column(db.String(200), nullable=False)

    # function to return string when added to db
    def __repr__(self):
        return "<issueReporter %r" % self.id


## Routes to all pages
# 404 page
@app.route('/404')
def pageNotFound():
    return render_template('404.html')


# all open issues
@app.route('/all')
def allOpenIssues():
    return render_template('all_open.html')


# issues assigned to me
@app.route('/assigned')
def assignedToMe():
    return render_template('assigned_to_me.html')


# overall dashboard
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# reporting an issue screen
@app.route('/report')
def reportAnIssue():
    return render_template('report_an_issue.html')


# any unhandled issues
@app.route('/unhandled')
def unhandledIssues():
    return render_template('unhandled.html')