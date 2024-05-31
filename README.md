# Power-BI

Welcome to the **Power-BI** repository! This project contains all the DAX functions you need to create comprehensive Power BI dashboards. It is an ongoing project and will receive regular updates to add more DAX functions and refine existing ones.

## Description

The **Power-BI** repository is designed to help developers build effective and scalable Power BI dashboards using DAX functions. While the repository aims to be as scalable as possible, certain elements such as table names and columns might require modification. As a guide, we've included example table names and columns to assist in this customization process.

## Features

- **Comprehensive DAX Functions**: Access a variety of DAX functions for different purposes.
- **Regular Updates**: New DAX functions and enhancements are regularly added.
- **Customizable Examples**: Easily modify table names and columns using the provided examples.

```markdown
## Detailed Breakdown of Measures

### `[cf_transparent]`
```DAX
MEASURE '[01] Measures'[cf_transparent] = "#FFFFFF00"
```
- Returns the color code for transparent white.

### `[Count Active Filters]`
```DAX
MEASURE '[01] Measures'[Count Active Filters] = 
VAR geography = IF(ISFILTERED(Churn_Modelling[Geography]), 1, 0)
VAR gender = IF(ISFILTERED(Churn_Modelling[gender]), 1, 0)
VAR age_group = IF(ISFILTERED(Churn_Modelling[age group]), 1, 0)
VAR tenure_group = IF(ISFILTERED(Churn_Modelling[tenure group]), 1, 0)
VAR credit_score_cluster = IF(ISFILTERED(Churn_Modelling[credit score cluster]), 1, 0)
VAR salary_range = IF(ISFILTERED(Churn_Modelling[salary range]), 1, 0)
VAR hascrcard = IF(ISFILTERED(Churn_Modelling[HasCrCard Label]), 1, 0)
VAR isactivemember = IF(ISFILTERED(Churn_Modelling[IsActiveMember Label]), 1, 0)

VAR filter_count = geography + gender + age_group + tenure_group + credit_score_cluster + salary_range + hascrcard + isactivemember

RETURN filter_count & ""
```
- Calculates the number of active filters applied across various columns in the `Churn_Modelling` table.

### `[Count Active Filters Button Color]`
```DAX
MEASURE '[01] Measures'[Count Active Filters Button Color] = 
IF([Count Active Filters] = "0", "#CDC4BA30", "#CDC4BA")
```
- Sets the button color based on the presence of active filters.

### `[Count Active Filters Counter Color]`
```DAX
MEASURE '[01] Measures'[Count Active Filters Counter Color] = 
IF([Count Active Filters] = "0", "#CDC4BA30", "#3D3D3D")
```
- Sets the counter color based on the presence of active filters.

### `[Count Active Filters Tooltip]`
```DAX
MEASURE '[01] Measures'[Count Active Filters Tooltip] = 
VAR geography = IF(ISFILTERED(Churn_Modelling[Geography]), "Geography", BLANK())
VAR gender = IF(ISFILTERED(Churn_Modelling[gender]), "Gender", BLANK())
VAR age_group = IF(ISFILTERED(Churn_Modelling[age group]), "Age Group", BLANK())
VAR tenure_group = IF(ISFILTERED(Churn_Modelling[tenure group]), "Tenure", BLANK())
VAR credit_score_cluster = IF(ISFILTERED(Churn_Modelling[credit score cluster]), "Credit Score", BLANK())
VAR salary_range = IF(ISFILTERED(Churn_Modelling[salary range]), "Salary Range", BLANK())
VAR hascrcard = IF(ISFILTERED(Churn_Modelling[hascrcard label]), "Credit Card Owners", BLANK())
VAR isactivemember = IF(ISFILTERED(Churn_Modelling[IsActiveMember label]), "Active Members", BLANK())

VAR filter_list = {geography, gender, age_group, tenure_group, credit_score_cluster, salary_range, hascrcard, isactivemember}

VAR filter_table = FILTER(filter_list, [Value] <> BLANK())

VAR filter_label_show = CONCATENATEX(filter_table, [Value], ", ")

RETURN "Active Filters: " & IF(filter_label_show <> BLANK(), filter_label_show, "None")
```
- Constructs a tooltip that lists all active filters.

### `[Active Slicer Labels]`
```DAX
MEASURE '[01] Measures'[Active Slicer Labels] = 
VAR slicer_filtered = [Slicer is Filtered]

VAR slicer_label = SWITCH(
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

VAR show_slicer_label = IF(slicer_filtered = 1, slicer_label)

RETURN show_slicer_label
```
- Determines and displays the label for active slicers.

### Label Measures (e.g., `[Active Members Label]`, `[Age Group Label]`, etc.)
```DAX
MEASURE '[01] Measures'[Active Members Label] = 
VAR __DISTINCT_VALUES_COUNT = DISTINCTCOUNT('Churn_Modelling'[IsActiveMember Label])
VAR __MAX_VALUES_TO_SHOW = 2

RETURN IF(
    __DISTINCT_VALUES_COUNT > __MAX_VALUES_TO_SHOW,
    CONCATENATE(
        CONCATENATEX(
            TOPN(
                __MAX_VALUES_TO_SHOW,
                VALUES('Churn_Modelling'[IsActiveMember Label]),
                'Churn_Modelling'[IsActiveMember Label],
                ASC
            ),
            'Churn_Modelling'[IsActiveMember Label],
            ", ",
            'Churn_Modelling'[IsActiveMember Label],
            ASC
        ),
        ", etc."
    ),
    CONCATENATEX(
        VALUES('Churn_Modelling'[IsActiveMember Label]),
        'Churn_Modelling'[IsActiveMember Label],
        ", ",
        'Churn_Modelling'[IsActiveMember Label],
        ASC
    )
)
```
- These measures generate labels for different fields, showing "etc." if there are more than two distinct values.

### `[Salary Range Label (Complex)]`
```DAX
MEASURE '[01] Measures'[Salary Range Label (Complex)] = 
VAR _max_value = MAX(Churn_Modelling[Salary Range Sort])
VAR _min_value = MIN(Churn_Modelling[Salary Range Sort])

VAR _table_with_gap = SUMMARIZE(Churn_Modelling, Churn_Modelling[Salary Range])

VAR _table_no_gap = CALCULATETABLE(
    SUMMARIZE(Churn_Modelling, Churn_Modelling[Salary Range]),
    FILTER(ALL(Churn_Modelling), 
        Churn_Modelling[Salary Range Sort] >= _min_value && 
        Churn_Modelling[Salary Range Sort] <= _max_value
    )
)

VAR _gaps = EXCEPT(_table_no_gap, _table_with_gap)

VAR _continuous = [Salary Range Label (Continuous)]

VAR _distinct = [Salary Range Label]

VAR _label = SWITCH(TRUE,
    COUNTROWS(_table_with_gap) = 1, _distinct,
    COUNTX(_gaps, Churn_Modelling[Salary Range]) <> 0, _distinct,
    COUNTX(_gaps, Churn_Modelling[Salary Range]) = 0, _continuous
)

RETURN _label
```
- Creates a label for the salary range, considering potential gaps in the salary range values.

### `[Salary Range Label (Continuous)]`
```DAX
MEASURE '[01] Measures'[Salary Range Label (Continuous)] = 
VAR _bottom_limit = IF(NOT MIN(Churn_Modelling[Salary Range Sort]) IN {1, 6},
    CALCULATE(VALUES(Churn_Modelling[Salary Range]),
        Churn_Modelling[Salary Range Sort] = MIN(Churn_Modelling[Salary Range Sort])
    ),
    "0-"
)
VAR _top_limit = IF(NOT MAX(Churn_Modelling[Salary Range Sort]) IN {1, 6},
    CALCULATE(VALUES(Churn_Modelling[Salary Range]),
        Churn_Modelling[Salary Range Sort] = MAX(Churn_Modelling[Salary Range Sort])
    ),
    "-200k+"
)

VAR _label = IF(
    ISFILTERED(Churn_Modelling[Salary Range])
    && _top_limit <> _bottom_limit,
    LEFT(_bottom_limit, SEARCH("-", _bottom_limit) - 1)
    & "-" &
    RIGHT(_top_limit, LEN(_top_limit) - SEARCH("-", _top_limit))
)

RETURN _label
```
- Returns a continuous salary range label based on the minimum and maximum salary range values.

### `[Churn]`
```DAX
MEASURE '[01] Measures'[Churn] = 
VAR exited_customers = CALCULATE(COUNTROWS(Churn_Modelling), Churn_Modelling[Exited] = 1)
VAR all_customers = COUNTROWS(Churn_Modelling)

RETURN DIVIDE(exited_customers, all_customers)
```
- Calculates the churn rate by dividing the number of exited customers by the total number of customers.

### `[Tooltip Cover Background]` and `[Tooltip Cover Text]`
```DAX
MEASURE '[01] Measures'[Tooltip Cover Background] = IF([Count Active Filters] = "0", "#3D3D3D", "#3D3D3D00")

MEASURE '[01] Measures'[Tooltip Cover Text] = IF([Count Active Filters] = "0", "No Active Filters")
```
- Controls the background color and text for a tooltip based on whether there are active filters.

### `[Slicer is Filtered]`
```DAX
MEASURE '[01] Measures'[Slicer is Filtered] = 
SWITCH (
    TRUE,
    ISFILTERED(Churn_Modelling[Geography])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Geography", 1,
    ISFILTERED(Churn_Modelling[Gender])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Gender",

 1,
    ISFILTERED(Churn_Modelling[Age Group])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Age Group", 1,
    ISFILTERED(Churn_Modelling[Tenure Group])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Tenure", 1,
    ISFILTERED(Churn_Modelling[Credit Score Cluster])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Credit Score", 1,
    ISFILTERED(Churn_Modelling[Salary Range])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Salary Range", 1,
    ISFILTERED(Churn_Modelling[HasCrCard Label])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Credit Card Holders", 1,
    ISFILTERED(Churn_Modelling[IsActiveMember Label])
        && SELECTEDVALUE('Slicer Table'[Slicer]) = "Active Members", 1
)
```
- Checks if specific columns are filtered and returns `1` if true, otherwise `0`.

## Contributing
If you have any suggestions or improvements, please feel free to submit a pull request or raise an issue. Contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore and utilize these measures to enhance your Power BI reports. For any questions or contributions, please raise an issue or submit a pull request.
```
