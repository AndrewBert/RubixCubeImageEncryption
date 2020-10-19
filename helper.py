import numpy as np

def upshift(a,index,n):
    #upshift column 
    a[:, index] = np.roll(a[:,index],-n)

def downshift(a,index,n):
    #downshift column 
    a[:, index] = np.roll(a[:,index],n)

def rotate180(n):
    bits = "{0:b}".format(n)
    return int(bits[::-1], 2)
