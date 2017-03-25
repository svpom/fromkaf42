#!/usr/bin/python3
import copy
import sys


def clip_met():
    tmp_matr = copy.deepcopy(matrix)
    tmp_size = size
    vert = []

    for i in range(0, size):  # array with vertex's number. [0,1,2,3,..,size-1]
        vert.append(i)

    while tmp_size > 2:  # if tmp_size ==1 then we have found vertex. if tmp_size ==2, 2 vertexes and it needs to do more
        tmp_del_lst = []
        new_index = 0
        for i in range(0, tmp_size):
            sum = 0
            for j in range(0, tmp_size):
                sum += tmp_matr[i][j]
            if sum == 1:
                tmp_del_lst.append(i)  # find new vertexes

        for i in reversed(tmp_del_lst):  # delete used vertexes
            vert.pop(i)

        for i in reversed(range(0, tmp_size)):  # delete used lines and columns
            for k in reversed(tmp_del_lst):
                tmp_matr[i].pop(k)
        for k in reversed(tmp_del_lst):
            tmp_matr.pop(k)

        tmp_size = tmp_size - len(tmp_del_lst)  # change the size of the matrix until it become 1 or 2

    if tmp_size == 1:  # if we have got center
        print('The root is the vertex number ', vert[0] + 1)

    if tmp_size == 2:  # if we have got bi-roots
        x1 = vert[0]
        x2 = vert[1]

        path1 = 0
        used_el = [x1, x2]
        start = [x1]
        while True:
            if len(start) == 0:  # if all vertexes were used
                paths_x1 = [path1, size - 1 - path1]
                break
            for k in start:
                if len(start) != 0:
                    for i in range(0, size):
                        elem = matrix[k][i]
                        if elem == 1 and not i in used_el:  # each this i is a new vertex
                            used_el.append(i)
                            path1 += 1
                            start.append(i)
                start.pop(0)  # delete used vertexes

        path2 = 0
        used_el = [x1, x2]
        start = [x2]
        while True:
            if len(start) == 0:
                paths_x2 = [path2, size - 1 - path2]
                break
            for k in start:
                if len(start) != 0:
                    for i in range(0, size):
                        elem = matrix[k][i]
                        if elem == 1 and not i in used_el:
                            used_el.append(i)
                            path2 += 1
                            start.append(i)
                start.pop(0)

        if min(paths_x1) <= min(paths_x2):
            print('The root is the vertex number ', vert[0] + 1)
        else:
            print('The root is the vertex number ', vert[1] + 1)


def height_met():
    '''path = 0
    used_el = [x1, x2]
    start = [x2]'''
    paths = []
    for i in range(0, size):
        branches = []
        paths_i = []
        for j in range(0, size):
            if matrix[i][j] == 1:
                branches.append(j)  # find all branches for vertex number i
        for b in branches:  # find path for each vertex, which connects with vertex number i. Don't forget to sum all paths and add 1
            path = 0
            used_el = [i, b]
            start = [b]
            while True:
                if len(start) == 0:
                    paths_i.append(path)
                    break
                for k in start:
                    if len(start) != 0:
                        for z in range(0, size):
                            elem = matrix[k][z]
                            if elem == 1 and not z in used_el:
                                used_el.append(z)
                                path += 1
                                start.append(z)
                    start.pop(0)
        paths.append(max(paths_i))
    print("The root is the vertex number ", paths.index(min(paths)) + 1)


def main():
    while True:
        task_num = int(input("Enter 1 for clipping method or 2 for method based on height or 3 for exit:\n"))
        if task_num == 3:
            sys.exit(0)
        global matrix
        matrix = []
        global size
        size = int(input("Enter the size of adjacency matrix: \n"))
        print("Enter the elements of the matrix using backspaces and enter(e.g. \n1 2 3 \n4 5 6\n7 8 9):")
        for i in range(0, size):
            matrix.append(input().split(' '))

        for i in range(0, size):
            for j in range(0, size):
                matrix[i][j] = int(matrix[i][j])  # end of the matrix initialization

        if task_num == 1:
            clip_met()
        if task_num == 2:
            height_met()

if __name__ == '__main__':
    main()
