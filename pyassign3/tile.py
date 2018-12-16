###Assign3

###chengnuo,1800011785
###2018.12.15
"""Module for tile work

This module provides all the ways to pave a wall of given length and
width with bricks of given length and width.It can also draw the way
you choose."""
if __name__=='__main__':
    wall=input('请输入墙的大小(长*宽)')
    A,B=int(wall.split('*')[0]),int(wall.split('*')[1])

    brick=input('请输入砖的大小(长*宽)')
    a,b=int(brick.split('*')[0]),int(brick.split('*')[1])

    AA=[0]*(A*B)

    def allcoor(x,y):
        allcoors=[]
        for j in range(b):
            for k in range(a):
                allcoors.append((x+k,y+j))
        return(allcoors)

    def tonum(t):
        for l in range(len(t)):
            x,y=t[l][0],t[l][1]
            t[l]=(x+y*A)
        return tuple(t)

    def tocoor(i):
        return((i%A,i//A))

    def judge(p):
        if p%A+a>A or p//A+b>B or p==A*B+1:
            return False
        for i in range(b):
            for j in AA[p+i*A:p+i*A+a]:
                if j == 1:
                    return False
        else:
            return True

    def tile(n=0):
        global a,b,A,B
        ans=[]
        while AA[n]==1:
            n+=1
            if n==A*B:
                return [[]]
        for (a, b) in [(a, b), (b, a)]:
            if judge(n):
                bricks=tonum(allcoor(tocoor(n)[0],tocoor(n)[1]))
                for p in bricks:
                    AA[p]=1
                bb = tile(n)
                for cc in bb:
                    cc.append(bricks)
                ans.extend(bb)
                for p in bricks:
                    AA[p]=0
        return ans

    def output():
        k=list(set([tuple(p) for p in tile()]))
        j=[0]*len(k)
        for t in k:
            j[k.index(t)]=list(t)
        return(j)

    for i in output():
        print(i)

    c=int(input('输入要画出的方法(从0到'+str(len(output()))+')'))
    import turtle
    wn=turtle.Screen()
    p=turtle.Pen()
    wn.setworldcoordinates(0,0,A,B)
    p.speed(0)
    p.pensize(1)
    for u in range(A*B):
        p.up()
        p.goto(tocoor(u)[0]+0.5,tocoor(u)[1]+0.5)
        p.write(u)
        p.goto(tocoor(u))
        p.down()
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
    p.pensize(5)
    for i in output()[c]:
        p.up()
        p.goto(tocoor(min(i)))
        p.down()
        a,b=int(brick.split('*')[0]),int(brick.split('*')[1])
        if max(i)-min(i)==a*b-1:
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
        else:
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
