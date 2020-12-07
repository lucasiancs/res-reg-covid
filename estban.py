import numpy as np
import pandas as pd

jan = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202001_ESTBAN.CSV'
fev = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202002_ESTBAN.CSV'
mar = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202003_ESTBAN.CSV'
abr = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202004_ESTBAN.CSV'
mai = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202005_ESTBAN.CSV'
jun = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202006_ESTBAN.CSV'
jul = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202007_ESTBAN.CSV'
aug = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/ESTBAN/202008_ESTBAN.CSV'




def clean_estban(df):
    est_ban = pd.read_csv(df,sep='\n',encoding='cp1252')
    est_ban.drop(est_ban.index[0],axis=0,inplace=True)
    est_ban.columns = ['ESTBAN']
    est_ban = est_ban['ESTBAN'].str.split(';',expand=True)
    est_ban.columns = est_ban.iloc[0,:]
    est_ban.drop(est_ban.index[0],axis=0,inplace=True)
    est_ban.index = est_ban['CODMUN_IBGE']
    credt = est_ban.loc[:,['#DATA_BASE','UF','MUNICIPIO','VERBETE_160_OPERACOES_DE_CREDITO']]
    credt.replace('',0,inplace=True)
    credt['VERBETE_160_OPERACOES_DE_CREDITO'] = credt['VERBETE_160_OPERACOES_DE_CREDITO'].astype('int64')
    credt['CREDITO'] = credt.groupby('CODMUN_IBGE')['VERBETE_160_OPERACOES_DE_CREDITO'].agg(np.sum)
    credt.drop_duplicates(subset=['MUNICIPIO'],inplace=True)
    credt.drop(credt.columns[[3]],axis=1,inplace=True)
    return credt

estban_jan = clean_estban(jan)
estban_fev = clean_estban(fev)
estban_mar = clean_estban(mar)
estban_abr = clean_estban(abr)
estban_mai = clean_estban(mai)
estban_jun = clean_estban(jun)
estban_jul = clean_estban(jul)
estban_aug = clean_estban(aug)

estban_2020 = pd.merge(left=estban_jan,right=estban_fev,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_mar,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_abr,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_mai,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_jun,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_jul,on='CODMUN_IBGE',how='left')
estban_2020 = pd.merge(left=estban_2020,right=estban_aug,on='CODMUN_IBGE',how='left')

