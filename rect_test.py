#  coding=utf-8
#  根据中心点坐标画长方形
import pylab
#  定义了点和长方形两个类
class POINT:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class RECT:
    def __init__(self, center=POINT(), length=0.0, width=0.0, valid=0, name=''):
     # 左下角坐标
        self.center = center
        self.length = length
        self.width = width
        self.valid = valid  # 0代表无效障碍物， 1代表有效障碍物
        self.name = name
        self.lower_left = self.get_lower_left_point()
        self.top_left = self.get_top_left_point()
        self.top_right = self.get_top_right_point()
        self.lower_right = self.get_lower_right_point()

        self.area = self.length * self.width

    # 左上角坐标
    def get_top_left_point(self):
        return POINT(self.center.x-self.length/2.0, self.center.y + self.width/2.0)

    # 左下角坐标
    def get_lower_left_point(self):
        return POINT(self.center.x-self.length/2.0, self.center.y - self.width/2.0)

    # 右上角
    def get_top_right_point(self):
        return POINT(self.center.x+self.length/2.0, self.center.y + self.width/2.0)

    # 右下角
    def get_lower_right_point(self):
        return POINT(self.center.x + self.length/2.0, self.center.y-self.width/2.0)
    #
    # # 中心坐标
    # def get_center(self):
    #     return POINT(self.lower_left.x + self.length / 2.0, self.lower_left.y + self.width / 2.0)


    # 坐标改变后的矩形
    def change_rect(self):
        self.lower_left=self.get_lower_left_point()
        self.top_left = self.get_top_left_point()
        self.top_right = self.get_top_right_point()
        self.lower_right = self.get_lower_right_point()
        # self.center = self.get_center()


#   绘制矩形的四个点
def paint(rectangle, color='b', ratio=0.):
    rect_x = [rectangle.top_left.x, rectangle.top_right.x,
              rectangle.lower_right.x, rectangle.lower_left.x, rectangle.top_left.x]

    rect_y = [rectangle.top_left.y, rectangle.top_right.y,
              rectangle.lower_right.y, rectangle.lower_left.y, rectangle.top_left.y]

    pylab.plot(rect_x, rect_y, color)
    if color == 'r':
        pylab.text(rectangle.center.x, rectangle.center.y, ratio)



def show_all_rect(area_name, max_length, max_width):
    pylab.title(area_name)
    pylab.xlabel('x_diameter')
    pylab.ylabel('y_width')
    pylab.xlim(0, max_length)
    pylab.ylim(0, max_width)
    pylab.legend()
    pylab.show()


if __name__ =="__main__":
    new_rect= RECT(center=POINT(),length=4, width=6)
    print new_rect.lower_left.x,new_rect.lower_left.y
    paint(new_rect)
    show_all_rect("test", 10, 10)
