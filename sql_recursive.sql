with recursive (col1, col2, col3, col4, col5) as 
(
select		col1
			    ,col2
			    ,col3
			    ,1
			    ,col4
from		  source_table

union all	

select	    result.col1
			      ,recursive.col2
			      ,result.col3
			      ,recursive.level + 1
			      ,result.col4
from		    recursive 
inner join	result 
			      on recursive.col3 = result.col2
)

select * from recursive

OF

WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, first_name, last_name, manager_id
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.first_name, e.last_name, e.manager_id
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy;
