# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 12:56:00 2022
@author: eiproject
"""

from .model import DegreeGLRLM, FeatureGLRLM 

class Operator:
    """
    GLRLM Operator for SRE, LRE, GLU, RLU, RPC
    """
    def __init__(self):
        self.title = "GLRLM Operator"
        self.__degree_obj:DegreeGLRLM = None

    def __SRE(self):
        input_matrix = self.__degree_obj.Degrees
        matSRE = []
        for input_matrix in input_matrix:
            S = 0
            SRE = 0
            for x in range(input_matrix.shape[1]):
                for y in range(input_matrix.shape[0]):
                    S += input_matrix[y][x]

            for x in range(input_matrix.shape[1]):
                Rj = 0
                for y in range(input_matrix.shape[0]):
                    Rj += input_matrix[y][x]

                SRE += (Rj/S)/((x+1)**2)
                # print('( ',Rj,'/',S,' ) / ',(x+1)**2)
            SRE = round(SRE, 3)
            matSRE.append(SRE)

        # print('Perhitungan SRE')
        return round(sum(matSRE),3)


    def __LRE(self):
        input_matrix = self.__degree_obj.Degrees
        matLRE = []
        for input_matrix in input_matrix:
            S = 0
            LRE = 0
            for x in range(input_matrix.shape[1]):
                for y in range(input_matrix.shape[0]):
                    S += input_matrix[y][x]

            for x in range(input_matrix.shape[1]):
                Rj = 0
                for y in range(input_matrix.shape[0]):
                    Rj += input_matrix[y][x]

                LRE += (Rj * ((x + 1) ** 2)) / S
                # print('( ', Rj ,' * ',((x + 1) ** 2), ' ) /', S)
            LRE = round(LRE, 3)
            matLRE.append(LRE)
        # print('Perhitungan LRE')
        return round(sum(matLRE),3)


    def __GLU(self):
        input_matrix = self.__degree_obj.Degrees
        matGLU = []
        for input_matrix in input_matrix:
            S = 0
            GLU = 0
            for x in range(input_matrix.shape[1]):
                for y in range(input_matrix.shape[0]):
                    S += input_matrix[y][x]

            for x in range(input_matrix.shape[1]):
                Rj = 0
                for y in range(input_matrix.shape[0]):
                    Rj += input_matrix[y][x]

                GLU += ((x + 1) ** 2) / S
                # print('( ',((x + 1) ** 2), ' ) /', S)
            GLU = round(GLU, 3)
            matGLU.append(GLU)
        # print('Perhitungan GLU')
        return round(sum(matGLU),3)


    def __RLU(self):
        input_matrix = self.__degree_obj.Degrees
        matRLU = []
        for input_matrix in input_matrix:
            S = 0
            RLU = 0
            for x in range(input_matrix.shape[1]):
                for y in range(input_matrix.shape[0]):
                    S += input_matrix[y][x]

            for x in range(input_matrix.shape[1]):
                Rj = 0
                for y in range(input_matrix.shape[0]):
                    Rj += input_matrix[y][x]

                RLU += (Rj ** 2) / S
                # print('( ', (Rj ** 2), ' ) /', S)
            RLU = round(RLU, 3)
            matRLU.append(RLU)
        # print('Perhitungan RLU')
        return round(sum(matRLU),3)


    def __RPC(self):
        input_matrix = self.__degree_obj.Degrees
        matRPC = []
        for input_matrix in input_matrix:
            S = 0
            RPC = 0
            for x in range(input_matrix.shape[1]):
                for y in range(input_matrix.shape[0]):
                    S += input_matrix[y][x]

            for x in range(input_matrix.shape[1]):
                Rj = 0
                for y in range(input_matrix.shape[0]):
                    Rj += input_matrix[y][x]

                RPC += (Rj) / (input_matrix.shape[0]*input_matrix.shape[1])
                # print('( ', (Rj), ' ) /', input_matrix.shape[0]*input_matrix.shape[1])
            RPC = round(RPC, 3)
            matRPC.append(RPC)
        # print('Perhitungan RPC')
        return round(sum(matRPC),3)
    
    def create_feature(self, degree:DegreeGLRLM):
        self.__degree_obj = degree
        return FeatureGLRLM(
            self.__SRE(), 
            self.__LRE(), 
            self.__GLU(), 
            self.__RLU(), 
            self.__RPC())
    