# Udacity-IPND-Logs-Analysis

# Description
>Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

>1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

>2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

>3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

# Good coding practices
SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.

# Download Software

1. Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.



# Run the Program
To load the NEWS database, cd into the vagrant directory and use the command ''' psql -d news -f newsdata.sql. '''

psql — the PostgreSQL command line program
```-d news``` — connect to the database named news which has been set up for you
```-f newsdata.sql``` — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.


# Please Create the following Views:
```
Question 1:

CREATE VIEW popular_articles AS
SELECT a.title articles, count(l.path) AS views
FROM log l
JOIN articles a
ON l.path = concat('/article/', a.slug)
GROUP BY articles
ORDER BY views desc
limit 3;

Question 2:

CREATE VIEW popular_authors AS
SELECT au.name AS authors, count(l.path) as views
FROM log l
JOIN articles a
ON l.path = concat('/article/', a.slug)
JOIN authors au
ON au.id = a.author 
GROUP BY au.name
ORDER BY views desc;

Question 3:

CREATE VIEW requests AS
SELECT date(time) date, count(*) AS views
FROM log 
GROUP BY date
ORDER BY views;

CREATE VIEW errors AS
SELECT date(time) date, count(*) AS errors
FROM log 
WHERE status != '200 OK'
GROUP BY date
ORDER BY errors;

CREATE VIEW max_errors AS
SELECT requests.date, round((100.0 * errors.errors)/requests.views,3) as percent
FROM requests
JOIN errors
ON errors.date = requests.date
GROUP BY requests.date, errors.errors, requests.views
ORDER BY percent desc;
```

# References 
https://classroom.udacity.com/courses/ud198
https://www.postgresql.org/docs/9.5/sql-select.html
https://www.postgresql.org/docs/9.5/functions-string.html
https://www.postgresql.org/docs/9.5/functions-aggregate.html
http://www.postgresqltutorial.com/postgresql-like/
https://www.postgresql.org/docs/8.1/functions-subquery.html
https://www.postgresql.org/docs/9.1/functions-datetime.html
https://www.postgresql.org/docs/9.5/functions-formatting.html
https://www.postgresql.org/docs/9.5/sql-createcast.html
