SELECT 
sub2.*,
CASE 
WHEN sub2.height NOT BETWEEN sub2.lcl AND sub2.ucl
THEN TRUE
ELSE FALSE
END AS alert

FROM
(SELECT sub1.*,
sub1.avg_height + 3*stddev_height/SQRT(5) AS ucl,
sub1.avg_height - 3*stddev_height/SQRT(5) AS lcl
 
FROM 
(SELECT operator,
 		 ROW_NUMBER() OVER w ,
 		 height,
 		 AVG(height) OVER w AS avg_height,
 		 STDDEV(height) OVER w AS stddev_height 
 
FROM manufacturing_parts
WINDOW w AS (
			PARTITION BY operator
			ORDER BY item_no
			ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
)
) as sub1

WHERE sub1.row_number >= 5
) as sub2
