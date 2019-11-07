# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:17:09 2019

@author: TaiT_
"""

class BBNode(object): # save this in a file BBNode.py
    def __init__(self, parent, dv, boundSense, bound):
        # instance variables
        self.parent = parent
        self.dv = dv
        self.boundSense = boundSense
        self.bound = bound
    def set_obj(self, obj):
        self.obj = obj
    def set_dvSol(self, dvSol):
        self.dvSol = dvSol
    def set_status(self, status):
        self.status = status
