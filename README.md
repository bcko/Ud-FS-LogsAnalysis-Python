# Logs-Analysis


## About the logs analysis project
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### Why this project?
In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

#### Report generation
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

#### Database as shared resource
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.

![Just one of many queries Udacity uses for logs analysis](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bf410d_pasted-image-at-2016-08-24-18-22/pasted-image-at-2016-08-24-18-22.png)

Just one of many queries Udacity uses for logs analysis.

## Review Your Skill
Completing this project will exercise your database skills. Here are some portions of the Relational Databases course that you might want to review:

* Joining tables
* The select ...where statement
* Select clauses
* Writing code with DB-API
* Views

### The PostgreSQL documentation
In this project, you'll be using a PostgreSQL database. If you'd like to know a lot more about the kinds of queries that you can use in this dialect of SQL, check out the PostgreSQL documentation. It's a lot of detail, but it spells out all the many things the database can do.

Here are some parts that may be particularly useful to refer to:
* The select statement
* SQL string functions
* Aggregate functions

## Prepare the software and data
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

### The virtual machine
This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons.

If you skipped those lessons and came right to this project, that's OK! However, you will need to go back to these instructions to install the virtual machine. This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
_Successfully logged into the virtual machine._
Successfully logged into the virtual machine.

### Download the data
Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson.

To load the data, use the command psql -d news -f newsdata.sql.
Here's what this command does:

* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

#### Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

### Explore the data
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

* \dt — display tables — lists the tables that are available in the database.
* \d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.


## Your assignment: Build it!
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:

* July 29, 2016 — 2.5% errors

### Good coding practices
#### SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

#### Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.
