# QPoint

## 基本功能
QPoint使用整型精度在平面上定义了一个位置  


## 构造函数
1. QPoint::QPoint()
创建一个空的位置，坐标为(0, 0)  
2. QPoint::QPoint(int xpos, int ypos)
使用给定的坐标创建一个位置  


## 常用公共函数
1. void QPoint::setX(int x)

2. void QPoint::setY(int y)

3. int QPoint::x() const

4. int QPoint::y() const

5. int &QPoint::rx()
返回的是指向x坐标的指针，因此可以进行自加和自减操作  
```
p.rx() ++;
```

6. int &QPoint::ry()
