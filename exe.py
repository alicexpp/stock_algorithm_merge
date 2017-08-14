#coding=utf-8
import driver
import random
import BaseClass
import recommend_area

suit_pos_dict = dict()
steel_list = list()
temp_name =''
Area_information = {'A1C': BaseClass.AREA(), 'A2C': BaseClass.AREA(), 'A3C': BaseClass.AREA(), 'A4C': BaseClass.AREA(),
                    'A5C': BaseClass.AREA(), 'A6C': BaseClass.AREA(), 'A7C': BaseClass.AREA(), 'A1S': BaseClass.AREA(),
                    'A2S': BaseClass.AREA(), 'A3S': BaseClass.AREA(), 'A4S': BaseClass.AREA(), 'A5S': BaseClass.AREA()}
for i in range(1,20):
    external_diameter= random.randint(10, 20) * 100
    print "钢卷外径：", external_diameter
    width = random.randint(13, 17) * 100
    print "钢卷宽度：",width
    # external_diameter =raw_input("请输入钢卷外径：")
    # width = raw_input("请输入钢卷宽度：")
    area_name = driver.fc_test('back_closed_coil',float(external_diameter),float(width))
    Max_Length = driver.select_data('UACS_STOCK_INFO', area_name)[0]
    Max_Width = driver.select_data('UACS_STOCK_INFO', area_name)[1]
    Current_Capacity = driver.select_data('UACS_STOCK_INFO', area_name)[2]
    print "放置之前：", Current_Capacity
    steel_information = BaseClass.RECT(llp=BaseClass.POINT(0., 0.), length=float(external_diameter),
                                       width=float(width))
    # 获取当前区域的steel_list，每个区域的steel_list不同
    new_steel_list = Area_information.get(area_name).steel_list
    new_storage_capacity=recommend_area.find_suit_pos(steel_information, new_steel_list,
                                                      Max_Length, Max_Width, area_name, Current_Capacity)
    driver.update_area_ratio('UACS_STOCK_INFO',area_name, new_storage_capacity)
    print "放置之后：",new_storage_capacity
    print "the coil should put in %s area"% area_name



