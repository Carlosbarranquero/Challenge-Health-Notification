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
    y_1_1 = tanh (-0.679029+ (scaled_type*-1.50352)+ (scaled_Development*0.526126)+ (scaled_DataScience*1.06092)+ (scaled_QualityAssurance*0.39317)+ (scaled_Design*-2.4547)+ (scaled_challenge_duration*0.0770525)+ (scaled_high_freq_createdBy*-2.92079)+ (scaled_low_freq_createdBy*0.897715)+ (scaled_medium_freq_createdBy*2.31395)+ (scaled_challenge_prize*0.517468))
    y_1_2 = tanh (2.79867+ (scaled_type*-0.741403)+ (scaled_Development*1.30682)+ (scaled_DataScience*-0.368839)+ (scaled_QualityAssurance*0.234348)+ (scaled_Design*0.39683)+ (scaled_challenge_duration*0.316367)+ (scaled_high_freq_createdBy*0.880003)+ (scaled_low_freq_createdBy*3.31175)+ (scaled_medium_freq_createdBy*-1.04531)+ (scaled_challenge_prize*0.0278751))
    y_1_3 = tanh (-6.49067+ (scaled_type*0.0275089)+ (scaled_Development*-5.64374)+ (scaled_DataScience*-3.02885)+ (scaled_QualityAssurance*-1.61211)+ (scaled_Design*6.55182)+ (scaled_challenge_duration*6.25462)+ (scaled_high_freq_createdBy*8.00254)+ (scaled_low_freq_createdBy*-4.17777)+ (scaled_medium_freq_createdBy*-7.68137)+ (scaled_challenge_prize*3.70839))
    y_1_4 = tanh (-5.5977+ (scaled_type*4.76765)+ (scaled_Development*-7.9269)+ (scaled_DataScience*-2.84882)+ (scaled_QualityAssurance*-2.32443)+ (scaled_Design*11.3153)+ (scaled_challenge_duration*-3.06442)+ (scaled_high_freq_createdBy*11.7476)+ (scaled_low_freq_createdBy*-7.47658)+ (scaled_medium_freq_createdBy*-9.56692)+ (scaled_challenge_prize*12.2092))
    y_1_5 = tanh (-3.29361+ (scaled_type*3.5414)+ (scaled_Development*-4.60949)+ (scaled_DataScience*-1.93679)+ (scaled_QualityAssurance*-1.43768)+ (scaled_Design*6.72943)+ (scaled_challenge_duration*-1.51341)+ (scaled_high_freq_createdBy*8.22972)+ (scaled_low_freq_createdBy*-4.66889)+ (scaled_medium_freq_createdBy*-6.82315)+ (scaled_challenge_prize*8.27499))
    scaled_numOfSubmissions =  (-0.966075+ (y_1_1*0.268985)+ (y_1_2*-0.0308669)+ (y_1_3*0.281586)+ (y_1_4*-5.66384)+ (y_1_5*5.65358))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(1614-0)+0)
    
    return numOfSubmissions 
