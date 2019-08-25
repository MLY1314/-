#4-10号台的吊筋为护筒顶-桩顶标高

import math
import string
import random
#from decimal import Decimal
#str01 = input(u'请输入分项工程名称：')
pier = int(input(u'请输入墩号：'))
#判断墩号是否准确
while pier not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,]:
    pier = int(input(u'请输入准确的墩号：'))
else:
    pole = int(input(u'请输入桩号：'))
#大范围判断桩号是否准确
while pole not in [1,2,3,4,5,6,7,8,9,10,11,12]:
    pole = int(input(u'请输入准确的桩号：'))
#else:
#输入的值为字符串
#pier = int(str02)
#pole = int(str03)
str04 = input(u'请输入设计桩顶标高：')
str05 = input(u'请输入设计孔底标高：')
str08 = input(u'请输入护筒标高：')
str07 = input(u'请输入实际孔底标高：')
str06 = input(u'请输入钢筋骨架低端高程偏差（单位：mm）：')
str09 = input(u'请输入沉淀厚度（单位：mm）：')
#字符串类型转换为浮点型
float04 = float(str04)
float05 = float(str05)
float06 = float(str06)
float07 = float(str07)
float08 = float(str08)
float09 = float(str09)
#浮点型取值保留三位数
stylist_pier_high = (round(float04,3))
stylist_pier_low = (round(float05,3))
reinforcement_bias = (round(float06,3))
practical_pier_low = (round(float07,3))
pile_casing_high = (round(float08,3))
sediment_ply = (round(float09,3))
#桩顶标高=设计标高-（2.5，2.0，1.8，1.6）
g = 2.0
h = 2.5
i = 1.8
j = 1.6
k = 3.0
if pier in [0]:
    practical_pier_high=stylist_pier_high - (round(g,1))
elif pier in [1,2,3,12,13]:
    practical_pier_high=stylist_pier_high - (round(j,1))
elif pier in [4,5,6,7,8,9,10]:
    practical_pier_high=stylist_pier_high - (round(h,1))
elif pier in [11]:
    practical_pier_high=stylist_pier_high - (round(i,1))
elif pier in [14]:
    if pole in [1,2]:
        practical_pier_high=stylist_pier_high
    elif pier in [3,4,5,6]:
        practical_pier_high=stylist_pier_high - (round(K,1))
#设计桩长
#有效桩长=桩顶标高-桩底标高
stylist_pile_length = stylist_pier_high - stylist_pier_low
#桩长大于设计桩长
#桩长=设计孔底标高-终孔孔底标高+有效桩长
pile_length = stylist_pier_low - practical_pier_low + (practical_pier_high - stylist_pier_low)
#应钻孔深
#应钻孔深=护筒顶-桩底标高
ought_hole_depht = pile_casing_high - stylist_pier_low
#吊筋长度
#吊筋长度=护筒标高-设计桩顶标高
l = 1.02
if pier in [0,1,2,3,11,12,13,14]:
    hanging_bar_length = pile_casing_high - practical_pier_high
elif pier in [4,5,6,7,8,9,10]:
    hanging_bar_length = pile_casing_high - practical_pier_high - (round(l,2))

#灌注前孔底标高=终孔孔底标高+沉淀厚度
a = (round(0.001,3))
pour_into_pier_low = practical_pier_low + (sediment_ply * a)
#钢筋笼底面标高=设计孔底标高+0.5+误差
b = (round(0.5,1))
c = (round(0.001,3))
reinforcement_pier_low = stylist_pier_low + b + (reinforcement_bias * c)
#应灌砼厚度=设计桩顶标高-灌注前孔底标高+（30-80）cm
e = int(random.randint(30,80))
print(e)
f = (round(0.01,2))
concrete_lenght = stylist_pier_high - pour_into_pier_low + (e * f)
#print(concrete_lenght)

#当第一次桩号输入错误的时候检查重新输入
#判断1，2，3，11，12，13号
if pier in [1,2,3,11,12,13]:
    while pole not in [1,2,3,4]:
        pole = int(input(u'请输入准确的桩号：'))
    else:
        if pole in [1,2]:
            print("左幅".center(26))
        elif pole in [3,4,5,6]:
            print("右副".center(26))

#判断14号
elif pier in [14]:
    while pole not in [1,2,3,4,5,6]:
        pole = int(input(u'请输入准确的桩号：'))
    else:
        if pole in [1,2]:
            print("左幅".center(26))
        elif pole in [3,4,5,6]:
            print("右副".center(26))

#判断4，5，6，7，8，9，10号
elif pier in [4,5,6,7,8,9,10]:
    while pole not in [1,2,3,4,5,6]:
        pole = int(input(u'请输入准确的桩号：'))
    else:
        if pole in [1,2,3,7,8,9]:
            print("左幅".center(26))
        elif pole in [4,5,6,10,11,12]:
            print("右副".center(26))

#判断0号
elif  pier in [0]:
    while pole not in [1,2,3,4,5,6]:
        pole = int(input(u'请输入准确的桩号：'))
    else:
        if pole in [1,2,5,6]:
            print("左幅".center(26))
        elif pole in [3,4,7,8]:
            print("右副".center(26))

message = f"            分项工程名称:k84+568\n \
           设计桩顶标高：{stylist_pier_high}\n \
           设计孔底标高：{stylist_pier_low}\n  \
          终孔孔顶标高：{practical_pier_high}\n \
           终孔孔底标高：{practical_pier_low}\n \
           护筒标高：{pile_casing_high}\n \
           应钻孔深：{(round(ought_hole_depht,3))}\n \
           吊筋长度：{(round(hanging_bar_length,3))}\n \
           设计桩长：{(round(stylist_pile_length,3))}\n \
           桩长：{(round(pile_length,3))}\n \
           灌注前孔底标高：{(round(pour_into_pier_low,3))}\n \
           钢筋笼底面标高：{(round(reinforcement_pier_low,3))}\n \
           应灌砼厚度：{(round(concrete_lenght,3))}\n"
#print(message.center(20))
print(format(message,"<20"));
