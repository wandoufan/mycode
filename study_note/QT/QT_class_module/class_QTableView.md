# QTableView

## 基本功能
QTableView提供一个基于Model/View(模型/视图)架构的二维数据表格  
具体可以参见QT_Model_View.md  
```
QWidget - QFrame - QAbstractScrollArea - QAbstractItemView - | - QTableView - QTableWidget 
															 | - QTreeView
															 | - QListView
															 | - QHeaderView
															 | - QColumnView
```


## 代码示例
```
QTableView *table_view;
table_view = new QTableView(this);
table_view -> setModel(model);
table_view -> setFixedSize(500, 600);
table_view -> setSelectionBehavior(QAbstractItemView::SelectRows);
table_view -> setSelectionMode(QAbstractItemView::ExtendedSelection);
table_view -> setEditTriggers(QAbstractItemView::NoEditTriggers);
table_view -> verticalHeader()->setVisible(false);
table_view -> horizontalHeader()->setVisible(true);
table_view -> horizontalHeader()->setDefaultSectionSize(50);
table_view -> horizontalHeader()->setSectionResizeMode(QHeaderView::Fixed);
table_view -> horizontalHeader()->setStretchLastSection(true);
table_view -> horizontalHeader()->resizeSection(1, 200);
table_view -> horizontalHeader()->resizeSection(2, 150);
table_view -> horizontalHeader()->resizeSection(3, 120);
table_view -> horizontalHeader()->resizeSection(4, 200);
table_view -> horizontalHeader()->setHighlightSections(false);
table_view -> show();
```


## 构造函数
1. QTableView::QTableView(QWidget \*parent = nullptr)


## 常用公共函数：读取/设置行高和列宽
备注：这里的宽高仅指工作区，表头行/表头列的宽高
1. int QTableView::columnWidth(int column) const

2. int QTableView::rowHeight(int row) const

3. void QTableView::setColumnWidth(int column, int width)

3. void QTableView::setRowHeight(int row, int height)


## 常用公共函数：读取/设置表头行和表头列
备注：表头是一个单独的QHeaderView对象
1. QHeaderView \*QTableView::horizontalHeader() const

2. QHeaderView \*QTableView::verticalHeader() const
 
3. void QTableView::setHorizontalHeader(QHeaderView \*header)

4. void QTableView::setVerticalHeader(QHeaderView \*header)


## 常用公共函数：读取/设置行和列隐藏
1. bool QTableView::isRowHidden(int row) const

2. bool QTableView::isColumnHidden(int column) const

3. void QTableView::setRowHidden(int row, bool hide)

4. void QTableView::setColumnHidden(int column, bool hide)


## 常用公共函数：读取/设置表格的网格线
1. bool QTableView::showGrid() const
备注：网格线显示属性的默认值是true

2. void QTableView::setShowGrid(bool show)

3. Qt::PenStyle QTableView::gridStyle() const

4. void QTableView::setGridStyle(Qt::PenStyle style)


## 常用公共函数：设置数据排序
1. bool QTableView::isSortingEnabled() const
备注：排序属性的默认值是false

2. void QTableView::setSortingEnabled(bool enable)
把排序属性设置为true之后就会立即触发调用sortByColum()函数

3. void QTableView::sortByColumn(int column, Qt::SortOrder order)


## 常用公共函数：设置自动换行
1. bool QTableView::wordWrap() const
备注：自动换行属性的默认值是true

2. void QTableView::setWordWrap(bool on)


## 槽函数：隐藏/显示行和列
1. [slot] void QTableView::hideRow(int row)

2. [slot] void QTableView::hideColumn(int column)

3. [slot] void QTableView::showRow(int row)

4. [slot] void QTableView::showColumn(int column)


## 槽函数：根据表格内容自动调整行高和列宽
1. [slot] void QTableView::resizeColumnToContents(int column)

2. [slot] void QTableView::resizeColumnsToContents()

3. [slot] void QTableView::resizeRowToContents(int row)

4. [slot] void QTableView::resizeRowsToContents()


## 槽函数：选中指定行和列
备注：需要SelectionMode 和 SelectionBehavior属性允许行/列被选中
1. [slot] void QTableView::selectRow(int row)

2. [slot] void QTableView::selectColumn(int column)




