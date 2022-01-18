# CellRange

## 基本功能
表示表格中一个单元格范围，比如"A1:C3"，"A1:A9"  
也可以是一个单独的单元格，比如"A1"、"B3"  
```
#include "xlsxcellrange.h"
```


## 构造函数
1. CellRange ()

2. CellRange (int firstRow, int firstColumn, int lastRow, int lastColumn)
```
CellRange cellrange = CellRange(1, 6, 10, 20);
```

3. CellRange (const CellReference &topLeft, const CellReference &bottomRight)

4. CellRange (const QString &range)
```
CellRange cellrange = CellRange("A1:C3");
```

5. CellRange (const char \*range)

6. CellRange (const CellRange &other)