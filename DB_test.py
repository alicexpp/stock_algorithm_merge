#coding=utf-8
import ibm_db
#连接数据库
conn = ibm_db.connect("DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
if conn:
    print "connect db2 successed"

#读取数据库中，每个库区的当前库容量、最大库容量
def select_data(table_name,area_name):
    sql="SELECT * FROM %s WHERE STOCK_NAME='%s'"% (table_name,area_name)
    stmt = ibm_db.exec_immediate(conn,sql)
    row = ibm_db.fetch_assoc(stmt)
    return row['MAX_LENGTH'],row['MAX_WIDTH'], row['CURRENT_RATIO']

def update_area_ratio(table_name, area_name, new_ratio):
    update_ratio = "UPDATE %s SET CURRENT_RATIO = '%f' WHERE STOCK_NAME = '%s' "%(table_name, new_ratio, area_name)
    ibm_db.exec_immediate(conn, update_ratio)
    ibm_db.commit(conn)
    return area_name

if __name__ == "__main__":
   print  "最大长度为",select_data("UACS_STOCK_INFO","A1C")[0]
   print  "最大宽度为",select_data("UACS_STOCK_INFO","A1C")[1]
   print  "当前库容率为",select_data("UACS_STOCK_INFO","A1C")[2]
   update_area_ratio("UACS_STOCK_INFO","A1C", 0.1)