[Modified] Active Slicer Labels = 
VAR slicer_filtered = [Slicer is Filtered]

VAR slicer_label = 
    SWITCH(
        SELECTEDVALUE('Slicer Table'[Slicer]),
        "Geography", [Geography Label],
        "Gender", [Gender Label],
        "Age Group", [Age Group Label],
        "Tenure", [Tenure Group Label],
        "Credit Score", [Credit Score Label],
        "Salary Range", [Salary Range Label],
        "Credit Card Holders", [Credit Card Holders Label],
        "Active Members", [Active Members Label]
    )

VAR show_slicer_label = 
IF(slicer_filtered = 1, slicer_label)

RETURN show_slicer_label
