SELECT COUNT(*) FROM flights WHERE destination='New York';
SELECT AVG(duration) FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%';
