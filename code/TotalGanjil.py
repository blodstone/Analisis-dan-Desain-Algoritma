def totalGanjil(A,p,r):
    if p<r:
        q = (p+r)//2
        x = totalGanjil(A,p,q)
        y = totalGanjil(A,q+1,r)
        return total(x,y)
    else:
        if A[r]%2!=0:
            return 1
        else:
            return 0

def total(x,y):
    return x+y

A = [3,1,2,7,6,5,3]
print(totalGanjil(A,0,len(A)-1))

