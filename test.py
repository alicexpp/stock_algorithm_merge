import BaseClass
Area_information = {'A1C':BaseClass.AREA(), 'A2C':BaseClass.AREA(), 'A3C':BaseClass.AREA(), 'A4C':BaseClass.AREA(),
                    'A5C':BaseClass.AREA("A5C",BaseClass.RECT(llp=BaseClass.POINT(0., 0.), length=2000,
                                       width=1000)), 'A6C':BaseClass.AREA(), 'A7C':BaseClass.AREA(), 'A1S':BaseClass.AREA(),
                    'A2S':BaseClass.AREA(), 'A3S':BaseClass.AREA(), 'A4S':BaseClass.AREA(), 'A5S':BaseClass.AREA()}
new_steel_list = Area_information.get('A5C').steel_list

print new_steel_list