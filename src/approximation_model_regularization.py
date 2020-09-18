#!/usr/bin/python

from math import tanh

def expression(inputs) : 


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
    scaled_DataScience = (DataScience-0.0362524)/0.186961
    scaled_QualityAssurance = (QualityAssurance-0.0254237)/0.157445
    scaled_Design = (Design-0.0729755)/0.260158
    scaled_challenge_duration = (challenge_duration-6.81827)/5.6451
    scaled_high_freq_createdBy = (high_freq_createdBy-0.346045)/0.47582
    scaled_low_freq_createdBy = (low_freq_createdBy-0.0357815)/0.185789
    scaled_medium_freq_createdBy = 2*(medium_freq_createdBy-0)/(1-0)-1
    scaled_challenge_prize = (challenge_prize-1117.31)/1106.32
    y_1_1 = tanh (1.2894+ (scaled_type*3.19862)+ (scaled_Development*-0.691157)+ (scaled_DataScience*0.306422)+ (scaled_QualityAssurance*-2.07697)+ (scaled_Design*0.360245)+ (scaled_challenge_duration*0.751147)+ (scaled_high_freq_createdBy*-0.817565)+ (scaled_low_freq_createdBy*-0.565436)+ (scaled_medium_freq_createdBy*1.48279)+ (scaled_challenge_prize*-0.548726))
    y_1_2 = tanh (-0.65046+ (scaled_type*-0.666055)+ (scaled_Development*-0.639528)+ (scaled_DataScience*-0.790793)+ (scaled_QualityAssurance*1.16154)+ (scaled_Design*-0.657011)+ (scaled_challenge_duration*0.0470725)+ (scaled_high_freq_createdBy*0.536204)+ (scaled_low_freq_createdBy*-0.148848)+ (scaled_medium_freq_createdBy*-0.970353)+ (scaled_challenge_prize*-0.328984))
    y_1_3 = tanh (-0.465536+ (scaled_type*2.1985)+ (scaled_Development*-1.79191)+ (scaled_DataScience*2.46172)+ (scaled_QualityAssurance*-2.08118)+ (scaled_Design*1.40647)+ (scaled_challenge_duration*2.51044)+ (scaled_high_freq_createdBy*0.748643)+ (scaled_low_freq_createdBy*1.3562)+ (scaled_medium_freq_createdBy*-0.226649)+ (scaled_challenge_prize*-1.54569))
    y_1_4 = tanh (-1.23724+ (scaled_type*-0.138381)+ (scaled_Development*-0.17635)+ (scaled_DataScience*-1.1425)+ (scaled_QualityAssurance*-0.541238)+ (scaled_Design*0.86249)+ (scaled_challenge_duration*-0.258047)+ (scaled_high_freq_createdBy*1.26927)+ (scaled_low_freq_createdBy*-1.67461)+ (scaled_medium_freq_createdBy*-1.90133)+ (scaled_challenge_prize*-0.829097))
    y_1_5 = tanh (0.749774+ (scaled_type*-1.56174)+ (scaled_Development*-0.75046)+ (scaled_DataScience*-1.72459)+ (scaled_QualityAssurance*-0.113665)+ (scaled_Design*1.46075)+ (scaled_challenge_duration*-1.29042)+ (scaled_high_freq_createdBy*0.970959)+ (scaled_low_freq_createdBy*-0.0251828)+ (scaled_medium_freq_createdBy*0.237583)+ (scaled_challenge_prize*1.27162))
    scaled_numOfSubmissions =  (-0.502862+ (y_1_1*0.58971)+ (y_1_2*0.781398)+ (y_1_3*0.221133)+ (y_1_4*-0.577208)+ (y_1_5*0.486855))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(29-0)+0)
    
    return numOfSubmissions 
