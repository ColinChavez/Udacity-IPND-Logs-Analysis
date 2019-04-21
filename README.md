# Udacity-IPND-Logs-Analysis

# Description
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors
Good coding practices
SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.

# Running the Program

Download VirtualBox and Vagrant
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
https://www.vagrantup.com/downloads.html

This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.

If you need to bring the virtual machine online (with vagrant up), do so now. Then log into it with vagrant ssh.

Download the NEWS Database

Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file:https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Note: If you are using Windows OS you will find a Time Out error, to fix it use the new Vagrant file configuration to replace you current Vagrant file.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:


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
