# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 12:56:00 2022
@author: eiproject
"""

from .operator import Operator
from .degree import Degree
from .normalizer import Normalizer

import cv2

class GLRLM:
    """
    Gray Level Run Length Matrix
    
    Feature extraction technique in image processing
    @author: M Razif Rizqullah | https://github.com/eiproject
    """
    def __init__(self):
        self.__title__ = "GLRLM"
        self.__normalizer = Normalizer()
        self.__degree = Degree()
        self.__operator = Operator()
        
        
    def __check_and_convert_to_gray(self, image):
        if len(image.shape) != 2:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image
        
        
    def get_features(self, image, level=8):
        """[summary]

        Args:
            image (array): Open CV image array
            level (int, optional): Pixel normalization level. Defaults to 8.

        Returns:
            FeatureGLRLM: Feature extraction result from GLRLM
            - SRE = Short Run Emphasis
            - LRE = Long Run Emphasis
            - GLU = Grey Level Uniformity
            - RLU = Run Length Uniformity
            - RPC = Run Percentage
        """
        grayscale_image = self.__check_and_convert_to_gray(image)
        normalized_image = self.__normalizer.normalizationImage(grayscale_image, 0, level)
        degree_obj = self.__degree.create_matrix(normalized_image, level)
        feature_obj = self.__operator.create_feature(degree_obj)
        return feature_obj