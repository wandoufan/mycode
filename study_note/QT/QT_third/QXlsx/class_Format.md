# Format

## 基本功能
设置单元格的格式
注意：设置完单元格的格式之后，单元格宽度会很变的窄，除非手动设置
原因？？？
```
#include "xlsxformat.h"
```


##构造函数
1. Format ()

2. Format (const Format &other)


## 设置单元格边框样式
1. void setBorderColor (const QColor &color)

2. void setBorderStyle (BorderStyle style)

3. void setBorderIndex (int index)


## 设置单元格字体样式
1. void setFont (const QFont &font)

2. void setFontSize (int size)

3. void setFontItalic (bool italic)
设置斜体

4. void setFontStrikeOut (bool)
设置删除线

5. void setFontColor (const QColor &)

6. void setFontBold (bool bold)
设置粗体

7. void setFontUnderline (FontUnderline)

8. void setFontName (const QString &)
设置单元格的名字
备注：单元格默认名为"Calibri"

9. void setFontOutline (bool outline)
没测试出有什么作用

10. void setFontScript (FontScript)
没测试出有什么作用


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
