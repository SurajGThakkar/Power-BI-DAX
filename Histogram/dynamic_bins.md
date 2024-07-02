### 1. Create Table

#### Bin Start
This table generates a series from 0 to 1000 with a step of 25.
```DAX
Bin Start = GENERATESERIES(0, 1000, 25)
```
### 2. Create Parameter 

#### BinSize
Create a parameter named BinSize with the following values:
- What will your variable adjust? : Numeric range
- Name : BinSize
- Data type : WholeNumber
- min : 25
- max : 100
- increment : 25

**The above step should automatically create a Table called BinSize with the following column:**

```DAX
BinSize = GENERATESERIES(25, 100, 25)
```

### 3. Create Measures

#### BinSize Value
This measure selects the bin size value or defaults to 50 if none is selected.
```DAX
BinSize Value = SELECTEDVALUE('BinSize'[BinSize], 50)
```

#### Nr of Sales Orders
This measure counts the number of sales orders.
```DAX
Nr of Sales Orders = COUNTROWS(fctSales)
```

#### Bins Filter
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

#### Custom Label
This measure creates custom labels for the bins.
```DAX
Custom Label =
VAR _BinSize_Min = MIN('Bin Start'[Bin Start])
VAR _BinSize_Max = _BinSize_Min + [BinSize Value] - 1
RETURN
    _BinSize_Min & "-" & _BinSize_Max
```

#### Nr of Products
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
