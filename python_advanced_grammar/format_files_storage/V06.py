import xml.etree.ElementTree as et

# 在内存中创建一个新的而文档

etree = et.ElementTree()

e = et.Element("Student")

etree._setroot(e)

e_name = et.SubElement(e, "Name")
e_name.text = 'hehehe'

etree.write("V06.xml")


