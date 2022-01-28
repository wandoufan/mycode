# Format

## 基本功能
设置单元格的格式以及单元格中的字体格式  
注意：设置完单元格的格式之后，单元格宽度会很变的窄，除非手动设置，原因未知
```
#include "xlsxformat.h"
```
备注：所有的函数接口详见源代码  


##构造函数
1. Format ()

2. Format (const Format &other)


## 设置单元格边框样式
1. void setBorderStyle (BorderStyle style)

2. void setLeftBorderStyle(BorderStyle style)

3. void setRightBorderStyle(BorderStyle style)

4. void setTopBorderStyle(BorderStyle style)

5. void setBottomBorderStyle(BorderStyle style)

6. void setDiagonalBorderStyle(BorderStyle style);

7. void setDiagonalBorderType(DiagonalBorderType style);
设置单元格斜对角线类型  


## 设置单元格边框颜色
1. void setBorderColor (const QColor &color)

2. void setLeftBorderColor(const QColor &color)

3. void setRightBorderColor(const QColor &color)

4. void setTopBorderColor(const QColor &color)

5. void setBottomBorderColor(const QColor &color)

6. void setDiagonalBorderColor(const QColor &color);


## 设置单元格字体样式
1. void setFont (const QFont &font)
用QFont设置整个字体

2. void setFontSize (int size)
设置大小

3. void setFontItalic (bool italic)
设置斜体

4. void setFontStrikeOut (bool)
设置删除线

5. void setFontColor (const QColor &)
设置颜色

6. void setFontBold (bool bold)
设置粗体

7. void setFontUnderline (FontUnderline)
设置下划线

8. void setFontStrikeOut(bool);
设置删除线

9. void setFontName (const QString &)
设置字体
备注：单元格默认名为"Calibri"

10. void setTextWarp(bool textWrap);
设置自动换行

11. void setRotation(int rotation);
设置旋转转向

12. void setIndent(int indent);
设置缩进

13. void setShrinkToFit(bool shink);
设置自动缩小适应

14. void setFontOutline (bool outline)
没测试出有什么作用，设置后没有任何变化

15. void setFontScript (FontScript)
没测试出有什么作用，设置后没有任何变化


## 设置单元格背景颜色
1. void setPatternForegroundColor (const QColor &color)

2. void setPatternBackgroundColor (const QColor &color)


## 设置单元格居中方式
1. void setHorizontalAlignment (HorizontalAlignment align)

2. void setVerticalAlignment (VerticalAlignment align)


## enum FontUnderline
集合中包括所有下划线样式
{
FontUnderlineNone, FontUnderlineSingle, FontUnderlineDouble, FontUnderlineSingleAccounting, 
FontUnderlineDoubleAccounting
}


## enum HorizontalAlignment
集合中包含所有单元格水平居中的样式
{
AlignHGeneral, AlignLeft, AlignHCenter, AlignRight, 
AlignHFill, AlignHJustify, AlignHMerge, AlignHDistributed
}


## enum VerticalAlignment
集合中包含所有单元格垂直居中的样式
{
AlignTop, AlignVCenter, AlignBottom, AlignVJustify, 
AlignVDistributed
}


## enum BorderStyle
集合中包括所有单元格边框样式
{
BorderNone, BorderThin, BorderMedium, BorderDashed, 
BorderDotted, BorderThick, BorderDouble, BorderHair, 
BorderMediumDashed, BorderDashDot, BorderMediumDashDot, BorderDashDotDot, 
BorderMediumDashDotDot, BorderSlantDashDot
}


## enum DiagonalBorderType
集合中包括所有对角线单元格边框样式
{
DiagonalBorderNone, DiagonalBorderDown, DiagonalBorderUp, DiagnoalBorderBoth
}


## enum FillPattern
{
PatternNone, PatternSolid, PatternMediumGray, PatternDarkGray, 
PatternLightGray, PatternDarkHorizontal, PatternDarkVertical, PatternDarkDown, 
PatternDarkUp, PatternDarkGrid, PatternDarkTrellis, PatternLightHorizontal, 
PatternLightVertical, PatternLightDown, PatternLightUp, PatternLightTrellis, 
PatternGray125, PatternGray0625, PatternLightGrid
}


## enum FontScript
没测试出有什么作用
{FontScriptNormal, FontScriptSuper, FontScriptSub}
