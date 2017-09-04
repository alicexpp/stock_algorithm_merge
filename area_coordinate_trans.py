# coding=utf-8
#  该字典里存储每个库区的名字和库区相对偏移量
Area_Coordinate={"A1C": (0,0), "A2C": (0,14050), "A3C": (6600, 0), "A4C": (6600, 16000), "A5C": (15400,0),
                 "A6C": (15400, 16000), "A7C": (28600, 0)}


# 将小区域的相对坐标转换成大区域的绝对坐标
def relative__to_absolute(area_name, x_position, y_position):
    x_offset = Area_Coordinate.get(area_name)[0]
    y_offset = Area_Coordinate.get(area_name)[1]
    x_to_absolute = x_position + x_offset
    y_to_absolute = y_position + y_offset
    return x_to_absolute, y_to_absolute


# 将大区域的绝对坐标转换成小区域的相对坐标
def absolute_to_relative(area_name, x_coordinate, y_coordinate):
    x_offset = Area_Coordinate.get(area_name)[0]
    y_offset = Area_Coordinate.get(area_name)[1]
    x_to_relative = x_coordinate - x_offset
    y_to_relative = y_coordinate - y_offset
    return x_to_relative, y_to_relative


if __name__=="__main__":
    print  relative__to_absolute("A2C",2000,1000)[1]
