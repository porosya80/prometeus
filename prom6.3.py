def saddle_point(matrix):
    matrix2 = list(zip(*matrix))
    coords = False
    # print("\n".join([" ".join(str(x)) for x in matrix]))
    # print("\n".join([" ".join(str(x)) for x in matrix2]))
    for i, row in enumerate(matrix):
        for j, ch in  enumerate(row):
            if ch == min(row) and row.count(ch) == 1  and ch == max(matrix2[j]) and  matrix2[j].count(ch)==1:
                coords = (i,j)
    return coords


#
# print(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]))
# print(saddle_point(([[1,2,3],[3,2,1]])))
# print(saddle_point([[21]]))
print(saddle_point([[13]]))
print(saddle_point([[0,0,0],[2,1,2],[1,0,1]]))
print(saddle_point([[5,5,5], [5,5,6], [5,4,5]]) )
print(saddle_point([[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]]) )
print(saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]))