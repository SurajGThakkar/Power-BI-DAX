Status Icon Column = 
SWITCH(
    TRUE(),
    [Status %]>=75 && [Status %]>=[Target %], [Icon_Status_Good_75],
    [Status %]>=50 && [Status %]>=[Target %], [Icon_Status_Good_50],
    [Status %]>=25 && [Status %]>=[Target %], [Icon_Status_Good_25],
    [Status %]>=0  && [Status %]>=[Target %], [Icon_Status_Good_0],
    [Status %]>=75 && [Status %]< [Target %], [Icon_Status_Bad_75],
    [Status %]>=50 && [Status %]< [Target %], [Icon_Status_Bad_50],
    [Status %]>=25 && [Status %]< [Target %], [Icon_Status_Bad_25],
    [Status %]>=0  && [Status %]< [Target %], [Icon_Status_Bad_0]
)
