def func(a,n):
    i=0
    j=n-1
    while i<=j:
        if a[i]>0 and a[j]<0 :
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        elif a[i]>=0:
            i+=1
        elif a[j]<=0:
            j-=1
    return a

if __name__ == "__main__":
    a = [2,3,-4,-1,6,9]

    print(func(a,7))
