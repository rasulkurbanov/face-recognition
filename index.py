from PIL import Image, ImageDraw
import face_recognition
import sys
import os
import shutil
from pascal_voc_writer import Writer

# Rasmlar joylashgan folder nomi
folder_name = 'images'

print(os.listdir('images'))

for img in os.listdir(folder_name):
    with open(f"{folder_name}/{img}", 'r') as img1:
        new_file = open(f"{img1.name[:-4]}.txt", 'w')
        image = face_recognition.load_image_file(img1.name)
        face_locations = face_recognition.face_locations(image)
        num_faces = len(face_locations)
        print(f"Found {num_faces} faces")
        for face_location in face_locations:
            top, right, bottom, left = face_location
            new_file.write("Face, {0}, {1}, {2}, {3} \n".format(
                top, right, bottom, left))
        os.rename(f"/media/rasul/766A9E0A6A9DC6F1/TASS/face_recognition/images/{new_file.name[7:]}",
                  f"/media/rasul/766A9E0A6A9DC6F1/TASS/face_recognition/txt_files/{new_file.name[7:]}")


# .txt fayllar joylashgan folder nomi
folder_txt = 'txt_files'

for txt in os.listdir(folder_txt):
    with open(f"{folder_txt}/{txt}", 'r') as txt_file:
        data = txt_file.readlines()
        writer = Writer(txt_file.name, 640, 360)
        for line in data:
            splittedLine = line.split(',')
            writer.addObject(splittedLine[0], splittedLine[1],
                             splittedLine[2], splittedLine[3], splittedLine[4])
        writer.save(txt_file.name[:-4] + ".xml")


for file1 in os.listdir(folder_txt):
    if(file1[-3:] == 'xml'):
        print(file1)
        os.rename(f"/media/rasul/766A9E0A6A9DC6F1/TASS/face_recognition/txt_files/{file1}",
                  f"/media/rasul/766A9E0A6A9DC6F1/TASS/face_recognition/xml_files/{file1}")



