import psycopg2;
db = psycopg2.connect(database='news')
c = db.cursor()
print("What are the most popular three articles of all time?")
c.execute("select a.title,count(*)as views from log as l,\
articles as a where l.path =concat('/article/',a.slug) \
Group by a.title order by count(*) desc limit 3;")
result = c.fetchall()
for result1 in result:
 print ('"{}" -- {} views'.format(result1[0], str(result1[1])))
 
print("Who are the most popular article authors of all time?")

c.execute("select t.name,count(*) as views  from log as l,\
articles as a,authors as t where l.path =concat('/article/',a.slug)and t.id=a.author \
Group by t.name order by count(*)desc limit 4;")
result2 = c.fetchall()
for result3 in result2:
 print ('"{}" -- {} views'.format(result3[0], str(result3[1])))
print("On which days did more than 1% of requests lead to errors?")

c.execute("WITH number_of_requests AS (SELECT time::date AS date, count(*)FROM log \
GROUP BY date ORDER BY date ), \
number_of_errors AS ( SELECT time::date AS date, count(*) \
FROM log WHERE status != '200 OK' GROUP BY date ORDER BY date )\
, error_of_rate AS \
( SELECT number_of_requests.date, \
Number_of_errors.count::float / number_of_requests.count::float * 100 AS error_per \
FROM number_of_requests, number_of_errors \
WHERE number_of_requests.date = number_of_errors.date )\
SELECT to_char(date,'Mon DD,YYYY')as date,round(cast(error_per as decimal), 2) \
as error_per FROM error_of_rate WHERE error_per > 1;")
result4 = c.fetchall()
for result5 in result4:
 print ('{} -- {}%'.format(result5[0], (result5[1])))
db.close()
