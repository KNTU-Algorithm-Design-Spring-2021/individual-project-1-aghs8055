def max_min(num1, num2):
    if num1>num2:
        return (num2, num1)
    else:
        return (num1, num2)
n=int(input("Enter count of vertices: "))
vertices=[]
for i in range(n):
    vertices.append(list(map(int,input("Enter coordinates of vertex #{}: ".format(i+1)).split())))
minx, maxx = max_min(vertices[0][0], vertices[1][0])
miny, maxy = max_min(vertices[0][1], vertices[1][1])
for i in range(n//2-1):
    tempx=max_min(vertices[2*i+2][0],vertices[2*i+3][0])
    tempy=max_min(vertices[2*i+2][1],vertices[2*i+3][1])
    maxx=max_min(tempx[1],maxx)[1]
    minx=max_min(tempx[0],minx)[0]
    maxy=max_min(tempy[1],maxy)[1]
    miny=max_min(tempy[0],miny)[0]
if n%2==1:
    maxx=max_min(vertices[n-1][0], maxx)[1]
    minx=max_min(vertices[n-1][0], minx)[0]
    maxy=max_min(vertices[n-1][1], maxy)[1]
    miny=max_min(vertices[n-1][0], miny)[0]
print("The minimum bounding box is:")
print("x =", minx)
print("x =", maxx)
print("y =", miny)
print("y =", maxy)
