def dist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5
def closest_dist(points, start, end):
    if end-start<=3:
        c=float("inf")
        for i in range(start, end):
            for j in range(i+1, end):
                if dist(points[i], points[j])<c:
                    c=dist(points[i], points[j])
        return c
    mid=(end+start)//2
    c1=closest_dist(points, start, mid)
    c2=closest_dist(points, mid, end)
    c=min(c1,c2)
    mid_points=[]
    for i in range(start, end):
        if (points[i][0]-points[mid][0])**2+(points[i][2]-points[mid][2])**2<c*c:
            mid_points.append(points[i])
    mp_size=len(mid_points)
    mid_points.sort(key=lambda x:x[1])
    for i in range(mp_size):
        j=i+1
        while j<mp_size and mid_points[j][1]-mid_points[i][1]<c:
            c=min(c,dist(mid_points[i], mid_points[j]))
            j+=1
    return c
n=int(input("Enter count of points: "))
print("Enter coordinates of each points in form \"x y z\":")
points=[]
for i in range(n):
    points.append(list(map(int,input("Point #{}:".format(i+1)).split())))
points.sort(key=lambda x:x[0])
print("Closest distance is: {}".format(closest_dist(points, 0, n)))
