from posixpath import curdir
from PIL import Image, ImageDraw
import face_recognition
import sys
import os
# from test import txt_to_xml
from pascal_voc_writer import Writer


imageName = sys.argv[1]
current_dir = os.getcwd()

# Imageni load qilish
image = face_recognition.load_image_file(imageName)


# face_recognition face larni aniqlaydi
face_locations = face_recognition.face_locations(image)
num_faces = len(face_locations)
print(f"Found {num_faces} faces")


pil_image = Image.fromarray(image)

# Yangi txt file yaratish
# imageName2 = imageName[-4:]
# print(imageName2)
new_file = open(f"{imageName}.txt", "w")

for face_location in face_locations:
    # Wr    top, right, bottom, left = face_location
iting to new_file.txt
    new_file.write("Face, {0}, {1}, {2}, {3} \n".format(
        top, right, bottom, left))
    draw_shape = ImageDraw.Draw(pil_image)
    draw_shape.rectangle([left, top, right, bottom], outline="red")


# imageni shu papkani o'ziga save qilish
# pil_image.save("output_image.jpg")
pil_image.show()