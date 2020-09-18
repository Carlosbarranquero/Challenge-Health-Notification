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
    y_1_1 = tanh (0.702425+ (scaled_type*-0.0463521)+ (scaled_Development*0.318221)+ (scaled_DataScience*0.287255)+ (scaled_QualityAssurance*-0.447497)+ (scaled_Design*0.0807428)+ (scaled_challenge_duration*-0.150304)+ (scaled_high_freq_createdBy*0.773027)+ (scaled_low_freq_createdBy*-1.7457)+ (scaled_medium_freq_createdBy*0.204698)+ (scaled_challenge_prize*1.85596))
    y_1_2 = tanh (-0.895252+ (scaled_type*-0.0413848)+ (scaled_Development*-0.482616)+ (scaled_DataScience*0.262333)+ (scaled_QualityAssurance*0.150647)+ (scaled_Design*-0.336806)+ (scaled_challenge_duration*-0.131607)+ (scaled_high_freq_createdBy*-1.27288)+ (scaled_low_freq_createdBy*-1.28991)+ (scaled_medium_freq_createdBy*1.40586)+ (scaled_challenge_prize*1.77075))
    y_1_3 = tanh (0.558783+ (scaled_type*-0.0143317)+ (scaled_Development*0.896583)+ (scaled_DataScience*-0.499694)+ (scaled_QualityAssurance*0.262578)+ (scaled_Design*-0.608768)+ (scaled_challenge_duration*0.00179995)+ (scaled_high_freq_createdBy*-0.885784)+ (scaled_low_freq_createdBy*-0.787474)+ (scaled_medium_freq_createdBy*1.30265)+ (scaled_challenge_prize*-0.478526))
    y_1_4 = tanh (-1.03406+ (scaled_type*-0.0277515)+ (scaled_Development*-0.678497)+ (scaled_DataScience*0.195618)+ (scaled_QualityAssurance*-0.17946)+ (scaled_Design*0.0694449)+ (scaled_challenge_duration*-0.210447)+ (scaled_high_freq_createdBy*0.773844)+ (scaled_low_freq_createdBy*-0.692625)+ (scaled_medium_freq_createdBy*-0.756669)+ (scaled_challenge_prize*0.0594927))
    y_1_5 = tanh (-0.159969+ (scaled_type*0.0965703)+ (scaled_Development*-1.19967)+ (scaled_DataScience*1.15464)+ (scaled_QualityAssurance*0.48387)+ (scaled_Design*0.50588)+ (scaled_challenge_duration*0.893719)+ (scaled_high_freq_createdBy*0.303865)+ (scaled_low_freq_createdBy*0.943648)+ (scaled_medium_freq_createdBy*-0.705805)+ (scaled_challenge_prize*-0.535531))
    y_1_6 = tanh (0.546224+ (scaled_type*-0.134085)+ (scaled_Development*1.03757)+ (scaled_DataScience*-0.928443)+ (scaled_QualityAssurance*0.710627)+ (scaled_Design*-0.67461)+ (scaled_challenge_duration*-1.26647)+ (scaled_high_freq_createdBy*-0.468156)+ (scaled_low_freq_createdBy*-1.19586)+ (scaled_medium_freq_createdBy*1.07793)+ (scaled_challenge_prize*0.870608))
    scaled_numOfSubmissions =  (-0.0688432+ (y_1_1*-0.938496)+ (y_1_2*1.158)+ (y_1_3*-0.640301)+ (y_1_4*0.928042)+ (y_1_5*-0.932103)+ (y_1_6*-0.514218))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(1614-0)+0)
    
    return numOfSubmissions 
