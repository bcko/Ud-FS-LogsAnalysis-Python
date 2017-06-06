#!/usr/bin/env python3

# psycopg is the PostgreSQL adapter for the Python programming language. 
import psycopg2 


def main():
  conn = psycopg2.connect("dbname=news")
  cursor = conn.cursor()

  
  conn.close()
  
if __name__ == "__main__":
    # execute only if run as a script
    main()
