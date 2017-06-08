#!/usr/bin/env python3

'''
psycopg is the PostgreSQL adapter for the Python programming language. 
Some database code and comments are adapted from the psycopg documentation(http://initd.org/psycopg/)
'''
import psycopg2 

def main():  
  
  question1 = """ 
  1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
  """

  q1_SQL = """ 
  SELECT articles.title, COUNT(log.path) as num_access 
  FROM articles, log
  WHERE log.path = '/article/' || articles.slug
  GROUP BY articles.title
  ORDER BY num_access DESC
  LIMIT 3;
  """
  
  question2 = """
  2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
  """
  
  q2_SQL = """
  SELECT authors.name
  FROM authors, articles, log
  WHERE articles.author = authors.id
      AND log.path = '/article/' || articles.slug
  GROUP BY 
  """
  
  question3 = """
  3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
  """
  
  q3_SQL = """
  
  """

  
  
  
  # Connect to an existing database
  conn = psycopg2.connect("dbname=news")
  
  # Open a cursor to perform database operations
  cur = conn.cursor()

  
  
  print(question1)
  
  
  print(question2)
  
  
  print(question3) 

  
  
  
  # Close communication with the database
  cur.close()
  conn.close()
  
if __name__ == "__main__":
    # execute only if run as a script
    main()
