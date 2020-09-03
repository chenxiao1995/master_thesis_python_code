import sys
def fb(n):
    a,b=1,1
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        for i in range(2,n):
            ret=a+b
            a=b
            b=ret
        return ret

    # if n==1:
    #     return 1
    # elif n==2:
    #     return 1
    # else:
    #     return fb(n-1)+fb(n-2)

def creat_fb_array(n):
    array=[]
    for i in range(n*n,0,-1):
        array.append(fb(i))
    return array

if __name__=="__main__":
    while True:
        n = int(input())
        fb_array=creat_fb_array(n)
        A=[[0 for i in range(n)] for i in range(n)]
        x,y,count=0,0,0
        # while(count<n*n):
        #     # right
        A[x][y] = fb_array[count]
        while(count<n*n-1):
            while( y+1<=n-1 and A[x][y+1]==0 ):
                count += 1
                y+=1
                A[x][y]=fb_array[count]
            # down
            while( x+1<=n-1 and A[x+1][y]==0 ):
                count += 1
                x+=1
                A[x][y]=fb_array[count]
            # left
            while( y-1>=0 and A[x][y-1]==0 ):
                count += 1
                y-=1
                A[x][y]=fb_array[count]
            # up
            while( x-1>=0 and A[x-1][y]==0 ):
                count += 1
                x-=1
                A[x][y]=fb_array[count]

        for i in A:
            for j in i:
                sys.stdout.write(str(j)+" ")
            sys.stdout.write("\n")
