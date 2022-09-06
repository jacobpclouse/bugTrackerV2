# Jacob Clouse's Bug Tracker (ver 2)
This is a helpdesk bug tracker built with flask, modeled off the old HTML version (link here: https://github.com/jacobpclouse/BugTracker-V1)

## Tech Used: 
- Python/Flask
- Google's Fontawesome
- Bootstrap
- CSS Variables & Flexbox
- REST APIs
- DB (????)
- Frontend (????)

## Ideas:
- Gets sample requests from Reddit tech support and from stackoverflow using apis
- stores uses in db
- oauth authentication

- DONE -- setup links on each page to redirect to separate pages
- DONE -- setup signup page
- DONE -- create login page template
- DONE -- setup db to store issues and display them (what fields do i need?) -
- DONE -- create specific issue page 
- DONE -- add assign to me button on all issues
- DONE -- add icon to the page title
- DONE -- show individual issues, reporter, etc

- have it so that you can type comments on the feed (store in db as comments)
- have it so that you can resolve each item when needed
- have a hamberger menu appear for all options (resolved, all, etc) when on phone
- hash database table (security)
- new table for users authentication (relationship to each assigned issue) and for comments
- clickable links on the issue that leads to a unique url where page info is generated and output
- sort issues in tables, have most recent issues push to the top
- Have it so that, once you sign in, you go to the dashboard
- setup db for login- do i need x2 db (one for login, one for issues?) -- TEST
- setup apis to grab issues (and way to grab them on command)
- setup oauth login system 
- improve css (effects and shadows)

- make it responsive
- use the EXTEND funchtion to extend out all pages from base (saves on space)
- add logic to dashboard that shows how many issues have been resolved today, this month, this year & outages from apis 
- all else based on the tech with tim (HTTP requests etc) - https://www.youtube.com/watch?v=dam0GPOAvVI
- ability to filter issues by date time (either buttons or sliders)

## Resources:
- CSS Not being picked up: https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python
- Setup Static Folder in CSS: https://youtu.be/tXpFERibRaU?t=325
- SQLAlchemy Databases in Flask: https://www.youtube.com/watch?v=hbDRTZarMUw
- How to Scrape Reddit's FREE API for Subreddit Stats & Data: https://www.youtube.com/watch?v=1KJ_I5h8FRo
- tkinter Error: https://stackoverflow.com/questions/25905540/importerror-no-module-named-tkinter
- flask template inheritance: https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/
- SQLAlchemy docs Declaring Models: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
- Add favicon to a page: https://www.w3schools.com/html/html_favicon.asp
- Hex Color Converter: https://www.w3schools.com/colors/colors_hexadecimal.asp
- SVG Maker: https://picsvg.com/
- Nth Child CSS: https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child
- Flask SQL Examples: https://www.fullstackpython.com/flask-sqlalchemy-model-examples.html
- **** How To Use an SQLite Database in a Flask Application: https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
- https://stackoverflow.com/questions/17147821/how-to-make-a-whole-row-in-a-table-clickable-as-a-link
- jQuery and Clickable rows: https://befused.com/jquery/clickable-table-row/
- jQuery with Flask: https://pythonprogramming.net/jquery-flask-tutorial/