
```sql
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
SELECT path, COUNT(*) as view
FROM log
GROUP BY path
ORDER BY path;
```
