import pandas as pd
import numpy as np

aux_abr = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/Auxílio Emergencial/202004_AuxilioEmergencial.csv'
aux_mai = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/Auxílio Emergencial/202005_AuxilioEmergencial.csv'
aux_jun = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/Auxílio Emergencial/202006_AuxilioEmergencial.csv'
aux_jul = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/Auxílio Emergencial/202007_AuxilioEmergencial.csv'
aux_ago = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/Auxílio Emergencial/202008_AuxilioEmergencial.csv'


def aux_emerg_cleaning(aux):
    aux_mes = pd.read_csv(aux,chunksize=50000,encoding='Latin-1',sep=';') #reading csv in chunks
    chunk_list = []  
    for chunks in aux_mes: #cleaning the dataframes
        chunks['CÓDIGO MUNICÍPIO IBGE'].fillna(0, inplace=True, axis=0)
        chunks = chunks.astype({'CÓDIGO MUNICÍPIO IBGE':'int'})
        chunks.drop(chunks.columns[[4,5,6,7,8,9,10,11,12]],inplace=True,axis=1)
        chunks = chunks.rename(columns={'VALOR BENEFÍCIO': 'VALOR BENEFÍCIO - IND'})
        agrupado1 = chunks.groupby('CÓDIGO MUNICÍPIO IBGE')
        auxemer1 = agrupado1['VALOR BENEFÍCIO - IND']
        valor1 = auxemer1.agg(np.sum)
        chunks.drop_duplicates(subset='CÓDIGO MUNICÍPIO IBGE',inplace=True)
        chunks.index = chunks['CÓDIGO MUNICÍPIO IBGE']
        chunks.sort_index(inplace=True)
        filtered_chunk = pd.concat([chunks,valor1],axis=1)
        chunk_list.append(filtered_chunk)
    for dataframes in chunk_list:
        dataframes.drop(dataframes.columns[[2]],axis=1,inplace=True)
    filtered_data = pd.concat(chunk_list,axis=0)
    filtered_data.sort_index(inplace=True)
    filtered_data['SOMA'] = filtered_data.iloc[:,4].apply(lambda x: sum(int(i) if len(x) > 0 else np.nan for i in x.split(',')))
    agrupamento = filtered_data.groupby('CÓDIGO MUNICÍPIO IBGE')
    soma_agrupada = agrupamento['SOMA']
    agrupamento_somado = soma_agrupada.agg(np.sum)
    auxilio_mes = pd.merge(left=filtered_data,right=agrupamento_somado,on='CÓDIGO MUNICÍPIO IBGE',how='left')
    return auxilio_mes

auxilio_abr = aux_emerg_cleaning(aux=aux_abr)
auxilio_mai = aux_emerg_cleaning(aux=aux_mai)
auxilio_jun = aux_emerg_cleaning(aux=aux_jun)
auxilio_jul = aux_emerg_cleaning(aux=aux_jul)
auxilio_ago = aux_emerg_cleaning(aux=aux_ago)

for auxilios in (auxilio_abr,auxilio_mai,auxilio_jun,auxilio_jul,auxilio_ago):
    auxilios.index.astype(int)
    auxilios = auxilios[~auxilios.index.duplicated(keep='first')]

auxilio_total = pd.merge(left=auxilio_abr,right=auxilio_mai,on='CÓDIGO MUNICÍPIO IBGE',how='left')
auxilio_total = pd.merge(left=auxilio_total,right=auxilio_jun,on='CÓDIGO MUNICÍPIO IBGE',how='left')
auxilio_total = pd.merge(left=auxilio_total,right=auxilio_jul,on='CÓDIGO MUNICÍPIO IBGE',how='left')
auxilio_total = pd.merge(left=auxilio_total,right=auxilio_ago,on='CÓDIGO MUNICÍPIO IBGE',how='left')

auxilio_total = auxilio_total.replace('nan',0)
auxilio_total = auxilio_total.replace(np.nan,0)
auxilio_total = auxilio_total.fillna(0)

auxilio_total.to_excel(excel_writer='/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Aux_Emg.xlsx')    
