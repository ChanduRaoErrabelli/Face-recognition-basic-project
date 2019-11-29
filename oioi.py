import cv2

img=cv2.imread('download.jpg',0)


cv2.imshow('gray_image',img)
cv2.waitKey(0)
ret, bi=cv2.threshold(img,110,255,cv2.THRESH_BINARY)
cv2.imshow('binary_image',bi)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
h,w=img.shape
for i in range(h):
    for j in range(w):
        px=bi[i,j]
        c=px
        if(px==0):
            x=i
            y=j

            print(i,j)

            break;
    if(c==0):
         break;
print(x,y)
for n in range(y):
    for m in range(x+1,h-1):
        px1=bi[m,n]
        c1=px1
        if(px1==0):
            x1=m
            y1=n
            print(m,n)
            break;
    if(c1==0):
        break;
print(x1,y1)
for l in range(w-1,y1,-1):
    for k in range(x+1,h-1):
        px2=bi[k,l]
        c2=px2
        if(px2==0):
            x2=k
            y2=l
            print(k,l)
            break;
    if(c2==0):
        break;
print(x2,y2)
for i in range(x,h):
    px3=bi[i,y]
    c3=px3
    if(px3==255):
        x3=i
        y3=y
        print(i,y)
        break;
print(x3,y3)
for i in range(w):
    px4=bi[x3,i]
    c4=px4
    if(px4==0):
        x4=x3
        y4=i
        print(x3,i)
        break;
print(x4,y4)
for i in range(y4,w):
    px5=bi[x3,i]
    c5=px5
    if(px5==255):
        x5=x3
        y5=i
        print(x3,i)
        break;
for i in range(x5+1,265):
    px6=bi[i,y5]
    c6=px6
    if(px6==255):
        x6=i
        y6=y5
        print(i,y5)
        break;

cv2.imshow('gray_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()













