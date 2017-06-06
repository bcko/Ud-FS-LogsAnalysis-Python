#!/usr/bin/env python3

'''
psycopg is the PostgreSQL adapter for the Python programming language. 
Some database code and comments are adapted from the psycopg documentation(http://initd.org/psycopg/)
'''
import psycopg2 

def main():
  
  question1 = "1. What are the most popular three articles of all time?\n\
  Which articles have been accessed the most?\n\
  Present this information as a sorted list with the most popular article at the top\n"
  '''
  Example:
      "Princess Shellfish Marries Prince Handsome" — 1201 views
      "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
      "Political Scandal Ends In Political Scandal" — 553 views
  '''
  
  question2 = "2. Who are the most popular article authors of all time?\n\
  That is, when you sum up all of the articles each author has written, which authors get the most page views?\n\
  Present this as a sorted list with the most popular author at the top.\n"
  '''
  Example:
      Ursula La Multa — 2304 views
      Rudolf von Treppenwitz — 1985 views
      Markoff Chaney — 1723 views
      Anonymous Contributor — 1023 views
  '''
  
  question3 = "3. On which days did more than 1% of requests lead to errors?\n\
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.\n"
  '''
  Example:
      July 29, 2016 — 2.5% errors
  '''
  
  
  
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
