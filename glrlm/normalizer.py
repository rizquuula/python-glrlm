# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 12:56:00 2022
@author: eiproject
"""

class Normalizer:
    """Perform image pixel normalization"""
    def __init__(self):
        super()

    def __normalization(self, value, min=0, max=255, newmin=0, newmax=10):
        newValue = (value-min)*((newmax-1-newmin)/(max-min))-newmin
        return newValue

    def normalizationImage(self, image=None, minScale=0, maxScale=9):
        for x in range(image.shape[1]):
            for y in range(image.shape[0]):
                image[y][x] = round(
                    self.__normalization(value=image[y][x],
                                    newmin=minScale,
                                    newmax=maxScale,
                                    ))
        return image
            
