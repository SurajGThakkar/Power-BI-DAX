Count Active Filters = 
VAR geography = IF(ISFILTERED(Churn_Modelling[Geography]),1,0)
VAR gender = IF(ISFILTERED(Churn_Modelling[gender]),1,0)
VAR age_group = IF(ISFILTERED(Churn_Modelling[age group]),1,0)
VAR tenure_group = IF(ISFILTERED(Churn_Modelling[tenure group]),1,0)
VAR credit_score_cluster = IF(ISFILTERED(Churn_Modelling[credit score cluster]),1,0)
VAR salary_range = IF(ISFILTERED(Churn_Modelling[salary range]),1,0)
VAR hascrcard = IF(ISFILTERED(Churn_Modelling[HasCrCard Label]),1,0)
VAR isactivemember = IF(ISFILTERED(Churn_Modelling[IsActiveMember Label]),1,0)

VAR filter_count=
geography+gender+age_group+tenure_group+credit_score_cluster+salary_range+hascrcard+isactivemember

RETURN
filter_count&""
