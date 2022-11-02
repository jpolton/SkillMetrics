import numpy as np
import matplotlib.pyplot as plt
import skill_metrics as sm

# Define consistent data
# also note that the first entry should not show up in the marD because it is the reference

sdev=  [1., 0.58612097, 1.00984653, 0.60574307, 1.06347975, 0.89496514,
 1.0121957, 0.95821264, 1.06343127, 0.99495893, 0.99544413, 0.99079383,
 1.02032532]
crmsd= [0., 0.67083162, 0.35317993, 0.63518765, 0.53751324, 0.50950639,
 0.32421738, 0.43099497, 0.50856422, 0.03357475, 0.04331349, 0.02994525,
 0.10166172]
ccoef= [1., 0.76223405, 0.9382881,  0.79527226, 0.86605725, 0.86113178,
 0.94814828, 0.90398244, 0.88028656, 0.99944628, 0.9990681,  0.99959025,
 0.99513783]
label = ['Non-Dimensional Observation',
         'EXP_MES_WAV_DJC_NTM_TDISSv2deepM2amp', 'EXP_MES_WAV_DJC_NTM_TDISSv2deepM2pha',
         'EXP_MES_WAV_DJC_NTM_TDISSv2shallowM2amp', 'EXP_MES_WAV_DJC_NTM_TDISSv2shallowM2pha',
         'EXP_MES_WAV_DJC_NTM_TDISSx2deepM2amp', 'EXP_MES_WAV_DJC_NTM_TDISSx2deepM2pha',
         'EXP_MES_WAV_DJC_NTM_TDISSx2shallowM2amp', 'EXP_MES_WAV_DJC_NTM_TDISSx2shallowM2pha',
         'FESdeepM2amp', 'FESdeepM2pha', 'FESshallowM2amp', 'FESshallowM2pha']

# put the data into arrays
sdev = np.array(sdev)
crmsd = np.array(crmsd)
ccoef = np.array(ccoef)

# define the marker-dict 'marD' for the data points:
# markershape is the experiment
# 'w' and 'k' define the edgecolors (here deep or shallow)
# the facecolors are for variable
marD = {'p': {'k': ['darkred', 'darkgoldenrod'],
              'w': ['darkred', 'darkgoldenrod']},
        'd': {'k': ['darkred', 'darkgoldenrod'],
              'w': ['darkred', 'darkgoldenrod']},
        '*': {'k': ['darkred', 'darkgoldenrod'],
              'w': ['darkred', 'darkgoldenrod']}}


# define marker-dict for legend: label: [marker, edgecolor, facecolor]
#taylor_label = ['hist', 'present', 'future']
taylor_label = dict({'> 200m':['^', 'k', 'cadetblue'],
                     '< 200m':['^', 'w', 'cadetblue'],
                     'amp': ['o', 'w', 'darkred'],
                     'pha':['o', 'w', 'darkgoldenrod'],
                     'MES_v2':['p', 'darkorange', 'w'],
                     'MES_x2':['d', 'darkorange', 'w'],
                     'FES': ['*', 'darkorange', 'w']
                     })

plt.figure(num=1, figsize=(7, 6))

sm.taylor_diagram(sdev,crmsd,ccoef, checkStats='on', styleOBS = '-', markerLabel = taylor_label,
                    colOBS = 'darkblue', markerobs = 'o', markerLegend = 'off',stylerms ='-',colRMS='grey',
                    titleOBS = 'Observation', titleRMS = 'off', titleRMSDangle=20, colCOR='dimgrey',
                    MarkerDictCH=marD, alpha=0.2, markerSize= 9)
#plt.show()
plt.savefig('M2_taylor_diagram.png')