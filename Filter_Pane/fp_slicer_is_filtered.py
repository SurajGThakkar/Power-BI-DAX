Slicer is Filtered = 
SWITCH(
    TRUE,
    ISFILTERED(Churn_Modelling[Geography]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Geography", 1,
    ISFILTERED(Churn_Modelling[Gender]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Gender", 1,
    ISFILTERED(Churn_Modelling[Age Group]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Age Group", 1,
    ISFILTERED(Churn_Modelling[Tenure Group]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Tenure", 1,
    ISFILTERED(Churn_Modelling[Credit Score Cluster]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Credit Score", 1,
    ISFILTERED(Churn_Modelling[Salary Range]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Salary Range", 1,
    ISFILTERED(Churn_Modelling[HasCrCard Label]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Credit Card Holders", 1,
    ISFILTERED(Churn_Modelling[IsActiveMember Label]) &&
    SELECTEDVALUE('Slicer Table'[Slicer]) = "Active Members", 1,
    0  // Default value if none of the conditions match
)
