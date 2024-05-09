//create a parameter named 'StartDate' with the required value
//Add this query in the Advanced Editor and press enter
let
    //Variables
    StartDate = StartDate,
    EndDate = DateTime.Date(DateTime.LocalNow()),
    Duration = Duration.Days(Duration.From(EndDate-StartDate))+1,
    Today = DateTime.Date(DateTime.LocalNow()),

    //Date Columns
    Dates = List.Dates(StartDate,Duration,#duration(1,0,0,0)),
    #"Converted to Table" = Table.FromList(Dates, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    #"Renamed Columns" = Table.RenameColumns(#"Converted to Table",{{"Column1", "Date"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Date", type date}}),
    #"Inserted Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
    #"Inserted QuarterNo" = Table.AddColumn(#"Inserted Year", "QuarterNo", each Date.QuarterOfYear([Date]), Int64.Type),
    #"Inserted Quarter" = Table.AddColumn(#"Inserted QuarterNo", "Quarter", each "Q"&Number.ToText([QuarterNo])),
    #"Inserted MonthNo" = Table.AddColumn(#"Inserted Quarter", "MonthNo", each Date.Month([Date]), Int64.Type),
    #"Inserted Month" = Table.AddColumn(#"Inserted MonthNo", "Month", each Text.Start(Date.MonthName([Date]),3), type text),
    #"Inserted DayNo" = Table.AddColumn(#"Inserted Month", "DayNo", each Date.DayOfWeek([Date], 1)+1, Int64.Type),
    #"Inserted Day Name" = Table.AddColumn(#"Inserted DayNo", "Day", each Text.Start(Date.DayOfWeekName([Date]),3), type text)
in
    #"Inserted Day Name"
