-- create as variable (instead of a temporary table)

DECLARE @tablename table
	(
	column1 nVARCHAR(20)
	,column2 DATETIME
	,column3 INT
	,column4 decimal(38,18)
	)
INSERT INTO @tablename
SELECT	column1
		,column2
		,column3
		,column4
