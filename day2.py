import numpy as np
import copy
if __name__ == '__main__':
    path_input_txt = r"C:\Workspace\adventofcode\day2.txt"
    array = np.loadtxt(path_input_txt,dtype=str)
    my_shape =copy.deepcopy(array[:,1])

    lst_scores = [['A', 'X',3],['A','Y',6],['A','Z',0],['B','X',0],['B','Y',3],['B','Z',6],['C','X',6],
                  ['C','Y',0,],['C','Z',3]]
    lst_scores2 = [['A', 'X', 0], ['A', 'Y', 3], ['A', 'Z', 6], ['B', 'X', 0], ['B', 'Y', 3], ['B', 'Z', 6],
                  ['C', 'X', 0],
                  ['C', 'Y', 3, ], ['C', 'Z', 6]]
    dict_scores = {1:'X',2:'Y',3:'Z'}

    vect = np.zeros(array.shape[0])
    vect2 = np.zeros(array.shape[0])
    new_vect_my_shape = []

    for score in lst_scores:
        key = [score[0],score[1]]
        val = score[2]
        vect += (array==key).all(axis=1)*val

    for score in lst_scores2:
        key = [score[0],score[1]]
        val = score[2]
        vect2 += (array==key).all(axis=1)*val
        count_non_zero = np.count_nonzero((array==key).all(axis=1))
        if val == 0: # lose
            if score[0] == 'A':
                new_vect_my_shape.extend(['Z']*count_non_zero)
            elif score[0] == 'B':
                new_vect_my_shape.extend(['X']*count_non_zero)

            elif score[0] == 'C':
                new_vect_my_shape.extend(['Y']*count_non_zero)
        elif val == 3: # draw
            if score[0] == 'A':
                new_vect_my_shape.extend(['X']*count_non_zero)
            elif score[0] == 'B':
                new_vect_my_shape.extend(['Y']*count_non_zero)
            elif score[0] == 'C':
                new_vect_my_shape.extend(['Z']*count_non_zero)
        elif val == 6: # win
            if score[0] == 'A':
                new_vect_my_shape.extend(['Y']*count_non_zero)
            elif score[0] == 'B':
                new_vect_my_shape.extend(['Z']*count_non_zero)
            elif score[0] == 'C':
                new_vect_my_shape.extend(['X']*count_non_zero)
    my_shape[my_shape=='X']=1
    my_shape[my_shape=='Y']=2
    my_shape[my_shape=='Z']=3
    my_shape = (my_shape).astype(int)
    print(sum(vect+my_shape))

    new_vect_my_shape = np.array(new_vect_my_shape)
    new_vect_my_shape[new_vect_my_shape=='X']=1
    new_vect_my_shape[new_vect_my_shape=='Y']=2
    new_vect_my_shape[new_vect_my_shape=='Z']=3
    new_vect_my_shape = new_vect_my_shape.astype(int)

    print( sum(vect2+new_vect_my_shape))
