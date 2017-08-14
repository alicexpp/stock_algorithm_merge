import BaseClass
Area_information = {'A1C':BaseClass.AREA(), 'A2C':BaseClass.AREA(), 'A3C':BaseClass.AREA(), 'A4C':BaseClass.AREA(),
                    'A5C':BaseClass.AREA(), 'A6C':BaseClass.AREA(), 'A7C':BaseClass.AREA(), 'A1S':BaseClass.AREA(),
                    'A2S':BaseClass.AREA(), 'A3S':BaseClass.AREA(), 'A4S':BaseClass.AREA(), 'A5S':BaseClass.AREA()}
new_steel_list = Area_information.get('A1C').steel_list
rect_list=[100,200]
new_steel_list.append(rect_list)
print new_steel_list