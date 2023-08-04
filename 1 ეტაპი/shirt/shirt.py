from PIL import Image, ImageOps
import sys
import os

#print(not len(sys.argv) == 3 or sys.argv[1].lower().split(".")[1] not in ['jpg','jpeg','png'] or sys.argv[2].lower().split(".")[1] not in ['jpg','jpeg','png'] or not os.path.isfile(sys.argv[1]) or  not sys.argv[1].lower().split(".")[1] == sys.argv[2].lower().split(".")[1])

if not len(sys.argv) == 3 or sys.argv[1].lower().split(".")[1] not in ['jpg','jpeg','png'] or sys.argv[2].lower().split(".")[1] not in ['jpg','jpeg','png'] or not os.path.isfile(sys.argv[1]) or  not sys.argv[1].lower().split(".")[1] == sys.argv[2].lower().split(".")[1]:
    sys.exit(1)
else:
    inputimg = Image.open(sys.argv[1])
    overlay = Image.open('shirt.png')
    imgSize = overlay.size

    outputImg = ImageOps.fit(inputimg, imgSize)

    outputImg.paste(overlay,overlay)

    outputImg.save(sys.argv[2])


#python shirt.py before1.jpg after1.jpg
#python shirt.py before2.jpg after2.jpg
#python shirt.py before3.jpg after3.jpg

#check50 cs50/problems/2022/python/shirt