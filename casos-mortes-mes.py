import pandas as pd
import numpy as np

casos = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/COVID/caso_full.csv.gz'
casos_full = pd.read_csv(casos)
casos_full = casos_full.fillna(0)
casos_full = casos_full.replace(np.nan,0)
casos_full = casos_full.astype({'city_ibge_code': int})
casos_full = casos_full[casos_full['city_ibge_code'] > 100]
casos_full.index = casos_full['city_ibge_code']
casos_full.drop(casos_full.columns[[1,3,4,5,6,7,9,10]],axis=1,inplace=True)
casos_full.sort_index(inplace=True)
datas = ['2020-02-29','2020-03-31','2020-04-30','2020-05-31','2020-06-30','2020-07-31','2020-08-31','2020-09-30']
casos_full = casos_full[casos_full['date'].isin(datas)]
replace_values = {'2020-02-29' : '02/2020', 
                  '2020-03-31' : '03/2020',
                  '2020-04-30' : '04/2020',
                  '2020-05-31' : '05/2020',
                  '2020-06-30' : '06/2020',
                  '2020-07-31' : '07/2020',
                  '2020-08-31' : '08/2020',
                  '2020-09-30' : '09/2020'}                                                                                  

casos_full = casos_full.replace({"date": replace_values})
casos_full.sort_values(['city_ibge_code','date'],inplace=True)

casos_full['New Cases'] = casos_full.groupby('city_ibge_code')['last_available_confirmed'].diff().fillna(casos_full['last_available_confirmed'])
casos_full['New Deaths'] = casos_full.groupby('city_ibge_code')['last_available_deaths'].diff().fillna(casos_full['last_available_deaths'])
casos_full.drop(casos_full.columns[[3,5,8,9]],axis=1,inplace=True)