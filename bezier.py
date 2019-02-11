import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
im = Image.new("RGB", (640,480))
draw = ID.Draw(im)
points1=[[100,160],[100,100],[400,100],[400,160]]
points2=[[100,160],[100,220],[400,220],[400,160]]
points3=[[100,160],[250,160],[250,280],[100,280]]
points4=[[400,280],[250,280],[250,160],[400,160]]
points5=[[100,280],[100,400],[400,400],[400,280]]
M=[[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]]
coord=list();
def Multiply(t,points):
	#print(points)
	P1=list()
	tMat=[(t*t*t),(t*t),t,1]
	for i in range(0,4):
		temp=0
		for j in range(0,4):
			temp=temp+tMat[j]*M[i][j]
			#print(temp);
		P1.append(temp)
	for i in range(0,2):
		temp=0
		for j in range(0,4):
			temp=temp+P1[j]*points[j][i]
		coord.append(int(temp))	
def matka(points):
	global coord;
	t=0
	i = 0
	while(t < 1):
		Multiply(t,points)
		im.putpixel((coord[i], coord[i + 1]), (255,255,255))
		i += 2
		t += 0.001
	coord=list()		
matka(points1)
matka(points2)
matka(points3)
matka(points4)
matka(points5)
im.show()
