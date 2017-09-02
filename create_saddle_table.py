# coding=utf-8
import ibm_db_dbi
import random

# 连接数据库
dsn = "DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;" \
      "HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;"
conn = ibm_db_dbi.connect(dsn, "", "")

# 添加数据记录
if conn:
    conn.set_autocommit(True)
    cursor = conn.cursor()
    for i in range(1, 50):
        for j in range(1,16):
            if i <= 20 and j <=3:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                       % ("DWJ"+str(i).zfill(2)+str(j).zfill(2), 1100+2200*(j-1), 450+600*i,'0',"A1C")
                cursor.execute(cmd)
            if i > 20 and j<=3:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" + str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i + 1000, '0',"A2C")
                cursor.execute(cmd)
            if  i<=25 and 3<j<=7:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" + str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i, '0', "A3C")
                cursor.execute(cmd)
            if  i > 25 and 3 < j <= 7:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" + str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i+1000, '0', "A4C")
                cursor.execute(cmd)
            if  i<= 25 and 8<= j<13:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" +str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i, '0', "A5C")
                cursor.execute(cmd)
            if  i > 25 and 8<= j<13:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" +str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i+1000, '0', "A6C")
                cursor.execute(cmd)
            if  i<=10 and 13<= j <16:
                cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
                      % ("DWJ" +str(i).zfill(2)+str(j).zfill(2), 1100 + 2200 * (j - 1), 450 + 600 * i, '0', "A7C")
                cursor.execute(cmd)

    cursor.close()
    conn.close()

# if conn:
#     conn.set_autocommit(True)
#     cursor = conn.cursor()
#     for i in range(0, 25):
#         for j in range(1,5):
#             cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
#                        % ("DWJ"+str(i * 10 + j+486), 11000+2200*j, 450+600*i,'0',"A1C")
#             cursor.execute(cmd)
#     cursor.close()
#     conn.close()


# # if conn:
# #     conn.set_autocommit(True)
# #     cursor = conn.cursor()
# #     for i in range(0, 25):
# #         for j in range(1,5):
# #             cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
# #                        % ("DWJ"+str(i * 10 + j+486), 9000+2200*j, 450+600*i,'0',"A3C")
# #             cursor.execute(cmd)
# #     cursor.close()
# #     conn.close()
#
# # if conn:
# #     conn.set_autocommit(True)
# #     cursor = conn.cursor()
# #     for i in range(0, 23):
# #         for j in range(1,5):
# #             cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
# #                        % ("DWJ"+str(i * 10 + j+730), 9000+2200*j, 16450+600*i,'0',"A4C")
# #             cursor.execute(cmd)
# #     cursor.close()
# #     conn.close()
#
# if conn:
#     conn.set_autocommit(True)
#     cursor = conn.cursor()
#     for i in range(0, 25):
#         for j in range(1,4):
#             cmd = "INSERT INTO UACS_SADDLE_TEST(SADDLE_NO, X_CENTER,Y_CENTER,HAS_COIL,AREA_NAME) VALUES ('%s',%d,%d,%s,'%s')" \
#                        % ("DWJ"+str(i * 10 + j+954), 20000+2200*j, 450+600*i,'0',"A5C")
#             cursor.execute(cmd)
#     cursor.close()
#     conn.close()