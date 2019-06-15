
def comb(n,k):
   
    
    def fac(x):
        x=range(1,x+1)
        factor=1
        for item in x:
            factor=item*factor
            pass
        return factor
    m= fac(n)
    return int(fac(n)/(fac(k)*fac(n-k)))


print(comb(10,0))