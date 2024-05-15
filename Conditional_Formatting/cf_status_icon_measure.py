Status Icon Measure = 
VAR _ProjectProgress = MAX('Project Status'[Status %])
VAR _ProjectTarget = MAX('Project Status'[Target %])
VAR _CF =
    SWITCH(
        TRUE(),
        _ProjectProgress >= 75 && _ProjectProgress >=_ProjectTarget, [Icon_Status_Good_75],
        _ProjectProgress >= 50 && _ProjectProgress >=_ProjectTarget, [Icon_Status_Good_50],
        _ProjectProgress >= 25 && _ProjectProgress >=_ProjectTarget, [Icon_Status_Good_25],
        _ProjectProgress >=  0 && _ProjectProgress >=_ProjectTarget, [Icon_Status_Good_0],
        _ProjectProgress >= 75 && _ProjectProgress < _ProjectTarget, [Icon_Status_Bad_75],
        _ProjectProgress >= 50 && _ProjectProgress < _ProjectTarget, [Icon_Status_Bad_50],
        _ProjectProgress >= 25 && _ProjectProgress < _ProjectTarget, [Icon_Status_Bad_25],
        _ProjectProgress >=  0 && _ProjectProgress < _ProjectTarget, [Icon_Status_Bad_0]
    )
RETURN
    _CF
