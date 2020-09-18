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
    scaled_DataScience = (DataScience-0.0376157)/0.19032
    scaled_QualityAssurance = (QualityAssurance-0.0248843)/0.155817
    scaled_Design = (Design-0.0746528)/0.262906
    scaled_challenge_duration = (challenge_duration-6.84838)/5.73555
    scaled_high_freq_createdBy = (high_freq_createdBy-0.329861)/0.470299
    scaled_low_freq_createdBy = (low_freq_createdBy-0.0381944)/0.191721
    scaled_medium_freq_createdBy = 2*(medium_freq_createdBy-0)/(1-0)-1
    scaled_challenge_prize = (challenge_prize-1127)/1123.58
    y_1_1 = tanh (-2.61663+ (scaled_type*-1.53305)+ (scaled_Development*1.18293)+ (scaled_DataScience*0.44987)+ (scaled_QualityAssurance*0.278144)+ (scaled_Design*0.540857)+ (scaled_challenge_duration*-0.0186631)+ (scaled_high_freq_createdBy*1.23474)+ (scaled_low_freq_createdBy*0.083376)+ (scaled_medium_freq_createdBy*1.37667)+ (scaled_challenge_prize*0.111184))
    y_1_2 = tanh (1.79971+ (scaled_type*-0.723378)+ (scaled_Development*0.484817)+ (scaled_DataScience*0.457151)+ (scaled_QualityAssurance*-0.519709)+ (scaled_Design*-0.805725)+ (scaled_challenge_duration*-0.98856)+ (scaled_high_freq_createdBy*1.27431)+ (scaled_low_freq_createdBy*-0.21784)+ (scaled_medium_freq_createdBy*1.13404)+ (scaled_challenge_prize*0.372016))
    y_1_3 = tanh (0.124957+ (scaled_type*-0.89784)+ (scaled_Development*-0.181614)+ (scaled_DataScience*-0.168964)+ (scaled_QualityAssurance*-0.178535)+ (scaled_Design*0.114763)+ (scaled_challenge_duration*0.988308)+ (scaled_high_freq_createdBy*-0.41553)+ (scaled_low_freq_createdBy*-2.25211)+ (scaled_medium_freq_createdBy*-0.0297511)+ (scaled_challenge_prize*0.722533))
    y_1_4 = tanh (0.393524+ (scaled_type*0.673372)+ (scaled_Development*0.23928)+ (scaled_DataScience*0.51231)+ (scaled_QualityAssurance*-1.41279)+ (scaled_Design*-1.33306)+ (scaled_challenge_duration*-3.54135)+ (scaled_high_freq_createdBy*-0.0435734)+ (scaled_low_freq_createdBy*-0.556775)+ (scaled_medium_freq_createdBy*-1.35358)+ (scaled_challenge_prize*0.0394218))
    y_1_5 = tanh (-0.404441+ (scaled_type*1.17921)+ (scaled_Development*0.088321)+ (scaled_DataScience*0.338442)+ (scaled_QualityAssurance*0.425748)+ (scaled_Design*0.544771)+ (scaled_challenge_duration*0.454422)+ (scaled_high_freq_createdBy*-0.757253)+ (scaled_low_freq_createdBy*0.0329259)+ (scaled_medium_freq_createdBy*-0.50932)+ (scaled_challenge_prize*0.0368668))
    y_1_6 = tanh (0.17461+ (scaled_type*0.400233)+ (scaled_Development*0.950591)+ (scaled_DataScience*0.59854)+ (scaled_QualityAssurance*-0.410306)+ (scaled_Design*0.86864)+ (scaled_challenge_duration*-0.0309214)+ (scaled_high_freq_createdBy*-0.228913)+ (scaled_low_freq_createdBy*0.873042)+ (scaled_medium_freq_createdBy*0.188181)+ (scaled_challenge_prize*0.411827))
    y_1_7 = tanh (2.22758+ (scaled_type*-0.570411)+ (scaled_Development*0.417618)+ (scaled_DataScience*-2.51897)+ (scaled_QualityAssurance*0.989794)+ (scaled_Design*-0.0417514)+ (scaled_challenge_duration*-1.42264)+ (scaled_high_freq_createdBy*0.385102)+ (scaled_low_freq_createdBy*-0.468223)+ (scaled_medium_freq_createdBy*0.0277526)+ (scaled_challenge_prize*-1.22096))
    y_1_8 = tanh (1.07222+ (scaled_type*1.24012)+ (scaled_Development*0.598977)+ (scaled_DataScience*-1.10348)+ (scaled_QualityAssurance*-1.03066)+ (scaled_Design*0.840007)+ (scaled_challenge_duration*-0.471519)+ (scaled_high_freq_createdBy*0.801737)+ (scaled_low_freq_createdBy*-0.759107)+ (scaled_medium_freq_createdBy*-3.10456)+ (scaled_challenge_prize*-0.861326))
    y_1_9 = tanh (1.51601+ (scaled_type*-1.02221)+ (scaled_Development*-1.00065)+ (scaled_DataScience*-1.72005)+ (scaled_QualityAssurance*1.29235)+ (scaled_Design*-0.0380242)+ (scaled_challenge_duration*-0.880542)+ (scaled_high_freq_createdBy*0.860956)+ (scaled_low_freq_createdBy*-0.896955)+ (scaled_medium_freq_createdBy*-0.25947)+ (scaled_challenge_prize*0.600885))
    y_1_10 = tanh (0.744773+ (scaled_type*-0.144991)+ (scaled_Development*0.0520204)+ (scaled_DataScience*1.17272)+ (scaled_QualityAssurance*-0.871647)+ (scaled_Design*0.919739)+ (scaled_challenge_duration*-0.237058)+ (scaled_high_freq_createdBy*-0.217635)+ (scaled_low_freq_createdBy*-0.518848)+ (scaled_medium_freq_createdBy*0.964883)+ (scaled_challenge_prize*0.438667))
    scaled_numOfSubmissions =  (-0.495155+ (y_1_1*-0.561415)+ (y_1_2*-0.329178)+ (y_1_3*0.136975)+ (y_1_4*0.0692715)+ (y_1_5*-0.267728)+ (y_1_6*-0.333208)+ (y_1_7*-0.272756)+ (y_1_8*0.110127)+ (y_1_9*0.0610682)+ (y_1_10*0.337046))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(29-0)+0)
    
    return numOfSubmissions 
