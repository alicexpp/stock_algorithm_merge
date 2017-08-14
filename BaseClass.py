#  coding=utf-8

MAXVALUE = float("inf")


#  定义了点和长方形两个类
class POINT:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class RECT:
    def __init__(self, llp=POINT(), length=0.0, width=0.0, valid=0, name=''):
     # 左下角坐标
        self.lower_left = llp
        self.length = length
        self.width = width
        self.valid = valid  # 0代表无效障碍物， 1代表有效障碍物
        self.name = name
        self.top_left = self.get_top_left_point()
        self.top_right = self.get_top_right_point()
        self.lower_right = self.get_lower_right_point()
        self.center = self.get_center()
        self.area = self.length * self.width

    # 左上角坐标
    def get_top_left_point(self):
        return POINT(self.lower_left.x, self.lower_left.y + self.width)

    # 右上角
    def get_top_right_point(self):
        return POINT(self.lower_left.x + self.length, self.lower_left.y + self.width)

    # 右下角
    def get_lower_right_point(self):
        return POINT(self.lower_left.x + self.length, self.lower_left.y)

    # 中心坐标
    def get_center(self):
        return POINT(self.lower_left.x + self.length / 2.0, self.lower_left.y + self.width / 2.0)

    # 坐标改变后的矩形
    def change_rect(self):
        self.top_left = self.get_top_left_point()
        self.top_right = self.get_top_right_point()
        self.lower_right = self.get_lower_right_point()
        self.center = self.get_center()


class AREA:
    def __init__(self,area_name='',steel_list = None):
        if steel_list is None:
            steel_list = list()
        self.area_name = area_name
        self.steel_list = steel_list
