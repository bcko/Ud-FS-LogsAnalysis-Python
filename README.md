# Logs Analysis Project

## Requirements
* Python 3.5.3
* psycopg2
* Postgresql 9.6

## How to run

### Create Views
```sql
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
CREATE VIEW view_per_path AS
SELECT path, COUNT(*) as view
FROM log
GROUP BY path
ORDER BY path;
```
