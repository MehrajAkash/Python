

def functionn(m):
    if(m<1) and (m>7): return

    functionn(m-1)
    print(m)
    functionn(m+1)

    return m 

print("hello11")
functionn(5)