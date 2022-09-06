from crypt import methods
from email.policy import default
import sqlite3
from turtle import title
from markupsafe import escape
from flask import Flask, render_template, abort, request, redirect, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Database setup 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'

# Init the Database
db = SQLAlchemy(app)

# Create Database model -- Will make fields required later
class Issues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueReporter = db.Column(db.String(200))
    #issueReporter = db.Column(db.String(200), nullable=False)
    reporterPhone = db.Column(db.Float(10))
    issueDate = db.Column(db.DateTime, default=datetime.utcnow)
    issueTitle = db.Column(db.String(200))
    #issueTitle = db.Column(db.String(200), nullable=False)
    issueDescription = db.Column(db.String(1000))
    #issueDescription = db.Column(db.String(1000), nullable=False)
    issueLocation = db.Column(db.String(200))
    #issueLocation = db.Column(db.String(200), nullable=False)
    issueType = db.Column(db.String(200))
    #issueType = db.Column(db.String(200), nullable=False
    issueAssigned = db.Column(db.Boolean, default=False)
    issueResolved = db.Column(db.Boolean, default=False)

    # function to return string when added to db
    def __repr__(self):
        return "<issueReporter %r" % self.id


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
## Routes to all pages
# 404 page
@app.route('/404')
def pageNotFound():
    title = "JPC Bug Tracker | 404 Error"
    return render_template('404.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# all open issues
@app.route('/all', methods=['POST', 'GET'])
def allOpenIssues():
    title = "JPC Bug Tracker | All Open"
    return render_template('all_open.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# issues assigned to me
@app.route('/assigned', methods=['POST', 'GET'])
def assignedToMe():
    title = "JPC Bug Tracker | Assigned to Me"
    return render_template('assigned_to_me.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# overall dashboard
@app.route('/')
@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    title = "JPC Bug Tracker | Dashboard"
    return render_template('dashboard.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# reporting an issue screen
@app.route('/report', methods=['POST', 'GET'])
def reportAnIssue():
    title = "JPC Bug Tracker | Report an Issue"

    if request.method == "POST":

        # 1st Step -- Adding to DB
        # need to have them all part of an object then add the object
        issue_Reporter = request.form["html_reporter"]
        ##add_reporter = Issues(issueReporter=issue_Reporter)

        reporter_Phone = request.form["html_phone"]
        ##add_phone = Issues(reporterPhone=reporter_Phone)

        issue_Title = request.form["html_title"]
        ##add_title = Issues(issueTitle=issue_Title)

        issue_Description = request.form["html_description"]
        ##add_description = Issues(issueDescription=issue_Description)

        issue_Location = request.form["html_location"]
        ##add_location = Issues(issueLocation=issue_Location)

        issue_Type = request.form["html_archetype"]
        ##add_type = Issues(issueType=issue_Type)

        # Putting all values into one object and then adding/commiting that to the DB
        addAllVal = Issues(issueReporter=issue_Reporter,reporterPhone=reporter_Phone,issueTitle=issue_Title,issueDescription=issue_Description,issueLocation=issue_Location,issueType=issue_Type)


        # 2nd Step -- Committing to DB
        try:
            #db.session.add(add_reporter,add_phone,add_title,add_description,add_location,add_type)
            ##db.session.add(add_reporter)
            db.session.add(addAllVal)
            db.session.commit()
            return redirect('/unhandled')

        except: 
            return redirect('/404', title = title) # if there is an issue, will return to 404 page
    else:
        return render_template('report_an_issue.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# resolved issues
@app.route('/resolved', methods=['POST', 'GET'])
def resolvedIssues():
    title = "JPC Bug Tracker | Resolved"
    return render_template('resolved.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# sign in / sign up
@app.route('/login', methods=['POST', 'GET'])
def loginPage():
    title = "JPC Bug Tracker | Login"
    return render_template('sign_in.html', title = title)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# any unhandled issues
@app.route('/unhandled', methods=['POST', 'GET'])
def unhandledIssues():
    title = "JPC Bug Tracker | Unhandled"

    # Run query to see all unhandled issues in DB
    unhandledIssuesForm = Issues.query.order_by(Issues.issueDate)

    return render_template('unhandled.html', title = title, Unhandled_issues = unhandledIssuesForm)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# # SELECTED SPECIFIC ISSUE /issue/<int:user_id>
@app.route('/issue/<int:issue_id>', methods=['POST', 'GET'])
def specificIssue(issue_id):
    title = f"JPC Bug Tracker | Issue No: {issue_id}"
    issueNumber = Issues.query.filter_by(id=issue_id)
    # issueNumber = Issues.query.filter_by(id=issue_id).all()
    # issueNumber = Issues.query.filter_by(id=issue_id)
    return render_template('selected_issue.html', title = title, current_Issue = issueNumber )
## TRY having it so that you click a link that uses id in the url, then that id pulls the data from the db and displays it
    # try:
    #     issueNumber = Issues.query.filter_by(id=issue_id)
    #     return render_template('selected_issue.html', current_Issue = issueNumber )
    # except IndexError:
    #     abort(404)
    
        