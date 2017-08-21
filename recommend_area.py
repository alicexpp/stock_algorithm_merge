# -*- coding: utf-8 -*-
# encoding=utf-8
import pylab
import copy
import BaseClass
import random
from area_coordinate_trans import *
from pylab import  mpl
from time import  sleep
import threading
from threading import Thread
mpl.rcParams['font.sans-serif'] = ['SimHei']
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
    sum_x = rect.length + other_rect.length
    # 两个矩形宽度的和
    sum_y = rect.width + other_rect.width
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
   # print "ratio_rect_list_sorted",ratio_rect_list
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


# 找到合适的摆放位置，rect是新输入的矩形，rect_list是之前所有的矩形
def find_suit_pos(rect, rect_list,max_length,max_width, area_name, current_capacity):
    new_ratio_rect_tuple = ()
    new_ratio_rect_list = []
    # 取之前的每个长方形的右上角的坐标（x,y）
    rect_x_list = [ele.top_right.x for ele in rect_list]
    rect_y_list = [ele.top_right.y for ele in rect_list]
    # 如果当前只有一个长方形
    if not rect_x_list or not rect_y_list:
        rect_list.append(rect)
        # print "rect_list:", rect_list
        storage_capacity = current_capacity + (rect.length * rect.width)/ ((max_length)*(max_width))
        ratio = 1.0
        recommend_x_coordinate = rect.center.x
        recommend_y_coordinate = rect.center.y
        print "推荐库位在 %s 中的中心点坐标为：(%.2f,%.2f)" % (area_name, recommend_x_coordinate,
                                                                recommend_y_coordinate)
        coordinate_in_area = relative__to_absolute(area_name, recommend_x_coordinate, recommend_y_coordinate)
        print "推荐库位在整个库区中的中心点坐标为：", coordinate_in_area
        paint(rect, color='b', ratio=1.0)
        pylab.text(rect.center.x, rect.center.y, ratio)
        show_all_rect(area_name, max_length, max_width)
        return storage_capacity,rect
    # 输入的长方形中右上角最大的x坐标和y坐标
    max_right = max(rect_x_list)
    max_top = max(rect_y_list)
    i = 0.
    while i <= max_top:  # width direction
        if rect.lower_left.x == max_right and  rect.lower_left.y == max_top:
            break
        temp_rect_list = copy.deepcopy(rect_list)
        j = 0.
        if max_top > Stock_Max_Width:
            i=0
            j = min(rect_x_list)

        while j <= max_right:  # length direction
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
                # 计算空间利用率
                ratio=cal_ratio(rect, rect_list)
                storage_capacity= cal_storage_capacity(rect, current_capacity, max_length, max_width )
                copy_rect = copy.deepcopy(rect)
                # 利用率和rect保存在元组中
                new_ratio_rect_tuple = (ratio, copy_rect)
                new_ratio_rect_list.append(new_ratio_rect_tuple)
                # # 绘制之前的矩形
                # paint_exit_rect(rect_list)
                # # 绘制新输入的矩形
                # paint(rect, color='r', ratio=ratio)
                # # 显示矩形
                # show_all_rect(area_name,max_length, max_width)
                # print "before", rect.lower_left.x, rect.lower_left.y
                min_x = min(rect_x_list)
                min_y = min(rect_y_list)
                i = min_y
                # width方向上的移动比较
                if j < max_right:
                    if rect.lower_right.x>max_right and rect.lower_left.x!=0.0:
                        rect.lower_left.x=0.0
                        rect.lower_left.y=min_y
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
                    rect.lower_left.x = 0.0
                    rect.lower_left.y = i
                    if len(rect_y_list) > 1:
                        rect_y_list.remove(min_y)
                    if len(rect_x_list) > 1:
                        rect_x_list.remove(min_x)
                rect.change_rect()
                # print rect.lower_left.x , rect.lower_left.y
                break
    max_ratio = find_max_ratio(new_ratio_rect_list, max_length, max_width, area_name)[0]
    max_ratio_rect = find_max_ratio(new_ratio_rect_list, max_length, max_width, area_name)[1]
    recommend_x_coordinate=max_ratio_rect.center.x
    recommend_y_coordinate=max_ratio_rect.center.y
    print "推荐库位在 %s 中的中心点坐标为：(%.2f,%.2f)" % (area_name, max_ratio_rect.center.x, max_ratio_rect.center.y)
    coordinate_in_area = relative__to_absolute(area_name, recommend_x_coordinate, recommend_y_coordinate)
    print "推荐库位在整个库区中的中心点坐标为：", coordinate_in_area
    rect_list.append(max_ratio_rect)
    # 绘制所有矩形
    paint_exit_rect(rect_list)
    pylab.text(max_ratio_rect.center.x, max_ratio_rect.center.y, max_ratio)
    show_all_rect(area_name, max_length, max_width)
    return storage_capacity,max_ratio_rect


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
    # 四舍五入取8位利用率
    ratio = round(ratio, 8)
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
            # external_diameter= random.randint(10, 20) * 100
            # print "钢卷外径：", external_diameter
            # width = random.randint(13, 17) * 100
            # print "钢卷宽度：",width
            external_diameter=raw_input("请输入钢卷外径：")
            width=raw_input("请输入钢卷宽度：")
            steel_information=BaseClass.RECT(llp=BaseClass.POINT(0.,0.),length=float(external_diameter),
                                         width=float(width))
            result=find_suit_pos(steel_information,steel_list,12000,10000,"A2C",0.2)
            print result[0]
            print result[1]



