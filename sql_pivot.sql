-- pivot
SELECT
  [non-pivoted column], -- optional
  [additional non-pivoted columns], -- optional
  [first pivoted column],
  [additional pivoted columns]
FROM (
  SELECT query producing sql data for pivot
  -- select pivot columns as dimensions and
  -- value columns as measures from sql tables
) AS TableAlias
PIVOT
(
  <aggregation function>(column for aggregation or measure column) -- MIN,MAX,SUM,etc
  FOR [<column name containing values for pivot table columns>]
  IN (
    [first pivoted column], ..., [last pivoted column]
  )
) AS PivotTableAlias
ORDER BY clause -- optional


-- unpivot
select B.COLUMN1, B.COLUMN2, b.COLUMN3
from <table_name>
unpivot
(
  VALUE
  for TYPE in (COLUMNA,
        COLUMNB,
        COLUMNC)
) B
where B.COLUMNX = '2019-03-31'






