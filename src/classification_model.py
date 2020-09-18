#!/usr/bin/python

from math import exp
def Logistic(x) : 
   return(1/(1+exp(-x))) 

def Binary(x) : 
   if x < 0.5 : 
       return 0
   else : 
       return 1

def expression_classification(inputs) : 

    if len(inputs) != 12:
        print('Incorrect number of inputs')
        exit()
            
    type=inputs[0]
    legacyId=inputs[1]
    Development=inputs[2]
    DataScience=inputs[3]
    QualityAssurance=inputs[4]
    Design=inputs[5]
    challenge_duration=inputs[6]
    high_freq_createdBy=inputs[7]
    low_freq_createdBy=inputs[8]
    medium_freq_createdBy=inputs[9]
    day_of_year=inputs[10]
    challenge_prize=inputs[11]
    scaled_type = 2*(type-0)/(1-0)-1
    scaled_legacyId = (legacyId-30092700)/13648.8
    scaled_Development = 2*(Development-0)/(1-0)-1
    scaled_DataScience = (DataScience-0.0855967)/0.279825
    scaled_QualityAssurance = (QualityAssurance-0.0230453)/0.150078
    scaled_Design = (Design-0.111111)/0.314334
    scaled_challenge_duration = (challenge_duration-10.049)/15.3516
    scaled_high_freq_createdBy = (high_freq_createdBy-0.302881)/0.459599
    scaled_low_freq_createdBy = (low_freq_createdBy-0.0415638)/0.199631
    scaled_medium_freq_createdBy = 2*(medium_freq_createdBy-0)/(1-0)-1
    scaled_day_of_year = 2*(day_of_year-1)/(365-1)-1
    scaled_challenge_prize = (challenge_prize-1919.63)/5154.11
    y_1_1 = Logistic (6.12049+ (scaled_type*0.213451)+ (scaled_legacyId*2.3199)+ (scaled_Development*1.79326)+ (scaled_DataScience*-2.62986)+ (scaled_QualityAssurance*1.24882)+ (scaled_Design*3.60868)+ (scaled_challenge_duration*-2.9721)+ (scaled_high_freq_createdBy*1.89217)+ (scaled_low_freq_createdBy*1.62103)+ (scaled_medium_freq_createdBy*0.548806)+ (scaled_day_of_year*-1.28007)+ (scaled_challenge_prize*7.40932))
    y_1_2 = Logistic (-5.1726+ (scaled_type*-1.87706)+ (scaled_legacyId*-2.15233)+ (scaled_Development*0.0304841)+ (scaled_DataScience*-2.61317)+ (scaled_QualityAssurance*2.98104)+ (scaled_Design*-2.4753)+ (scaled_challenge_duration*-2.63589)+ (scaled_high_freq_createdBy*-2.17388)+ (scaled_low_freq_createdBy*-2.31919)+ (scaled_medium_freq_createdBy*2.54207)+ (scaled_day_of_year*-8.10497)+ (scaled_challenge_prize*-2.00058))
    y_1_3 = Logistic (-2.85548+ (scaled_type*4.57249)+ (scaled_legacyId*1.01853)+ (scaled_Development*-0.50226)+ (scaled_DataScience*-3.12569)+ (scaled_QualityAssurance*-2.05476)+ (scaled_Design*2.12489)+ (scaled_challenge_duration*0.746509)+ (scaled_high_freq_createdBy*0.303982)+ (scaled_low_freq_createdBy*3.5088)+ (scaled_medium_freq_createdBy*-2.21073)+ (scaled_day_of_year*4.58408)+ (scaled_challenge_prize*-9.62138))
    non_probabilistic_numOfSubmissions = Logistic (3.99695+ (y_1_1*11.5121)+ (y_1_2*-10.8356)+ (y_1_3*-11.1767))
    numOfSubmissions = non_probabilistic_numOfSubmissions
    
    return numOfSubmissions 
