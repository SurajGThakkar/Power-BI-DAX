Count Active Filters Tooltip = 
VAR geography = IF(ISFILTERED(Churn_Modelling[Geography]),"Geography",BLANK())
VAR gender = IF(ISFILTERED(Churn_Modelling[gender]),"Gender",BLANK())
VAR age_group = IF(ISFILTERED(Churn_Modelling[age group]),"Age Group",BLANK())
VAR tenure_group = IF(ISFILTERED(Churn_Modelling[tenure group]),"Tenure",BLANK())
VAR credit_score_cluster = IF(ISFILTERED(Churn_Modelling[credit score cluster]),"Credit Score",BLANK())
VAR salary_range = IF(ISFILTERED(Churn_Modelling[salary range]),"Salary Range",BLANK())
VAR hascrcard = IF(ISFILTERED(Churn_Modelling[hascrcard label]),"Credit Card Owners",BLANK())
VAR isactivemember = IF(ISFILTERED(Churn_Modelling[IsActiveMember label]),"Active Members",BLANK())


VAR filter_list=
{geography,  gender, age_group, tenure_group, credit_score_cluster, salary_range, hascrcard, isactivemember}

VAR filter_table=
FILTER(filter_list,[Value]<>BLANK())

VAR filter_label_show =
CONCATENATEX(filter_table,[Value],", ")

RETURN
"Active Filters: " & IF(filter_label_show<>BLANK(),filter_label_show,"None")
