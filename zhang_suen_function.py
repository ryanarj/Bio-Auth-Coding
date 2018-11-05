from utilities_function import utilities

'''
Implementation of the Zhang Suen Algorithm
'''


def zhang_suen(image):
    '''
    Fill in the missing code here to complete the Zhang Suen Algorithm.
    This should entail making the necessary checks in parts
    1 and 2 of the algorithm.  If pixels are changed, use
    variables step1 and step2 as flags; if step1 is one,
    at least one pixel was changed during step1 (likewise for step2).
    Hence, if either step1 or step2 are 1, the algorithm will continue
    in the while loop. It will only stop once step1 and step2 remain 0.
    Be sure to perform your checks on thinned_img. You can use the imported
    utilities function to compute A(P1), B(P1), and find a pixel's neighbors.
    This function returns all three items.
    '''
    thinned_img = image.copy()
    step1 = step2 = 1
    while step1 or step2:
        step1 = step2 = 0
        rows, columns = thinned_img.shape
        changing1 = []
        for x in range(1, rows-1):
            for y in range(1, columns-1):
                ap1, bp1, neighbors = utilities(x, y, thinned_img)
                if thinned_img[x][y] == 1 and 2 <= bp1 <= 6 and ap1 == 1:
                    changing1.append((x, y))
        for x, y in changing1:
            thinned_img[x][y] = 0

        changing2 = []
        for x in range(1, rows-1):
            for y in range(1, columns-1):
                ap1, bp1, neighbors = utilities(x, y, thinned_img)
                if thinned_img[x][y] == 1 and 2 <= bp1 <= 6 and ap1 == 1:
                    changing2.append((x, y))
        for x, y in changing2:
            thinned_img[x][y] = 0
    
    return thinned_img