MaxMin = 
VAR Sales = [Total Sales]

VAR MaxSalesOverall = 
    MAXX(
        ALLSELECTED(dimDate[Year], dimDate[Quarter], dimDate[QuarterNo]),
        CALCULATE([Total Sales])
    )

VAR MinSalesOverall = 
    MINX(
        ALLSELECTED(dimDate[Year], dimDate[Quarter], dimDate[QuarterNo]),
        CALCULATE([Total Sales])
    )

VAR Result = 
    SWITCH(
        TRUE,
        Sales = MaxSalesOverall, "#22957e",  // Color code for max sales
        Sales = MinSalesOverall, "#ff908c",  // Color code for min sales
        "#7b8cfe"  // Default color code
    )

RETURN
Result
