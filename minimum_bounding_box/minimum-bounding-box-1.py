def min_max(arr, start, end, index):
    if start==end-1:
        return arr[start][index], arr[end-1][index]
    if start==end-2:
        if arr[start][index]>arr[end-1][index]:
            return arr[end-1][index], arr[start][index]
        else:
            return arr[start][index], arr[end-1][index]
    mid=(start+end)//2
    min_max1=min_max(arr, start, mid, index)
    min_max2=min_max(arr, mid, end, index)
    if min_max1[0]<min_max2[0]:
        minimum=min_max1[0]
    else:
        minimum=min_max2[0]
    if min_max1[1]>min_max2[1]:
        maximum=min_max1[1]
    else:
        maximum=min_max2[1]
    return minimum,maximum
n=int(input("Enter count of vertices: "))
vertices=[]
for i in range(n):
    vertices.append(list(map(int,input("Enter coordinates of vertex #{}: ".format(i+1)).split())))
minx, maxx = min_max(vertices, 0, n, 0)
miny, maxy = min_max(vertices, 0, n, 1)
print("The minimum bounding box is:")
print("x =", minx)
print("x =", maxx)
print("y =", miny)
print("y =", maxy)
