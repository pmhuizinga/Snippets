-- LAG function: get the previous value in the current record
select	column1
  	,column2
	,lag(column3,1) over (order by column1, columns2) as PreviousValue
From	table

-- ISNULL function: in case of null replace with alternative value
select	ISNULL(column, alternative column)
From	table

-- COALESCE function: Return the first non-null value in a list
select	ISNULL(column1, column2, column3)
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
