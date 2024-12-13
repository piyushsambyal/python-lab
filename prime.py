count = 0
def check(i):
    
    if i<=1:
        count=0
    else:
        for k in  range(1,i+1):
            if(i%k==0):
                count=count+1
    return count

def prime(li):
    for i in li:
        x=check(i)
        if(x!=0):
            print(i)


li=[1,2,3,40,50,60,87,27,9,3]
print(prime(li))


