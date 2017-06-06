#!/usr/bin/env python3

'''
psycopg is the PostgreSQL adapter for the Python programming language. 
Some database code and comments are adapted from the psycopg documentation(http://initd.org/psycopg/)
'''
import psycopg2 

def main():
  
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
