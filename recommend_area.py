# -*- coding: utf-8 -*-
# encoding=utf-8
import pylab
import copy
import BaseClass
import random
from area_coordinate_trans import *

import ibm_db_dbi
import area_coordinate_trans
#连接数据库
dsn = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;" \
      "HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;"
conn = ibm_db_dbi.connect(dsn, "", "")
if conn:
    print "connect db2 successed"

# 库区最大长度
Stock_Max_Length = 12000
# 库区最大宽度
Stock_Max_Width = 10000


# 判断两个矩形相交的方法
def rectangles_cross(rect, other_rect):
    # 为了检查两个矩形是否与障碍物相交。
    # 分别比较两个矩形的重心在x轴方向上和y轴方向上的距离与两个矩形的长或者宽的一半的和的大小。
    # 如果重心的在x轴和y轴上的距离都比他们边长和的一半要小就符合相交的条件。

    # 两个矩形的重心的X坐标的差值的两倍
    x_focus_distance = abs(rect.center.x - other_rect.center.x) * 2.0
    # 两个矩形的重心的Y坐标的差值的两倍
    y_focus_distance = abs(rect.center.y - other_rect.center.y) * 2.0
    # 两个矩形边长的和
    sum_x = rect.width + other_rect.width
    # 两个矩形宽度的和
    sum_y = rect.length + other_rect.length
    # 两个矩形相交
    if x_focus_distance - sum_x < 0 and y_focus_distance - sum_y < 0:
        return True
    else:
        return False


# 循环判断长方形与其他长方形是否相交
def cross_rect_list(rect, rect_list):
    # rect_list为空
    if not rect_list:
        return True, None
    # 判断新输入的长方形与所有的长方形是否相交
    for item in rect_list:
    # 如果相交，返回相交的矩形
        if rectangles_cross(rect, item):
            return False, item
    return True, None


# 找到最大空间利用率时的长方形摆放位置
def find_max_ratio(ratio_rect_list, max_length, max_width, area_name):
    if not ratio_rect_list:
        print"only rect"
        return
    ratio_list = [item[0] for item in ratio_rect_list]
    # print "ratio_rect_list=",ratio_rect_list
    #  将用利用率和长方形作为列表元组元素的列表按照ratio从大到小的顺序排列
    ratio_rect_list.sort(reverse=True)
    #print "ratio_rect_list_sorted",ratio_rect_list
    index= 0
    while index <= len(ratio_rect_list):
        max_ratio=ratio_rect_list[index][0]
        max_ratio_rect=ratio_rect_list[index][1]
        if max_ratio_rect.top_right.x > max_length or max_ratio_rect.top_right.y > max_width :
            index = index + 1
            while index==len(ratio_rect_list):
              print "the stock area is full "
              show_all_rect(area_name, max_length, max_width)
              return
            continue
        # print max_ratio,max_ratio_rect.top_right.x, max_ratio_rect.top_right.y
        return max_ratio,max_ratio_rect


#  返回推荐位置中心的X坐标
def output_coordinate_x(recommend_rect):
  return recommend_rect.center.x


#  返回推荐位置中心的Y坐标
def output_coordinate_y(recommend_rect):
    return recommend_rect.center.y


# 求取推荐位置的中心坐标并保存至列表中，recommend_rect_list中保存的是推荐的钢卷摆放的位置，即rect
def recommend_position_data(recommend_rect):
    x_center = recommend_rect.center.x
    y_center = recommend_rect.center.y
    # 将计算出的钢卷摆放位置坐标存储在元组中
    position_center_coordinate = (x_center,y_center)
    # # 将其计算出的中心坐标全都保存至列表中便于遍历
    # recommend_position_list.append(position_coordinate)
    return position_center_coordinate


# 在库图数据库中寻找合适的鞍座，向外延伸查询，并寻找与其挨着最近的鞍座,recommend_position_list保存的是推荐的摆放
# 位置的中心点坐标，即rect.center.x和rect.center.y
def select_saddle_date(table_name,recommend_rect_center,area_name):
    conn.set_autocommit(True)
    cursor=conn.cursor()
    x_center = recommend_rect_center[0]
    y_center = recommend_rect_center[1]
    sql="SELECT MIN(X_CENTER),MIN(Y_CENTER) FROM %s WHERE Y_CENTER=(SELECT MIN(Y_CENTER) FROM %s WHERE" \
        " Y_CENTER >= %d AND HAS_COIL = 0 AND AREA_NAME='%s') AND X_CENTER >= %d AND HAS_COIL = 0 AND AREA_NAME = '%s' " \
        ""%(table_name,table_name,y_center,area_name,x_center,area_name)
    stmt= cursor.execute(sql)
    select_saddle_center= cursor.fetchall()
    cursor.close()
    return select_saddle_center


# 更新库图中是否有钢卷的状态位
def update_has_coil(table_name, x_center, y_center):
    conn.set_autocommit(True)
    cursor = conn.cursor()
    update_sql="UPDATE %s SET HAS_COIL='%s' WHERE X_CENTER = %d AND Y_CENTER = %d"%(table_name,'1',x_center,y_center)
    stmt = cursor.execute(update_sql)
    cursor.close()


# 找到合适的摆放位置，rect是新输入的矩形，rect_list是之前所有的矩形
def find_suit_pos(rect, rect_list,max_length,max_width, area_name, current_capacity):
    select_saddle=[]
    width = rect.width
    external_diameter = rect.length
    rect_x_start = rect.lower_left.x
    rect_y_start = rect.lower_left.y
    new_ratio_rect_tuple = ()
    new_ratio_rect_list = []
    # 取之前的每个长方形的右上角的坐标（x,y）
    rect_x_list = [ele.top_right.x for ele in rect_list]
    rect_y_list = [ele.top_right.y for ele in rect_list]
    # 如果当前只有一个长方形
    if not rect_x_list or not rect_y_list:
        rect_center_x = rect.center.x
        rect_center_y = rect.center.y
        # 需要将其x,y坐标转换为大区域的坐标，再去选鞍座号，相对坐标转换成大区绝对坐标
        CENTER_X = area_coordinate_trans.relative__to_absolute(area_name, rect_center_x, rect_center_y)[0]
        CENTER_Y = area_coordinate_trans.relative__to_absolute(area_name, rect_center_x, rect_center_y)[1]
        print "CENTER_X:", CENTER_X
        print "CENTER_Y:", CENTER_Y
        rect_center = (CENTER_X, CENTER_Y)
        select_saddle = select_saddle_date("UACS_SADDLE_TEST", rect_center, area_name)
        print "最终选择的小区的坐标为：",rect_center
        print "最终选择的鞍座坐标为：", select_saddle
        select_saddle_x = select_saddle[0][0]
        select_saddle_y = select_saddle[0][1]
        new_saddle_rect = BaseClass.RECT(llp=BaseClass.POINT(select_saddle_x-float(width) / 2,
                                                             select_saddle_y-float(external_diameter) / 2),
                                         length=float(external_diameter), width=float(width))
        storage_capacity = current_capacity + (rect.length * rect.width)/ ((max_length)*(max_width))
        ratio = 1.0
        # 将以库图中的鞍座坐标为中心点，转换成小区域的中心点，以便绘制rect
        new_recommend_area_x = area_coordinate_trans.absolute_to_relative(area_name, select_saddle_x,select_saddle_y)[0]
        new_recommend_area_y = area_coordinate_trans.absolute_to_relative(area_name, select_saddle_x,select_saddle_y)[1]
        new_recommend_rect = BaseClass.RECT(llp=BaseClass.POINT(new_recommend_area_x-float(width) / 2,
                                                             new_recommend_area_y-float(external_diameter) / 2),
                                         length=float(external_diameter), width=float(width))
        rect_list.append(new_recommend_rect)
        update_has_coil('UACS_SADDLE_TEST', new_saddle_rect.center.x, new_saddle_rect.center.y)
        paint(new_recommend_rect, color='b', ratio=1.0)
        pylab.text(new_recommend_rect.center.x, new_recommend_rect.center.y, ratio)
        show_all_rect(area_name, max_length, max_width)
        return storage_capacity, new_saddle_rect
    # 输入的长方形中右上角最大的x坐标和y坐标
    max_right = max(rect_x_list)
    max_top = max(rect_y_list)
    i = 0.
    while i <= max_top and select_saddle!=[(None,None)]:  # width direction
        if rect.lower_left.x == max_right and rect.lower_left.y == max_top:
            break
        temp_rect_list = copy.deepcopy(rect_list)
        j = 0.
        # if max_top > Stock_Max_Width:
        #     i = 0
        #     j = min(rect_x_list)
        while j <= max_right and select_saddle!=[(None,None)]:  # length direction
            cross_flag, cross_rect = cross_rect_list(rect, temp_rect_list)
            # 有矩形相交
            if not cross_flag:
            #  如果相交，j为相交的矩形的右上角的x坐标，相交的矩形的右上角的x坐标赋给当前输入矩形的左下角x，
            #  当前新矩形沿x方向移动到相交矩形最外面
                j = cross_rect.top_right.x
                rect.lower_left.x = j
            # 移动后的输入矩形的新坐标
                rect.change_rect()
            # 将此相交矩形从需要判断相交的矩形中移除
                temp_rect_list.remove(cross_rect)
                continue
            # 不相交
            else:
                copy_rect = copy.deepcopy(rect)
                copy_rect_center_x = copy_rect.center.x
                copy_rect_center_y = copy_rect.center.y
                # 需要将其x,y坐标转换为大区域的坐标，再去选鞍座号，相对坐标转换成大区绝对坐标
                CENTER_X = area_coordinate_trans.relative__to_absolute(area_name, copy_rect_center_x, copy_rect_center_y)[0]
                CENTER_Y = area_coordinate_trans.relative__to_absolute(area_name, copy_rect_center_x, copy_rect_center_y)[1]
                # 计算出来的大区中心点坐标
                cal_recommend_rect_center = (CENTER_X, CENTER_Y)
                # print "计算推荐摆放位置的中心坐标：", cal_recommend_rect_center
                # 根据计算出的推荐位置的中心坐标选择合适的鞍座
                select_saddle = select_saddle_date("UACS_SADDLE_TEST", cal_recommend_rect_center,area_name)
                if select_saddle!=[(None,None)]:
                    # print "选择的库图中的鞍座坐坐标为：", select_saddle
                    select_saddle_x = select_saddle[0][0]
                    select_saddle_y = select_saddle[0][1]
                    # 将以库图中的鞍座坐标为中心点，转换成小区域的中心点，以便绘制rect
                    new_recommend_area_x = \
                    area_coordinate_trans.absolute_to_relative(area_name, select_saddle_x, select_saddle_y)[0]
                    new_recommend_area_y = \
                    area_coordinate_trans.absolute_to_relative(area_name, select_saddle_x, select_saddle_y)[1]
                    # 小区域中的矩形
                    new_recommend_rect = BaseClass.RECT(llp=BaseClass.POINT(new_recommend_area_x - float(width) / 2,
                                                                            new_recommend_area_y - float(
                                                                                external_diameter) / 2),
                                                        length=float(external_diameter), width=float(width))
                    # 计算以鞍座号摆放的位置的空间利用率
                    ratio_saddle = cal_ratio(new_recommend_rect, rect_list)
                    # 计算以鞍座号摆放的位置的库容率
                    storage_capacity = cal_storage_capacity(new_recommend_rect, current_capacity, max_length, max_width)
                    # 将新的位置和空间利用率保存在元组中
                    ratio_saddle_rect_tuple = (ratio_saddle, new_recommend_rect)
                    new_ratio_rect_list.append(ratio_saddle_rect_tuple)
                    # # 绘制之前的矩形
                    # paint_exit_rect(rect_list)
                    # # 绘制新输入的矩形
                    # paint(new_recommend_rect, color='r', ratio=ratio_saddle)
                    # # 显示矩形
                    # show_all_rect(area_name,max_length, max_width)
                    min_x = min(rect_x_list)
                    min_y = min(rect_y_list)
                    i = min_y
                    # width方向上的移动比较
                    if j < max_right:
                        if rect.lower_right.x>max_right and rect.lower_left.x!=rect_x_start:
                            rect.lower_left.x= rect_x_start
                            rect.lower_left.y= min_y
                        else:
                            # 将比较的矩形中的最小x坐标赋给新长方形左下角x
                            rect.lower_left.x = min_x
                        # 将比较的矩形中的最小y坐标赋给新长方形的左下角y
                            rect.lower_left.y = min_y
                        if len(rect_y_list) > 1:
                            rect_y_list.remove(min_y)
                        if len(rect_x_list) > 1:
                            rect_x_list.remove(min_x)
                    else:
                        rect.lower_left.x = rect_x_start
                        rect.lower_left.y = i
                        if len(rect_y_list) > 1:
                            rect_y_list.remove(min_y)
                        if len(rect_x_list) > 1:
                            rect_x_list.remove(min_x)
                    rect.change_rect()
                    # print rect.lower_left.x , rect.lower_left.y
                    break

    if select_saddle !=[(None, None)]:
        max_ratio = find_max_ratio(new_ratio_rect_list, max_length, max_width, area_name)[0]
        # 这是小区中的矩形和坐标
        max_ratio_rect = find_max_ratio(new_ratio_rect_list, max_length, max_width, area_name)[1]
        recommend_x_coordinate=max_ratio_rect.center.x
        recommend_y_coordinate=max_ratio_rect.center.y
        print "最终选择的小区的坐标为：%d,%d" % (max_ratio_rect.center.x, max_ratio_rect.center.y)
        # 将小区中的矩形坐标转换成大区的鞍座坐标
        saddle_x_center = area_coordinate_trans.relative__to_absolute(area_name, recommend_x_coordinate,recommend_y_coordinate)[0]
        saddle_y_center = area_coordinate_trans.relative__to_absolute(area_name, recommend_x_coordinate, recommend_y_coordinate)[1]
        print "最终选择的鞍座坐标为：%d,%d" % (saddle_x_center, saddle_y_center)
        new_saddle_rect = BaseClass.RECT(llp=BaseClass.POINT(saddle_x_center - float(width) / 2,
                                                             saddle_y_center - float(external_diameter) / 2),
                                         length=float(external_diameter), width=float(width))
        update_has_coil('UACS_SADDLE_TEST', saddle_x_center, saddle_y_center)
        rect_list.append(max_ratio_rect)
        # 绘制所有矩形
        paint_exit_rect(rect_list)
        pylab.text(max_ratio_rect.center.x, max_ratio_rect.center.y, max_ratio)
        show_all_rect(area_name, max_length, max_width)
        return storage_capacity,new_saddle_rect
    else:
        return False

# 绘制之前所有的矩形
def paint_exit_rect(rect_list):
    for item in rect_list:
        paint(item)


#  显示之前所有的矩形
def show_all_rect(area_name, max_length, max_width):
    pylab.title(area_name)
    pylab.xlabel('x_diameter')
    pylab.ylabel('y_width')
    pylab.xlim(0, max_length)
    pylab.ylim(0, max_width)
    pylab.legend()
    pylab.show()


# 绘制矩形的四个点
def paint(rectangle, color='b', ratio=0.):
    rect_x = [rectangle.top_left.x, rectangle.top_right.x,
              rectangle.lower_right.x, rectangle.lower_left.x, rectangle.top_left.x]

    rect_y = [rectangle.top_left.y, rectangle.top_right.y,
              rectangle.lower_right.y, rectangle.lower_left.y, rectangle.top_left.y]
    #pylab.plot(rect_x,rect_y,color)
    pylab.plot(rect_x, rect_y, color)
    if color == 'r':
        pylab.text(rectangle.center.x, rectangle.center.y, ratio)


# 计算空间利用率
def cal_ratio(input_rect, rects):
    new_rect_list = rects+ [input_rect]
    # 利用率的计算公式= 所有长方形的面积之和/最大边界矩形面积
    ratio = sum([item.area for item in new_rect_list]) / (
        max([item.top_right.x for item in new_rect_list]) *
        max([item.top_right.y for item in new_rect_list]))
    # 四舍五入取3位利用率
    ratio = round(ratio, 3)
    return ratio


# 计算库区的库容率
def cal_storage_capacity(input_rect, current_capacity, max_length, max_width):
    # 库容率的计算公式 = 当前库容率+该长方形的面积/ 库区面积
    storage_capacity = current_capacity + (input_rect.width * input_rect.length)/ (max_length * max_width)
    return storage_capacity



if __name__ == "__main__":

        suit_pos_dict = dict()
        steel_list = list()

        while True:
            width = random.randint(11, 15) * 100
            print "钢卷宽度：", width
            external_diameter= random.randint(7, 12) * 100
            print "钢卷外径：", external_diameter
            center_x = 1100
            center_y = 1050
            while float(width) / 2 > center_x:
                center_x = center_x + 2200
            while float(external_diameter) / 2 > center_y:
                center_y = center_y + 600

            # external_diameter=raw_input("请输入钢卷外径：")
            # width=raw_input("请输入钢卷宽度：")
            steel_information = BaseClass.RECT(
                llp=BaseClass.POINT(center_x - float(width) / 2, center_y - float(external_diameter) / 2),
                length=float(external_diameter),
                width=float(width))

            find_suit_pos(steel_information, steel_list, 22000, 30000, "A2C", 0.2)




