#!/usr/bin/python

from math import tanh

def expression(inputs) : 

    # if type(inputs) != list:
    #    print('Argument must be a list')
    #    exit()
    if len(inputs) != 10:
       print('Incorrect number of inputs')
       exit()
    type=inputs[0]
    Development=inputs[1]
    DataScience=inputs[2]
    QualityAssurance=inputs[3]
    Design=inputs[4]
    challenge_duration=inputs[5]
    high_freq_createdBy=inputs[6]
    low_freq_createdBy=inputs[7]
    medium_freq_createdBy=inputs[8]
    challenge_prize=inputs[9]
    scaled_type = 2*(type-0)/(1-0)-1
    scaled_Development = 2*(Development-0)/(1-0)-1
    scaled_DataScience = (DataScience-0.0855967)/0.279825
    scaled_QualityAssurance = (QualityAssurance-0.0230453)/0.150078
    scaled_Design = (Design-0.111111)/0.314334
    scaled_challenge_duration = (challenge_duration-10.049)/15.3516
    scaled_high_freq_createdBy = (high_freq_createdBy-0.302881)/0.459599
    scaled_low_freq_createdBy = (low_freq_createdBy-0.0415638)/0.199631
    scaled_medium_freq_createdBy = 2*(medium_freq_createdBy-0)/(1-0)-1
    scaled_challenge_prize = (challenge_prize-1919.63)/5154.11
    y_1_1 = tanh (-4.14124+ (scaled_type*2.28731)+ (scaled_Development*-2.75089)+ (scaled_DataScience*0.625544)+ (scaled_QualityAssurance*-1.64514)+ (scaled_Design*0.733275)+ (scaled_challenge_duration*-0.440895)+ (scaled_high_freq_createdBy*4.7027)+ (scaled_low_freq_createdBy*-2.96126)+ (scaled_medium_freq_createdBy*-4.92873)+ (scaled_challenge_prize*3.06072))
    y_1_2 = tanh (-1.67349+ (scaled_type*0.597572)+ (scaled_Development*0.0105052)+ (scaled_DataScience*0.638908)+ (scaled_QualityAssurance*0.308648)+ (scaled_Design*0.499757)+ (scaled_challenge_duration*-1.93211)+ (scaled_high_freq_createdBy*1.82679)+ (scaled_low_freq_createdBy*-3.41035)+ (scaled_medium_freq_createdBy*-2.23862)+ (scaled_challenge_prize*0.946313))
    y_1_3 = tanh (4.49122+ (scaled_type*-1.53611)+ (scaled_Development*-2.24633)+ (scaled_DataScience*2.17896)+ (scaled_QualityAssurance*-0.15957)+ (scaled_Design*3.37958)+ (scaled_challenge_duration*-5.25104)+ (scaled_high_freq_createdBy*0.0758309)+ (scaled_low_freq_createdBy*-0.222471)+ (scaled_medium_freq_createdBy*2.19087)+ (scaled_challenge_prize*0.16074))
    y_1_4 = tanh (-9.79864+ (scaled_type*0.199695)+ (scaled_Development*-3.02956)+ (scaled_DataScience*-2.21907)+ (scaled_QualityAssurance*-0.867475)+ (scaled_Design*-1.96165)+ (scaled_challenge_duration*0.0253519)+ (scaled_high_freq_createdBy*-1.55279)+ (scaled_low_freq_createdBy*1.22941)+ (scaled_medium_freq_createdBy*-2.26966)+ (scaled_challenge_prize*0.76103))
    y_1_5 = tanh (-1.50443+ (scaled_type*0.612666)+ (scaled_Development*-2.28436)+ (scaled_DataScience*-1.02832)+ (scaled_QualityAssurance*0.948593)+ (scaled_Design*1.53195)+ (scaled_challenge_duration*-1.06625)+ (scaled_high_freq_createdBy*0.965652)+ (scaled_low_freq_createdBy*-0.486135)+ (scaled_medium_freq_createdBy*0.00805073)+ (scaled_challenge_prize*0.619479))
    y_1_6 = tanh (-0.586727+ (scaled_type*1.63188)+ (scaled_Development*-0.634632)+ (scaled_DataScience*-4.55418)+ (scaled_QualityAssurance*0.665412)+ (scaled_Design*2.79517)+ (scaled_challenge_duration*6.06619)+ (scaled_high_freq_createdBy*1.98754)+ (scaled_low_freq_createdBy*1.14633)+ (scaled_medium_freq_createdBy*-0.262794)+ (scaled_challenge_prize*0.727198))
    y_1_7 = tanh (2.05874+ (scaled_type*-2.11568)+ (scaled_Development*0.457095)+ (scaled_DataScience*-1.33504)+ (scaled_QualityAssurance*-0.75193)+ (scaled_Design*2.69038)+ (scaled_challenge_duration*-0.851879)+ (scaled_high_freq_createdBy*-0.442478)+ (scaled_low_freq_createdBy*1.72053)+ (scaled_medium_freq_createdBy*0.422527)+ (scaled_challenge_prize*1.15407))
    y_1_8 = tanh (-1.6033+ (scaled_type*1.25507)+ (scaled_Development*-1.91718)+ (scaled_DataScience*-1.54117)+ (scaled_QualityAssurance*-0.737836)+ (scaled_Design*1.77679)+ (scaled_challenge_duration*2.31467)+ (scaled_high_freq_createdBy*-0.163732)+ (scaled_low_freq_createdBy*-2.64589)+ (scaled_medium_freq_createdBy*-0.556802)+ (scaled_challenge_prize*2.39158))
    y_1_9 = tanh (-1.66042+ (scaled_type*-2.23517)+ (scaled_Development*1.54418)+ (scaled_DataScience*0.600864)+ (scaled_QualityAssurance*0.298367)+ (scaled_Design*-0.966002)+ (scaled_challenge_duration*1.32596)+ (scaled_high_freq_createdBy*0.558867)+ (scaled_low_freq_createdBy*0.709993)+ (scaled_medium_freq_createdBy*0.823189)+ (scaled_challenge_prize*-1.15001))
    scaled_numOfSubmissions =  (0.69275+ (y_1_1*0.119397)+ (y_1_2*-0.117143)+ (y_1_3*0.251236)+ (y_1_4*1.88501)+ (y_1_5*-0.239511)+ (y_1_6*0.227546)+ (y_1_7*-0.0364799)+ (y_1_8*0.0374264)+ (y_1_9*0.0104294))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(1614-0)+0)
    
    return numOfSubmissions 
