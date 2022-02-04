# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 12:56:00 2022
@author: eiproject
"""

class DegreeGLRLM:
    def __init__(self, mat_0, mat_45, mat_90, mat_135):
        self.__title__ = "Degree Object for GLRLM"
        self.Mat_0 = mat_0 
        self.Mat_45 = mat_45
        self.Mat_90 = mat_90
        self.Mat_135 = mat_135
        self.Degrees = [mat_0, mat_45, mat_90, mat_135]
        
        
class FeatureGLRLM:
    def __init__(self, sre, lre, glu, rlu, rpc):
        self.__title__ = "Feature Object from GLRLM"
        self.SRE = sre
        self.LRE = lre
        self.GLU = glu
        self.RLU = rlu
        self.RPC = rpc
        self.Features = [sre, lre, glu, rlu, rpc]
        