#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:52:54 2020

@author: sandesh
"""


def DNAtoRNA(string):
    
    string = string.replace('T', 'U')
    print(string)

string = "TTCCTGTTGATTGATAACCGTCCAGGCTATGGTTTAACTGTTCGTGTTCGGGGGGATGCCATAAATTGCTGAAACCCTGCAATAATTGTATCCGAAGCCGTACGTTACAAGGGATGCCATAGCGGTAGTGACACCCACCCGAACGAATCATCAGATTGTGTATCGGTGAGCTAACTAGTAGCCCCGGATCCGCCCATACACGTCGGAGATAAGAAGATCTAATCACTTCAGCGTCGGGTTAAAAACAAAGCCCCAATGAGTGGCAGCTGTACTGTAACGTGGCAACCAGTCTATACCCAGGTGTGACGCGGGACCGTGGGGTGTAATATCTGGCTAACCACGGGCCCCACCATAGAAGGAGTAACGCGCTCATCGTGAAGTTATCTGGACTCATTGTCGGATTTCAGGCCGGACCTAAATTTGATATGGAGTTGATCGGCTGTCGGACATACCTTCATGGGCAGTCGATATGAGCGGATATGGAGCGATACTCTGGCGCAGCGCGGTTTTAGTTATCTAATAGACGCACGAATACGGACATCATATCCAAAAACTTGTAGGGTCTCAATAAGGGTGTCATATTCTGGGCACCCTCATGCTGGCGTTCTGGCGTTCCACTTGGCTTTCAATATCCTCATATAAGTGCTTAACGCCTCAGGGGATGGCCGTGGTCGTCATTAAGAGTCGGATCTTTGATTGTTGCCTACGGCCCGACAGATCGTTGGTTGGGCGTCCGAGGCAAGTTAGGTCGTATTGAAAACGTCAGGGGATCGCCGCAAATCCTCGCGTGGGCTGCGTGTCGTATGCAATTTTCGGCTAAGTAACAGGCTCTTTCCTCGTAATCAGGGAGCCGATCGCTTAGAGATAATTCATACTAATAGGTCCGTCTGCTTATCGCCGGAG"
DNAtoRNA(string)