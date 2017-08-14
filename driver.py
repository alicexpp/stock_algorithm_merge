#coding=utf-8

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_compiler
from pyke import krb_traceback
from pyke import goal

import ibm_db
import datetime
import time
import recommend_area
import BaseClass

Area_information = {'A1C': BaseClass.AREA(), 'A2C': BaseClass.AREA(), 'A3C': BaseClass.AREA(), 'A4C': BaseClass.AREA(),
                    'A5C': BaseClass.AREA(), 'A6C': BaseClass.AREA(), 'A7C': BaseClass.AREA(), 'A1S': BaseClass.AREA(),
                    'A2S': BaseClass.AREA(), 'A3S': BaseClass.AREA(), 'A4S': BaseClass.AREA(), 'A5S': BaseClass.AREA()}

engine = knowledge_engine.engine(__file__)
# 激活事实库
engine.activate('fc_area_recommend')


# 判断库满的函数
def fc_test(coil_kind,external_diameter, width, status1=1):
    fc_goal = goal.compile('coil_area.move_area($coil_kind,$area,$status)')
    try:
        with fc_goal.prove(engine, coil_kind=coil_kind, status=status1) as gen:
            for vars, plan in gen:
                # 读取数据库中库区的信息
                # 当前库区的最大长度
                Max_Length = select_data('UACS_STOCK_INFO', vars['area'])[0]
                # 当前库区的最大宽度
                Max_Width = select_data('UACS_STOCK_INFO', vars['area'])[1]
                # 当前库区的库容率
                Current_Ratio = select_data('UACS_STOCK_INFO', vars['area'])[2]
                #  计算该钢卷放入之后的库容率
                Cal_Capacity= Current_Ratio + (external_diameter * width)/ (Max_Length * Max_Width)
                print "若该钢卷放入%s区域，库容率为%f"%(vars['area'],Cal_Capacity)
                if Cal_Capacity < 1:
                    print"%s should be played in %s" % (coil_kind, vars['area'])
                    return vars['area']
                else:
                    print "the %s area is full" % (vars['area'])
                    status_n = status1 + 1
                    return fc_test(coil_kind,external_diameter,width,status1=status_n)
        return "null"
    except:
        print "something err"
        krb_traceback.print_exc()
        sys.exit()


#连接数据库
conn = ibm_db.connect("DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
if conn:
    print "connect db2 successed"

#读取数据库中，每个库区的当前库容量、最大库容量
def select_data(table_name,area_name):
    sql="SELECT * FROM %s WHERE STOCK_NAME='%s'"% (table_name,area_name)
    stmt = ibm_db.exec_immediate(conn,sql)
    row = ibm_db.fetch_assoc(stmt)
    return row['MAX_LENGTH'], row['MAX_WIDTH'], row['CURRENT_RATIO']

#更新数据库，放入一个钢卷，数据库的当前库容量加1
def update_current(table_name,area_name):
    old_result=select_data(table_name,area_name)
    new_current=old_result[0]+1
    update_sql="UPDATE %s SET CURRENT_NO='%d' WHERE STOCK_NAME='%s'"%(table_name,new_current,area_name)
    ibm_db.exec_immediate(conn,update_sql)
    ibm_db.commit(conn)
    return new_current

#按行堆放的钢卷
def select_position(area,row_number,column_number,current_num):
    #第i行
    i=current_num/column_number+1
    #第j列
    j=current_num%column_number
    while j==0:
        i=i-1
        j=4
    print 'the coil should put in %s, %d 排，%d 列' % (area,i, j)

#c++调用的函数接口
def place_position(coil_information):
    begin = datetime.datetime.now().microsecond
    begin1=time.time()
    area_name = fc_test(coil_information)
    update_current('UACS_STOCK_INFORMATION_TEST', area_name)
    end = datetime.datetime.now().microsecond
    end1=time.time()
    re=float(end-begin)
    print "python程序执行时间为：%f ms" % (re/1000.0)

#统计区域中的可放钢卷位的位数
def count_area_num(table_name,area_name):
    select_sql = "SELECT COUNT(*) FROM  %s  WHERE PLACEMENT_STATUS='0'AND STOCK_NUM='%s'"%(table_name,area_name)
    stmt = ibm_db.exec_immediate(conn, select_sql)
    # row是字典形式
    row = ibm_db.fetch_assoc(stmt)
    #返回该区域的可放钢卷的位数
    return row['1']

# 先找最小库位号的库位信息
def find_min_region(table_name,area_name):
    select_sql = "SELECT MIN(REGION_NUM) FROM  %s WHERE PLACEMENT_STATUS='0'AND STOCK_NUM='%s'"%(table_name,area_name)
    stmt = ibm_db.exec_immediate(conn, select_sql)
    # row是字典形式
    row = ibm_db.fetch_assoc(stmt)
    return row['1']

# 更新最小库位号的库位状态信息，把状态0改为状态1
def update_min_region(table_name,area_name):
    region_num=find_min_region(table_name,area_name)
    update_sql = "UPDATE %s SET PLACEMENT_STATUS ='%d' WHERE REGION_NUM='%s'" % (table_name, 1, region_num)
    ibm_db.exec_immediate(conn, update_sql)
    ibm_db.commit(conn)
    return region_num

# 放置钢卷后，更新库区的库容率
def update_area_ratio(table_name, area_name, new_ratio):
    update_ratio = "UPDATE %s SET CURRENT_RATIO = '%f' WHERE STOCK_NAME = '%s' "%(table_name, new_ratio, area_name)
    ibm_db.exec_immediate(conn, update_ratio)
    ibm_db.commit(conn)
    return area_name


# 先判断推荐库位，再根据库位推荐相应的库区的函数
def recommend_stock_position(table_name, coil_information, external_diameter, width):
    area_name = fc_test(coil_information, float(external_diameter), float(width))
    Max_Length = select_data(table_name, area_name)[0]
    Max_Width = select_data(table_name, area_name)[1]
    Current_Capacity = select_data(table_name, area_name)[2]
    print "放置之前：", Current_Capacity
    steel_information = BaseClass.RECT(llp=BaseClass.POINT(0., 0.), length=float(external_diameter),
                                       width=float(width))
    # 获取当前区域的steel_list，每个区域的steel_list不同
    new_steel_list = Area_information.get(area_name).steel_list
    print new_steel_list
    new_storage_capacity = recommend_area.find_suit_pos(steel_information, new_steel_list,
                                                        Max_Length, Max_Width, area_name, Current_Capacity)
    update_area_ratio('UACS_STOCK_INFO', area_name, new_storage_capacity)
    print "放置之后：", new_storage_capacity
    print "the coil should put in %s area" % area_name

if __name__ == "__main__":
    while True:
        external_diameter =raw_input("请输入钢卷外径：")
        width = raw_input("请输入钢卷宽度：")
        recommend_stock_position('UACS_STOCK_INFO', 'back_closed_coil', float(external_diameter),float(width))
        print 'successful'