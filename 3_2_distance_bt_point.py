x1=int(input('Enter the x position of point 1:\n'))
y1=int(input('Enter the y position of point 1:\n'))


x2=int(input('Enter the x position of point 2:\n'))
y2=int(input('Enter the x position of point 2:\n'))
a=(x2-x1)**2
b=(y2-y1)**2
d=(a+b)**0.5
print('Distance between the points (',x1,',',y1,') and (',x2,',',y2,') is ',d)
