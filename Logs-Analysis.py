#!/usr/bin/env python3

"""
psycopg is the PostgreSQL adapter for the Python programming language. 
Some database code and comments are adapted from the psycopg documentation(http://initd.org/psycopg/)
"""
import psycopg2 

def main():  
  
  sql_popular_articles = """ 
    SELECT * 
    FROM article_view 
    ORDER BY article_view.view DESC
    LIMIT 3;
  """

  sql_popular_authors = """
    SELECT article_view.name, SUM(article_view.view) AS author_view
    FROM article_view
    GROUP BY article_view.name
    ORDER BY author_view DESC
    LIMIT 1;
  """
  
  sql_more_than_one_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
  """
  
  # Connect to an existing database
  conn = psycopg2.connect("dbname=news")
  
  # Open a cursor to perform database operations
  cur = conn.cursor()
  
  

  
 

  
  
  
  # Close communication with the database
  cur.close()
  conn.close()
  
if __name__ == "__main__":
    # execute only if run as a script
    main()
