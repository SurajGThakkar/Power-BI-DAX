### 1. Create a New Table: Bin Start
This table generates a series from 0 to 1000 with a step of 25.
```DAX
Bin Start = GENERATESERIES(0, 1000, 25)
```

### 2. Measure: Bins Filter
This measure filters the bins based on the selected bin size.
```DAX
Bins Filter =
VAR _BinSize = BinSize[BinSize Value]
VAR _BinsToKeep = 
    SELECTEDVALUE('Bin Start'[Bin Start]) / _BinSize = 
    ROUND(SELECTEDVALUE('Bin Start'[Bin Start]) / _BinSize, 0)
VAR BinFilter = 
    IF(_BinsToKeep, 1, 0)
RETURN
    BinFilter
```

### 3. Measure: Custom Label
This measure creates custom labels for the bins.
```DAX
Custom Label =
VAR _BinSize_Min = MIN('Bin Start'[Bin Start])
VAR _BinSize_Max = _BinSize_Min + [BinSize Value] - 1
RETURN
    _BinSize_Min & "-" & _BinSize_Max
```

### 4. Measure: Nr of Products
This measure calculates the number of products within each bin range.
```DAX
Nr of Products =
VAR _BinSize_Min = MIN('Bin Start'[Bin Start])
VAR _BinSize_Max = _BinSize_Min + [BinSize Value] - 1
VAR _SalesNr = 
    SUMX(
        ALLSELECTED(dimProduct[ProductName]),
        IF(
            [Nr of Sales Orders] >= _BinSize_Min &&
            [Nr of Sales Orders] < _BinSize_Max,
            1
        )
    )
RETURN
    _SalesNr
```

### 5. New Table: BinSize
This table generates a series for bin sizes from 25 to 100 with a step of 25.
```DAX
BinSize = GENERATESERIES(25, 100, 25)
```

### 6. Measure: BinSize Value
This measure selects the bin size value or defaults to 50 if none is selected.
```DAX
BinSize Value = SELECTEDVALUE('BinSize'[BinSize], 50)
```

### 7. Measure: Nr of Sales Orders
This measure counts the number of sales orders.
```DAX
Nr of Sales Orders = COUNTROWS(fctSales)
```
