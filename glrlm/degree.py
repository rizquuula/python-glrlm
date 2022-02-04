# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 12:56:00 2022
@author: eiproject
"""

from .model import DegreeGLRLM
import numpy

class Degree:
    """
    GLRLM degree operations for 0, 45, 90, and 135 degree
    """
    def __init__(self):
        self.__title__ = "GLRLM"
        self.__image_src = None
        self.__gray_level = None
        self.__run_length = None
        
    def __degree0GLRLM(self):
        degree0Matrix = numpy.zeros([self.__gray_level, self.__run_length])
        counter = 0
        for y in range(self.__image_src.shape[0]):
            for x in range(self.__image_src.shape[1]):
                # print('coordinate ',y,x)
                nowVal = self.__image_src[y][x]
                if x + 1 >= self.__image_src.shape[1]:
                    nextVal = None
                else:
                    nextVal = self.__image_src[y][x + 1]

                if nextVal != nowVal and counter == 0:
                    # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                    degree0Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree0Matrix[int(nowVal)][counter] += 1
                    counter = 0
                    # print(y, " val,counter 3 |",nowVal, nextVal, counter)
        # print()
        # print("Gray Level Run Length Matrix degree 0")
        return degree0Matrix

    def __degree90GLRLM(self):
        degree90Matrix = numpy.zeros([self.__gray_level, self.__run_length])
        counter = 0
        for x in range(self.__image_src.shape[1]):
            for y in range(self.__image_src.shape[0]):
                nowVal = self.__image_src[y][x]
                if y + 1 >= self.__image_src.shape[0]:
                    nextVal = None
                else:
                    nextVal = self.__image_src[y + 1][x]

                if nextVal != nowVal and counter == 0:
                    # print(x, " val,counter 1 |",nowVal, nextVal, counter)
                    degree90Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(x, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree90Matrix[int(nowVal)][counter] += 1
                    counter = 0

        # print()
        # print("Gray Level Run Length Matrix degree 90")
        return degree90Matrix

    def __degree45GLRLM(self):
        degree45Matrix = numpy.zeros([self.__gray_level, self.__run_length])

        for y in range(self.__image_src.shape[0]):
            # print()
            counter = 0
            i_range = max(self.__image_src.shape)
            for i in range(i_range):
                y1 = y - i
                if i >= self.__image_src.shape[1] or y1 < 0:
                    break
                else:
                    nowVal = self.__image_src[y1][i]
                # print(y1, i)
                if y1 - 1 < 0 or i + 1 >= self.__image_src.shape[1]:
                    nextVal = None
                else:
                    nextVal = self.__image_src[y1 - 1][i + 1]
                # print(y1, i , ' and ', nowVal, nextVal)
                # print(y1,i , ' and ', self.imageSrc[y1][i])
                if nextVal != nowVal and counter == 0:
                    # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                    degree45Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree45Matrix[int(nowVal)][counter] += 1
                    counter = 0
                    # print(y, " val,counter 3 |",nowVal, nextVal, counter)

        for x in range(self.__image_src.shape[1]):
            if x == self.__image_src.shape[1] - 1:
                break
            # print()
            counter = 0
            i_range = max(self.__image_src.shape)
            for i in range(i_range):
                y_i = -1 - i
                x_i = -1 + i - x
                # print(y_i, x_i)
                if x_i >= 0 or y_i <= -1 - self.__image_src.shape[0]:
                    break
                else:
                    nowVal = self.__image_src[y_i][x_i]

                if y_i - 1 <= -(self.__image_src.shape[0] + 1) or x_i + 1 >= 0:
                    nextVal = None
                else:
                    nextVal = self.__image_src[y_i - 1][x_i + 1]

                # print(y_i,x_i, ' and ', nowVal, nextVal)
                if nextVal != nowVal and counter == 0:
                    # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                    degree45Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree45Matrix[int(nowVal)][counter] += 1
                    counter = 0
                    # print(y, " val,counter 3 |",nowVal, nextVal, counter)

        # print()
        # print("Gray Level Run Length Matrix degree 45")
        return degree45Matrix

    def __degree135GLRLM(self):
        degree135Matrix = numpy.zeros([self.__gray_level, self.__run_length])

        for y in range(self.__image_src.shape[0]):
            # print()
            counter = 0
            i_range = max(self.__image_src.shape)
            for i in range(i_range):
                y1 = y + i
                if y1 >= self.__image_src.shape[0] or i >= self.__image_src.shape[1]:
                    # print('Break in coordinate = ', y1, i)
                    break
                else:
                    nowVal = self.__image_src[y1][i]
                    # print(nowVal)
                    if y1 >= self.__image_src.shape[0] - 1 or i >= self.__image_src.shape[1] - 1:
                        nextVal = None
                    else:
                        nextVal = self.__image_src[y1 + 1][i + 1]
                    # print('First step', nowVal, nextVal)
                    if nextVal != nowVal and counter == 0:
                        # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                        degree135Matrix[int(nowVal)][counter] += 1
                    elif nextVal == nowVal:
                        counter += 1
                        # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                    elif nextVal != nowVal and counter != 0:
                        degree135Matrix[int(nowVal)][counter] += 1
                        counter = 0
                        # print(y, " val,counter 3 |",nowVal, nextVal, counter)

        for x in range(self.__image_src.shape[1]):
            if x == 0:
                continue
            # print()
            i_range = max(self.__image_src.shape)
            counter = 0
            for i in range(i_range):
                x1 = x + i
                if i >= self.__image_src.shape[0] or x1 >= self.__image_src.shape[1]:
                    # print('Break in coordinate = ',i,x)
                    break
                else:
                    nowVal = self.__image_src[i][x1]
                    # print(nowVal)
                if i >= self.__image_src.shape[0] - 1 or x1 >= self.__image_src.shape[1] - 1:
                    nextVal = None
                else:
                    nextVal = self.__image_src[i + 1][x1 + 1]
                # print('Second step', nowVal, nextVal)
                if nextVal != nowVal and counter == 0:
                    # print(y, " val,counter 1 |",nowVal, nextVal, counter)
                    degree135Matrix[int(nowVal)][counter] += 1
                elif nextVal == nowVal:
                    counter += 1
                    # print(y, " val,counter 2 |",nowVal, nextVal, counter)
                elif nextVal != nowVal and counter != 0:
                    degree135Matrix[int(nowVal)][counter] += 1
                    counter = 0
                    # print(y, " val,counter 3 |",nowVal, nextVal, counter)

        # print()
        # print("Gray Level Run Length Matrix degree 135")
        return degree135Matrix

    
    def create_matrix(self, normalized_img, level):
        """
        Create degree matrix for GLRLM
        Return:
            Array of degree
        """
        self.__image_src = normalized_img
        self.__gray_level = level
        self.__run_length = max(normalized_img.shape)
        
        mat0 = self.__degree0GLRLM()
        mat45 = self.__degree45GLRLM()
        mat90 = self.__degree90GLRLM()
        mat135 = self.__degree135GLRLM()
        
        return DegreeGLRLM(mat0, mat45, mat90, mat135)