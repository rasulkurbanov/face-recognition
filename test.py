from pascal_voc_writer import Writer
import sys

# Rasm title

imageName = '05.jpg'
fileName = sys.argv[1]


with open(fileName, 'r') as file1:
    data = file1.readlines()
    writer = Writer(imageName, 640, 360)

    for line in data:
        splittedLine = line.split(',')
        writer.addObject(splittedLine[0], splittedLine[1],
                         splittedLine[2], splittedLine[3], splittedLine[4])
        writer.save(imageName + ".xml")


'''
file1 = open('01.jpg.txt', 'r')
Lines = file1.readlines()
writer = Writer(imageName, 640, 360)
print(Lines)



for line in Lines:
    splittedLine = line.split(',')
    writer.addObject(splittedLine[0], splittedLine[1],
                     splittedLine[2], splittedLine[3], splittedLine[4])
    writer.save(imageName + ".xml")
'''


# def txt_to_xml(img_name, txt_file):
#     file1 = open(txt_file.name, 'r')
#     Lines = file1.readlines()
#     writer = Writer(img_name, 640, 360)

#     for line in Lines:
#         splittedLine = line.split(',')
#         writer.addObject(splittedLine[0], splittedLine[1],
#                          splittedLine[2], splittedLine[3], splittedLine[4])
#         writer.save(img_name.name + ".xml"
