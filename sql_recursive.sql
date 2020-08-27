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
