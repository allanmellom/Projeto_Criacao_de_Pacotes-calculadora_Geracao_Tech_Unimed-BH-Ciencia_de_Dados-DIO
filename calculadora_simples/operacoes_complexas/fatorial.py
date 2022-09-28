def fatorial(x):
    y=1
    for i in range(x+1):
        if i==0:
            continue
        y*=i
    return y