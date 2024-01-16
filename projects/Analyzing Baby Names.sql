postgresql:///names


/*
  Find names that have been given to over 5,000 babies of either sex every year for the 101 years from 1920 through 2020; recall that names only show up in our dataset when at least 5,000 babies have been given that name in a year.
*/
SELECT first_name, SUM(num) AS sum
FROM baby_names
GROUP BY first_name
HAVING count(year) = 101
ORDER BY SUM(num) DESC;


/*
  Classify each name's popularity according to the number of years that the name appears in the dataset.
*/

SELECT first_name, SUM(num),
CASE 
WHEN COUNT(*) > 80 THEN 'Classic' 
WHEN COUNT(*) > 50 THEN 'Semi - classic' 
WHEN COUNT(*) > 20 THEN 'Semi - trendy'
ELSE 'Trendy'
END AS popularity_type
FROM baby_names
GROUP BY first_name
ORDER BY first_name ASC;

/*
  Let's take a look at the ten highest-ranked American female names in our dataset.
*/

SELECT
    RANK() OVER (ORDER BY sum(num) DESC) AS name_rank,
    first_name, 
    SUM(num)
FROM baby_names
WHERE sex = 'F'
GROUP BY first_name
LIMIT 10;

/*
 Return a list of first names which meet this friend's baby name criteria.
*/
SELECT first_name
FROM baby_names
WHERE sex = 'F' AND 
      year > 2015 AND 
      first_name LIKE '%a'
GROUP BY first_name
ORDER BY sum(num) DESC;

/*
 Find the cumulative number of babies named Olivia over the years since the name first appeared in our dataset.
*/
SELECT first_name, year, num,
       SUM(num) OVER (ORDER BY year) AS cumulative_olivias
FROM baby_names
WHERE first_name LIKE 'Olivia'
ORDER BY year ASC;

/*
Write a query that selects the year and the maximum num of babies given any male name in that year.
*/
SELECT year, MAX(num) AS max_num
FROM baby_names
WHERE sex = 'M'
GROUP BY year;
/*
Using the previous task's code as a subquery, look up the first_name that corresponds to the maximum number of babies given a specific male name in a year.
*/
SELECT b1.year, b1.first_name, b1.num
FROM baby_names b1
INNER JOIN (
    SELECT year, MAX(num) AS max_num
    FROM baby_names
    WHERE sex = 'M'
    GROUP BY year) AS b2
ON b1.year = b2.year AND b1.num = b2.max_num
WHERE b1.sex = 'M'
ORDER BY year DESC;
/*
Return a list of first names that have been the top male first name in any year along with a count of the number of years that name has been the top name.
*/

WITH top_male_names AS (  
SELECT b1.year, b1.first_name, b1.num
FROM baby_names b1
INNER JOIN (
    SELECT year, MAX(num) AS max_num
    FROM baby_names
    WHERE sex = 'M'
    GROUP BY year) AS b2
ON b1.year = b2.year AND b1.num = b2.max_num
WHERE b1.sex = 'M'
ORDER BY year DESC
)

SELECT first_name, COUNT(first_name) AS count_top_name
FROM top_male_names
GROUP BY first_name
ORDER BY COUNT(first_name) DESC;
