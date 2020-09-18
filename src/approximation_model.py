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
    y_1_1 = tanh (-2.14353+ (scaled_type*-2.73381)+ (scaled_Development*-0.541849)+ (scaled_DataScience*0.57334)+ (scaled_QualityAssurance*-0.672025)+ (scaled_Design*-1.23957)+ (scaled_challenge_duration*1.99939)+ (scaled_high_freq_createdBy*0.511219)+ (scaled_low_freq_createdBy*-2.57948)+ (scaled_medium_freq_createdBy*-0.166916)+ (scaled_challenge_prize*-7.00811))
    y_1_2 = tanh (2.46445+ (scaled_type*2.54887)+ (scaled_Development*2.27992)+ (scaled_DataScience*3.04269)+ (scaled_QualityAssurance*-0.974234)+ (scaled_Design*-3.76749)+ (scaled_challenge_duration*2.98565)+ (scaled_high_freq_createdBy*0.186072)+ (scaled_low_freq_createdBy*2.86959)+ (scaled_medium_freq_createdBy*-0.557034)+ (scaled_challenge_prize*-9.0752))
    y_1_3 = tanh (1.75653+ (scaled_type*2.04263)+ (scaled_Development*-1.53739)+ (scaled_DataScience*3.97107)+ (scaled_QualityAssurance*1.86568)+ (scaled_Design*-0.409183)+ (scaled_challenge_duration*-1.22471)+ (scaled_high_freq_createdBy*0.656863)+ (scaled_low_freq_createdBy*-3.46269)+ (scaled_medium_freq_createdBy*1.30477)+ (scaled_challenge_prize*1.02941))
    y_1_4 = tanh (1.20328+ (scaled_type*-4.03792)+ (scaled_Development*-0.48887)+ (scaled_DataScience*3.88124)+ (scaled_QualityAssurance*-0.455934)+ (scaled_Design*-1.374)+ (scaled_challenge_duration*-0.651804)+ (scaled_high_freq_createdBy*2.58968)+ (scaled_low_freq_createdBy*1.88395)+ (scaled_medium_freq_createdBy*-2.76644)+ (scaled_challenge_prize*2.29721))
    y_1_5 = tanh (1.32291+ (scaled_type*-0.307055)+ (scaled_Development*2.56003)+ (scaled_DataScience*-4.51935)+ (scaled_QualityAssurance*-0.420608)+ (scaled_Design*1.36933)+ (scaled_challenge_duration*5.92885)+ (scaled_high_freq_createdBy*0.771665)+ (scaled_low_freq_createdBy*-4.21044)+ (scaled_medium_freq_createdBy*1.39337)+ (scaled_challenge_prize*0.0677177))
    y_1_6 = tanh (-1.34677+ (scaled_type*0.114432)+ (scaled_Development*3.46425)+ (scaled_DataScience*-1.34466)+ (scaled_QualityAssurance*0.456432)+ (scaled_Design*-5.71949)+ (scaled_challenge_duration*1.45784)+ (scaled_high_freq_createdBy*-0.15847)+ (scaled_low_freq_createdBy*0.0688026)+ (scaled_medium_freq_createdBy*-0.257461)+ (scaled_challenge_prize*6.63036))
    y_1_7 = tanh (-1.4768+ (scaled_type*0.418125)+ (scaled_Development*-2.86824)+ (scaled_DataScience*5.0859)+ (scaled_QualityAssurance*0.45724)+ (scaled_Design*-1.50764)+ (scaled_challenge_duration*-6.70981)+ (scaled_high_freq_createdBy*-0.75747)+ (scaled_low_freq_createdBy*4.31946)+ (scaled_medium_freq_createdBy*-1.50036)+ (scaled_challenge_prize*-0.151968))
    y_1_8 = tanh (-2.37267+ (scaled_type*-1.98254)+ (scaled_Development*-1.7517)+ (scaled_DataScience*2.69339)+ (scaled_QualityAssurance*0.585064)+ (scaled_Design*-2.03164)+ (scaled_challenge_duration*-1.83394)+ (scaled_high_freq_createdBy*-0.476106)+ (scaled_low_freq_createdBy*-1.14115)+ (scaled_medium_freq_createdBy*0.114462)+ (scaled_challenge_prize*5.14284))
    y_1_9 = tanh (-0.985304+ (scaled_type*-0.404054)+ (scaled_Development*1.74697)+ (scaled_DataScience*-1.79348)+ (scaled_QualityAssurance*-0.68427)+ (scaled_Design*-1.77349)+ (scaled_challenge_duration*-2.4013)+ (scaled_high_freq_createdBy*2.78981)+ (scaled_low_freq_createdBy*0.849185)+ (scaled_medium_freq_createdBy*-3.19487)+ (scaled_challenge_prize*1.1264))
    scaled_numOfSubmissions =  (-1.01634+ (y_1_1*0.10712)+ (y_1_2*-0.113413)+ (y_1_3*0.115005)+ (y_1_4*0.139037)+ (y_1_5*-2.80936)+ (y_1_6*0.0986334)+ (y_1_7*-2.70378)+ (y_1_8*-0.14373)+ (y_1_9*-0.132297))
    numOfSubmissions = (0.5*(scaled_numOfSubmissions+1.0)*(1614-0)+0)
    
    return numOfSubmissions 
