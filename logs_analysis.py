#!/usr/bin/env/python
import psycopg2
import sys


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)
        raise e


def results(query):
    db, c = connect()
    c.execute(query)
    results = c.fetchall()
    c.close()
    return results


def popular_articles():
    """Displays Top 3 Articles"""
    print "What are the most popular three articles of all time?" + '\n'
    query1 = "SELECT * FROM popular_articles;"
    top_articles = results(query1)
    for s in top_articles:
        print'"' + str(s[0]) + '"' + ' - ' + str(s[1]) + ' views'


def popular_authors():
    """Displays Top 3 Articles"""
    print '\n' + "Who are the most popular authors?" + '\n'
    query2 = "SELECT * FROM popular_authors;"
    top_authors = results(query2)
    for s in top_authors:
        print'"' + str(s[0]) + '"' + ' - ' + str(s[1]) + ' views'


def max_errors():
    """Displays Top 1% of Errors"""
    print '\n'
    print "Which day did more than one percent of requests lead to errors?"
    print '\n'
    query3 = ("""SELECT * FROM max_errors
                 WHERE max_errors.percent > 1
                ORDER BY max_errors.percent DESC;""")
    top_errors = results(query3)
    for s in top_errors:
        print'"' + str(s[0]) + '"' + ' - ' + str(s[1]) + ' errors'


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    max_errors()
