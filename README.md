
```sql
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```
