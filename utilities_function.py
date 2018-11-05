''' Utilities function to find a pixels neighbors, 
assign a value to A which indicates the number of transitions
in the neighbors from 0 to 1, and the sum of 
neighbors that are black (B). It returns A, B, and the neighbors
'''


def utilities(x, y, my_img):

    img = my_img
    P2 = img[x-1, y]
    P3 = img[x-1, y+1]
    P4 = img[x, y+1]
    P5 = img[x+1, y+1]
    P6 = img[x+1, y]
    P7 = img[x+1, y-1]
    P8 = img[x, y-1]
    P9 = img[x-1, y-1]
    neighbors = [P2, P3, P4, P5, P6, P7, P8, P9, P2]
    
    A_P1 = 0
    for i in range(len(neighbors)-1):
        if (neighbors[i] == 0) and (neighbors[i+1] == 1):
            A_P1 += 1
     
    neighbors = [P2, P3, P4, P5, P6, P7, P8, P9]
    B_P1 = sum(neighbors)
    
    return A_P1, B_P1, neighbors