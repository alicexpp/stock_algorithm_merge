# coding=utf-8

import ibm_db_dbi

conn = ibm_db_dbi.connect("DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
if conn:
    conn.set_autocommit(True)
    print "connect db2 successed"


def count_stock_num(table_name,area_name):
    select_sql = "SELECT COUNT(*) FROM  %s  WHERE STOCK_NAME='%s'" % (table_name,area_name)
    # stmt = ibm_db_dbi.exec_immediate(conn, select_sql)
    # # row是字典形式
    # row = ibm_db_dbi.fetch_assoc(stmt)
    # 返回该区域的可放钢卷的位数
    c = conn.cursor()
    c.execute(select_sql)
    row = c.fetchone()
    return row[0]


# def read_stock_status(table_name,area_name):
#     stock_count = count_stock_num(table_name,area_name)
#     list = []
#     sql="SELECT * FROM %s " % (table_name)
#     stmt = ibm_db.exec_immediate(conn, sql)
#     r=ibm_db.fetch_both(stmt)
#     while r:
#         if r.get('STOCK_NAME') == area_name:
#             list.append(r)
#         r = ibm_db.fetch_both(stmt)
#     for i in range(0,stock_count):
#          external_diameter = list[i].get('COIL_OUT_LENGTH')
#          width = list[i].get('COIL_WIDTH')
#          center_x_exist = list[i].get('X_CENTER')
#          center_y_exist = list[i].get('Y_CENTER')
#          print external_diameter,width,center_x_exist,center_y_exist

def read_stock_status(table_name, area_name):
    stock_count = count_stock_num(table_name,area_name)
    list = []
    sql="SELECT * FROM %s WHERE STOCK_NAME = '%s'" % (table_name,area_name)
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

    # for i in range(0,stock_count):
    #      external_diameter = list[i].get('COIL_OUT_LENGTH')
    #      width = list[i].get('COIL_WIDTH')
    #      center_x_exist = list[i].get('X_CENTER')
    #      center_y_exist = list[i].get('Y_CENTER')
    #      print external_diameter,width,center_x_exist,center_y_exist

if __name__ =="__main__":
    n=count_stock_num('UACS_STOCK_STATUS_TEST','A5C')
    steel_list_rows=read_stock_status('UACS_STOCK_STATUS_TEST','A5C')
    for item in steel_list_rows:
        print item[1],item[2],item[4],item[5]