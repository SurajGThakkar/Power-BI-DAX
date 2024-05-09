Rolling 12 Month = 
CALCULATE(
    SELECTEDMEASURE(),
    DATESINPERIOD(DimDate[Date], MAX(DimDate[Date]), -12, MONTH)
    )
