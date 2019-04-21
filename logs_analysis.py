import psycopg2

def popular_articles():
  """Displays Top 3 Articles"""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("SELECT * FROM popular_articles")
  results = c.fetchall()
  db.close()
  return results
  for solution in results:
    print results 

def popular_authors():
  """Displays Top Authors"""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("SELECT * FROM popular_authors")
  results = c.fetchall()
  db.close()
  return results
  for solution in results:
    print results

def max_errors():
  """Displays Top 1% of Errors"""
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("SELECT * FROM max_errors WHERE max_errors.percent > 1 ORDER BY max_errors.percent DESC;")
  results = c.fetchall()
  db.close()
  return results
  for solution in results:
    print results

if __name__ == '__main__':
  popular_articles()
  popular_authors()
  max_errors()