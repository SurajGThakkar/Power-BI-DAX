Running Total = 
VAR MaxDate = MAX(DimDate[Date])
RETURN 
CALCULATE(
    SELECTEDMEASURE(),
    FILTER(
        ALL(DimDate),
        DimDate[Date] <= MaxDate
        )
    )
