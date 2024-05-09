YoY% = 
VAR LastYear = 
CALCULATE(
    SELECTEDMEASURE(),
    DATEADD(DimDate[Date], -1, YEAR)
    )
RETURN 
DIVIDE(SELECTEDMEASURE() - LastYear, LastYear, 0)
