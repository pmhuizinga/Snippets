-- WINDOWS FUNCTIONS:
select 	row_number() over () rn,
       	rank() over () rnk,
       	dense_rank() over () dns_rnk,
       	lead(p.name) over () lead_name,
       	lag(p.name) over () lag_name, 		--get the previous value in the current record
       	first_value(p.name) over () fv_name,
       	last_value(p.name) over () lv_name,
       	ntile(4) over () quartile,
       	ntile(5) over () quintile
  from 	tabel

-- RANK
SELECT employee_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM employees;	

-- SUM
SELECT employee_id, salary,
       SUM(salary) OVER (ORDER BY employee_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS salary_sum
FROM employees;
  
-- ISNULL function: in case of null replace with alternative value
select	ISNULL(column, alternative column)
From	table

-- COALESCE function: Return the first non-null value in a list
select	COALESCE(column1, column2, column3)
From	table

-- OVER, PARTITION BY: for calculating running totals
select	sum(column1) over (partition by column2 order by column3) 
	,column2
	,column3
from	table

-- FILTER: 
select	column1
	,count(*) FILTER (WHERE column2 = ?) as column3
from	table

-- GROUPING SETS
SELECT department_id, job_id, SUM(salary) AS total_salary
FROM employees
GROUP BY GROUPING SETS ((department_id), (department_id, job_id));
