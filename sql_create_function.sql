USE Markit_EDM_DEV_v95
go

drop function dbo.fn_Test
go

CREATE FUNCTION dbo.fn_Test
	(
	@SingleDate date
	)
	RETURNS @TESTPAUL TABLE 
		(
		col1 bigint
		,col2 nvarchar(50)
		,col3 datetime
		,col4 decimal(38, 18)
		)
	AS
	BEGIN

		--INSERT INTO @TEST
		DECLARE @TEST2 TABLE
			(
			col1 bigint
			,col2 nvarchar(50)
			,col3 datetime
			,col4 decimal(38, 18)
			)
		INSERT INTO @TEST2
		SELECT	col1
				,col2
				,col3
				,col4
		FROM	<table_name>
		WHERE	AS_OF_DATE = @SingleDate
	
		INSERT INTO @TEST
		SELECT * FROM @TEST2

		RETURN

	END
	GO

SELECT * FROM dbo.fn_Test('2019-03-28') WHERE col1 = '<variable>'
