import os
import cv2

def getRGB(image,y1,y2,x1,x2):
	r=g=b=n=0
	for i in range(y1,y2):
		for j in range(x1,x2):
			b+=image[i,j][0]
			g+=image[i,j][1]
			r+=image[i,j][2]
			n+=1
	r=r//n
	g=g//n
	b=b//n
	return r,g,b

class_words=['aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair', 'container',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor', 'words']

f=open("res.txt",'a+')
f.write('image_name\t\t\tobject_class_code\t\t\t\t\t\tcolor_code\twords\n')
for img_name in os.listdir("./Annotations/"):
	print(img_name)
	t=open("./Annotations/"+img_name,'r')
	lines=t.readlines()
	d={}
	color={}
	img_name=img_name.split('.')
	img=cv2.imread("./JPEGImages/"+img_name[0]+".jpg")
	for i,line in enumerate(lines):
		line=line.strip()
		#print(line)
		line=line.split('>')
		#print(line[0])
		if line[0]=="<object":
			nm=lines[i+1].strip()[6:].split("<")[0]
			if nm in d:
				d[nm]+=1
			else:
				d[nm]=1
			#print(lines[i+6].strip())
			x1=int(lines[i+6].strip()[6:].split("<")[0])
			y1=int(lines[i+7].strip()[6:].split("<")[0])
			x2=int(lines[i+8].strip()[6:].split("<")[0])
			y2=int(lines[i+9].strip()[6:].split("<")[0])
			r,g,b=getRGB(img,y1,y2,x1,x2)
			if nm in color:
				color[nm].append((r,g,b,x1,y1,x2,y2))
			else:
				color[nm]=[(r,g,b,x1,y1,x2,y2)]
	occ="("
	cc=[]
	for cw in class_words:
		if cw in d:
			occ+=str(d[cw])+","
			cc.append(color[cw])
		else:
			occ+='0,'
	occ=occ[:-1]+')'
	f.write(img_name[0]+".jpg\t"+occ+'\t')
	for c in cc:
		f.write(str(c)+' ')
	f.write('\n')
