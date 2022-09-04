from flask import Flask, render_template

app = Flask(__name__)



# all open issues
@app.route('/all-open')
def allOpenIssues():
    return render_template('all_open.html')


# issues assigned to me
@app.route('/assigned-to-me')
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