#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:53:39 2020

@author: sandesh
"""

def AAtoRNA(aminoacid):
    totalfrequency = frequencylist['STOP']
    for i in aminoacid: 
        totalfrequency = totalfrequency * frequencylist[i]
    
    answer = totalfrequency% 1000000
    print(answer)

rna_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

frequencylist = {}
for v in rna_table.values():
    if v not in frequencylist:
        frequencylist[v] = 1
    else: 
        frequencylist[v] += 1

aminoacid ="MSYYSYCAMYSSMGWHRWSGTLGYRFCFWLDPVANHSYVDPYFMALCYYLYDGEDCRNPDQAHPLTQMEMMMHHCHSIMINKQLSPWDLRSSCMRNKLFWKQTMPKARWWTEIIMNRGIHYWTSAIWDMMHDRCCSRIVVERWWLFPCGREYSKAREEGQNGEADMIFCHYYFEWNIGEPIPEFACIRVSLKCLTKVRCTKKCMAGPKDLPFSVWQSAAFYKYYWHVPLNKDVYFDPLDHSQMHRVETWSCEPWWFGKAIIMHIVDKLRPIMILGCMPMTCTNYGWGFMSIAIDRQGGWVWEYFYNWWMLFQISSWNYEATYIFDQLGEMYMMRMWCVIHNMVNAFQEYSGPEQFKTCTSNQGFKQSMWQCANLGPVSYDSCMQRYNQLPERFDPGEIVAHSDPTPIGMANLAFFMADFVDQADRHGYTWGTIRFKPTEGWIICCHNNWLINQQVKNICQWWISKNMWLGGNNFYIWEQGIALVGCSWHMYQPRVYHLSVDFIPSGACHEDMRVPKVKRDSGAHRENDYLRTPSINDNGDEFGHRCWYGHYTWQRRFGEMWPFTNFECWWIAVCAGMFWSQFGQVLTGVWISNWINGRTVLDNSDFTSHPWGFNSAYPYLMTACWNTKRPHWHYIKFRGMKELKYFYPVSKGQWNQMDLEAMRSYIWAWMLYNLYMHLPYSITPGQAMPYPWLCPWNCPEVCKSEMSYCPRARAAETNLMKWCFHRDMGHKGDCWCAIVLSSANRGHCHICSPMDTSFGKQAGIIWYMYMDGHTQVILEQRCHHNFFPYEFGLCSQTWKPNNDHCACRRQVRQDHHKGLVFEDQAMSYWKVKFADLRLLIWEQDMNDSFRPMCQPNYKWVRHHESTNCMTMRGRIPMSCVMRTPFYYAGWVNMENDMWQQGSWFRSTPFNLIGFIWLDQGVSSNQDGKYIDFWHSYDQKDKTIEKYPKARGARVGCLWGIIIAETFIYTDDMRVDWEAHFACKLWFLEMDDWHRPDWC"
AAtoRNA(aminoacid)