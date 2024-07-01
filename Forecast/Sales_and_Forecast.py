Sales and Forecast =
VAR LastSalesDate = 
    CALCULATE(
        MAX(fctSales[TransactionDate]),
        REMOVEFILTERS()
    )

VAR Actuals = [Sales Actuals]

VAR FutureForecast =
    CALCULATE(
        [Sales Forecast],
        KEEPFILTERS(dimDate[Date] > LastSalesDate)
    )

VAR Result = FutureForecast + Actuals

RETURN
    Result
