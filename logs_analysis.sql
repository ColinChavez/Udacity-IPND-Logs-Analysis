--What are the three most popular articles?
CREATE VIEW popular_articles AS
SELECT a.title articles, count(l.path) AS views
FROM log l
JOIN articles a
ON l.path = concat('/article/', a.slug)
GROUP BY articles
ORDER BY views desc
limit 3;

--Who are the most popular authors?
CREATE VIEW popular_authors AS
SELECT au.name AS authors, count(l.path) as views
FROM log l
JOIN articles a
ON l.path = concat('/article/', a.slug)
JOIN authors au
ON au.id = a.author 
GROUP BY au.name
ORDER BY views desc;

-- Which day did more than 1% of requests lead to errors?
CREATE VIEW requests AS
SELECT date(time) date, count(*) AS views
FROM log 
GROUP BY date
ORDER BY views;


CREATE VIEW errors AS
SELECT date(time) date, count(*) AS errors
FROM log 
WHERE status != '200 OK'
GROUP BY date
ORDER BY errors;

CREATE VIEW max_errors AS
SELECT requests.date, round((100.0 * errors.errors)/requests.views,3) as percent
FROM requests
JOIN errors
ON errors.date = requests.date
GROUP BY requests.date, errors.errors, requests.views
ORDER BY percent desc;