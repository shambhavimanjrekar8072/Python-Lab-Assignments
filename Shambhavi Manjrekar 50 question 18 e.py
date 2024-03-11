
def geo_sum(a,r,n):
    if n == 0:
        return
    return a + geo_sum(a*r,r,n-1)
print(geo_sum(1,4,10))
