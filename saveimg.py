from PIL import Image
imgpath = '/home/shjeong/Data/HumanHeadDetection/HollywoodHeads/JPEGImages/'
filelist = ['mov_011_129448.jpeg','mov_008_117754.jpeg','mov_004_029507.jpeg']
for f in filelist:
    image = Image.open(imgpath+f)
    image.save('/home/shjeong/HumanHeadDetect/'+f)