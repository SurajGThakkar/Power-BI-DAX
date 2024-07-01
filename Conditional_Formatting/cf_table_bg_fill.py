CF = 
VAR SummaryTable = 
    CALCULATETABLE(
        ADDCOLUMNS(
            SUMMARIZE(
                fctSales,
                dimStore[StoreName],
                dimDate[Year],
                dimDate[Quarter]
            ),
            "Sales", [Total Sales]
        ),
        ALLSELECTED(dimDate)
    )
VAR MaxValue =
    MAXX(
        SummaryTable,
        [Sales]
    )
VAR MinValue =
    MINX(
        SummaryTable,
        [Sales]
    )
VAR Range = MaxValue - MinValue
VAR Hue = 
    ROUND(
        DIVIDE(
            [Total Sales] - MinValue,
            Range
        ) * 120, 0) + 240
VAR Colour = "hsla(" & Hue & ", " & "100%" & ", " & "90%" & ", " & 1 & ")"
RETURN
    Colour
