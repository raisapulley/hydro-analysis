# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 16:27:53 2025

@author: raisa
"""
import hydrostats.data as hd
import pandas as pd
import pandas as to_csv
import hydrostats.visual as hv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#
#### ---- Loading the data
datat = pd.read_excel(r'C:\Users\raisa\Desktop\SAOJOAO_PLANILHAS\evapotranspiracao.xlsx', sheet_name='Todas_bacias', engine='openpyxl')
datat.Data = pd.to_datetime(datat.Data)
datat.set_index('Data', inplace=True) 
datat.info()
datat.head()
#
#### ---- Grouping annual and monthly series
def year_total(datat): # function to calculate annual totals
    b = datat.groupby(datat.index.year)
    return b.sum()
totalannual = year_total(datat)
#
"""
Info: All these def functions are in the hydrostats data.py file
"""
def monthly_total(datat): # function to calculate monthly totals
    a = datat.groupby(datat.index.strftime("%m"))
    return a.sum()
totalmonths = monthly_total(datat)
#
plt.rcParams.update({'font.size': 14})
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['patch.force_edgecolor'] = True
plt.rcParams['figure.facecolor'] = '0.90'
#
# Support calculations
totalannual = year_total(datat)
type_total = 'annual' # Choose the type of graph you want to produce: annual or monthly
pd.options.display.max_rows = 30
num_linhas = totalannual.shape[0]  # to know the number of years
#
# If you chose to make an annual chart or a monthly chart
if type_total == 'annual':
    xdatat = totalannual.index.tolist()
    total = totalannual  #for annual totals   
else:
    xdatat = ['jan.','fev.','mar.','abr.','maio','jun.','jul.','ago.','set.','out.','nov.','dez.']
    total = totalmonths/num_linhas  #for annual totals
#        
plt.rcParams.update({'font.size': 24})
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['patch.force_edgecolor'] = True
plt.rcParams['figure.facecolor'] = '0.90'
#
#""" Select the columns corresponding to the desired products
ymediamodcol=total.iloc[:,2].values  #variable for mean
desvpadmodcol=total.iloc[:,6].values  #variable for standard deviation
ymediassebopcol = total.iloc[:,3].values #variable for mean
desvpadssebopcol=total.iloc[:,7].values #variable for standard deviation
#
ymedianamodcol = total.iloc[:,10].values #variable for median
ymedianassebopol=total.iloc[:,11].values #variable for median
#"""
#
##boxplot
plt.boxplot(ymediamodcol)
plt.show()
#
plt.rcParams.update({'font.size': 25})
plt.rcParams["font.family"] = "Times New Roman"
#
# define figure
fig, ax = plt.subplots(1, figsize=(20, 9))
# numerical x
x = np.arange(0, len(xdatat))
print(x)
#
# Plot bars and error bars
plt.bar(x - 0.1, ymediamodcol, width = 0.2, color = '#3CB371')
plt.bar(x + 0.1, ymediassebopcol, width = 0.2, color = '#008000')
plt.errorbar(x - 0.1, ymediamodcol, yerr = desvpadmodcol, fmt = 'o',color = 'gray', markersize=2, capsize = 4)
plt.errorbar(x + 0.1, ymediassebopcol, yerr = desvpadssebopcol, fmt = 'o',color = 'gray', markersize=2, capsize = 4)
#Plot median lines
plt.plot(x - 0.1, ymediamodcol, color='#3CB371', marker='o', linestyle='--', linewidth=3)
plt.plot(x + 0.1, ymediassebopcol, color='#008000', marker='o', linestyle='--', linewidth=3)
#
# remove spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# x y details
#
# If you chose to make an annual chart or a monthly chart
if type_total == 'annual':
    plt.ylabel('ETa (mm.ano$^{-1}$)')
    plt.xlim(-0.5, 16.5)
    plt.ylim(0, 1800)
    plt.title('Evapotranspiração real anual da bacia menor de 404 km² (2003 a 2019)', loc ='center', fontsize=28)
else:
    plt.ylabel('ETa (mm.mês$^{-1}$)', fontsize=25)
    plt.xlim(-0.5, 11.5)
    plt.ylim(0, 180)
    plt.title('Evapotranspiração real mensal da bacia maior de 2115 km² (2003 a 2019)', loc ='center', fontsize=28)
#    
plt.grid(color='grey', linestyle='dotted', linewidth=1)
#plt.xticks(x, dadosf.x, fontsize=20)
#plt.xticks(x+0.5, xdatat, fontsize = 30, rotation=0)
plt.xticks(x+0.2, xdatat, fontsize = 25)
plt.gcf().autofmt_xdate()
#
# grid lines
ax.set_axisbelow(True)
ax.yaxis.grid(color='black', linestyle='dashed', alpha=0.2)
ax.set_facecolor('xkcd:gray')
ax.set_facecolor((1, 1, 1))
plt.rcParams.update({'font.size': 20})
plt.legend(['Mediana MOD16A2GF','Mediana SSEBop','MOD16A2GF','SSEBop'], loc='upper right', ncol =4)


plt.show()