Status Icon Measure CF Rule = 
VAR _ProjectProgress = MAX('Project Status'[Status %])
VAR _ProjectTarget = MAX('Project Status'[Target %])
VAR _CF =
    SWITCH(
        TRUE(),
        _ProjectProgress >= 75 && _ProjectProgress >=_ProjectTarget, 8,
        _ProjectProgress >= 50 && _ProjectProgress >=_ProjectTarget, 7,
        _ProjectProgress >= 25 && _ProjectProgress >=_ProjectTarget, 6,
        _ProjectProgress >=  0 && _ProjectProgress >=_ProjectTarget, 5,
        _ProjectProgress >= 75 && _ProjectProgress < _ProjectTarget, 4,
        _ProjectProgress >= 50 && _ProjectProgress < _ProjectTarget, 3,
        _ProjectProgress >= 25 && _ProjectProgress < _ProjectTarget, 2,
        _ProjectProgress >=  0 && _ProjectProgress < _ProjectTarget, 1
    )
RETURN
    _CF
