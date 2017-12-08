# Project Specification : Logs Analysis

## Functionality

### Functionality 
- Running the code displays the correct answers to each of the questions in the lab description.
### Compatibility: Database 
- The code works with the (unchanged) database schema from the lab description. It is OK to add views to the database, but don't modify or rename the existing tables.
### Compatibility: Language 
- The code may be written in Python 2 or Python 3 but must be consistent. It should start with a correct shebang line to indicate the Python version.
### Well-formatted text output 
- The code presents its output in clearly formatted plain text. Imagine that you are looking at this text in an email message, not on a web page.
### Database queries 
- The code connects to and queries an SQL database. It does not use answers hardcoded into the application code.

## Code Quality

### No errors 
- The project code runs without any error messages or warnings from the language interpreter.
### Application code style 
- The code conforms to the PEP8 style recommendations. 
- You can install the `pep8` tool to test this, with `pip install pep8` or `pip3 install pep8` (Python 3). 
- In order for this requirement to pass, running the `pep8` tool on your code should produce *zero* warnings.

### SQL code quality 
- When the application fetches data from multiple tables, it uses a single query with a join, rather than multiple queries. 
- Each of the questions must be answered using one SQL query.

## README file

### README file describes work 
- The README file includes instructions for how to run the program, as well as a description of the program's design. 
- Imagine a person who knows Python and SQL well, but has not done this project. 
- If that person read the README would they know how to run this code?

### README file includes view definitions, if any 
- If the code relies on views created in the database, the README file includes the `create view` statements for these views. (If the code does not depend on views, ignore this requirement.)
