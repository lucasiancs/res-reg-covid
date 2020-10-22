import pandas as pd
import numpy as np

#importando bases
caged8 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202008.txt'
cagedaug = pd.read_csv(caged8,sep=';', encoding='cp1252')
caged7 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202007.txt'
cagedjul = pd.read_csv(caged7,sep=';', encoding='cp1252')

caged6 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202006.txt'
cagedjun = pd.read_csv(caged6,sep=';', encoding='cp1252')

caged5 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202005.txt'
cagedmai = pd.read_csv(caged5,sep=';', encoding='cp1252')

caged4 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202004.txt'
cagedabr = pd.read_csv(caged4,sep=';', encoding='cp1252')

caged3 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202003.txt'
cagedmar = pd.read_csv(caged3,sep=';', encoding='cp1252')

caged2 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202002.txt'
cagedfev = pd.read_csv(caged2,sep=';', encoding='cp1252')

caged1 = '/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Bases/CAGED/Estabelecimentos/CAGEDESTAB202001.txt'
cagedjan = pd.read_csv(caged1,sep=';', encoding='cp1252')
#novos nomes para as colunas
columns1 = ['Ano/Mes','Código da Grande Região','Código UF','Código do Município','Código CNAE','Admitidos-Demitidos','Tipo do tamanho em Jan/2020'] 
#remover algumas colunas apenas com um loop
for cageds in (cagedjan,cagedfev,cagedmar,cagedabr,cagedmai,cagedjun,cagedjul,cagedaug):
    cageds = cageds.drop(cageds.columns[[5,6,7,8,10,11]], axis=1,inplace=True)
#renomeando colunas
cagedaug.columns = columns1    
cagedjul.columns = columns1
cagedjun.columns = columns1
cagedmai.columns = columns1
cagedabr.columns = columns1
cagedmar.columns = columns1
cagedfev.columns = columns1
cagedjan.columns = columns1
#criando novas colunas: nome da regiao
for cageds in (cagedjan,cagedfev,cagedmar,cagedabr,cagedmai,cagedjun,cagedjul,cagedaug):
    conditions = [
            (cageds['Código da Grande Região']==1),
            (cageds['Código da Grande Região']==2),
            (cageds['Código da Grande Região']==3),
            (cageds['Código da Grande Região']==4),
            (cageds['Código da Grande Região']==5),
            ]
    choices = ['Norte','Nordeste','Sudeste','Sul','Centro-Oeste']
    cageds['Nome da Grande Região'] = np.select(conditions, choices)
    conditions1 = [
            (cageds['Código UF']==11),
            (cageds['Código UF']==12),
            (cageds['Código UF']==13),
            (cageds['Código UF']==14),
            (cageds['Código UF']==15),
            (cageds['Código UF']==16),
            (cageds['Código UF']==17),
            (cageds['Código UF']==21),
            (cageds['Código UF']==22),
            (cageds['Código UF']==23),
            (cageds['Código UF']==24),
            (cageds['Código UF']==25),
            (cageds['Código UF']==26),
            (cageds['Código UF']==27),
            (cageds['Código UF']==28),
            (cageds['Código UF']==29),
            (cageds['Código UF']==31),
            (cageds['Código UF']==32),
            (cageds['Código UF']==33),
            (cageds['Código UF']==35),
            (cageds['Código UF']==41),
            (cageds['Código UF']==42),
            (cageds['Código UF']==43),
            (cageds['Código UF']==51),
            (cageds['Código UF']==52),
            (cageds['Código UF']==53),
            (cageds['Código UF']==50)
            ]
    choices1 = ['Rondônia','Acre','Amazonas','Roraima','Pará','Amapá','Tocantins','Maranhão','Piaui','Ceará','Rio Grande do Norte','Paraiba','Pernambuco','Alagoas','Sergipe','Bahia','Minas Gerais','Espirito Santo','Rio de Janeiro','Sao Paulo','Parana','Santa Catarina','Rio Grande do Sul','Mato Grosso','Goias','Distrito Federal','Mato Grosso do Sul']
    cageds['Nome da UF'] = np.select(conditions1, choices1)
    choices2 = ['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MT','GO','DF','MS']
    cageds['Sigla da UF'] = np.select(conditions1, choices2)    

dropar = [1,2,3,4,5,6,7,8,9]

agrupado1 = cagedjan.groupby('Código do Município')
admitidos1 = agrupado1['Admitidos-Demitidos']
dif_ad1 = admitidos1.agg(np.sum)
cagedjan = (cagedjan.drop_duplicates('Código do Município'))
cagedjan.index = cagedjan['Código do Município']
cagedjan.sort_index(inplace=True)
cagedjan.drop(cagedjan.columns[[3,4,5,6]],inplace=True,axis=1)
cagedjan = pd.concat([cagedjan,dif_ad1],axis=1)

agrupado2 = cagedfev.groupby('Código do Município')
admitidos2 = agrupado2['Admitidos-Demitidos']
dif_ad2 = admitidos2.agg(np.sum)
cagedfev = (cagedfev.drop_duplicates('Código do Município'))
cagedfev.index = cagedfev['Código do Município']
cagedfev.sort_index(inplace=True)
cagedfev.drop(cagedfev.columns[[dropar]],inplace=True,axis=1)
cagedfev = pd.concat([cagedfev,dif_ad2],axis=1)

agrupado3 = cagedmar.groupby('Código do Município')
admitidos3 = agrupado3['Admitidos-Demitidos']
dif_ad3 = admitidos3.agg(np.sum)
cagedmar = (cagedmar.drop_duplicates('Código do Município'))
cagedmar.index = cagedmar['Código do Município']
cagedmar.sort_index(inplace=True)
cagedmar.drop(cagedmar.columns[[dropar]],inplace=True,axis=1)
cagedmar = pd.concat([cagedmar,dif_ad3],axis=1)

agrupado4 = cagedabr.groupby('Código do Município')
admitidos4 = agrupado4['Admitidos-Demitidos']
dif_ad4 = admitidos4.agg(np.sum)
cagedabr = (cagedabr.drop_duplicates('Código do Município'))
cagedabr.index = cagedabr['Código do Município']
cagedabr.sort_index(inplace=True)
cagedabr.drop(cagedabr.columns[[dropar]],inplace=True,axis=1)
cagedabr = pd.concat([cagedabr,dif_ad4],axis=1)

agrupado5 = cagedmai.groupby('Código do Município')
admitidos5 = agrupado5['Admitidos-Demitidos']
dif_ad5 = admitidos5.agg(np.sum)
cagedmai = (cagedmai.drop_duplicates('Código do Município'))
cagedmai.index = cagedmai['Código do Município']
cagedmai.sort_index(inplace=True)
cagedmai.drop(cagedmai.columns[[dropar]],inplace=True,axis=1)
cagedmai = pd.concat([cagedmai,dif_ad5],axis=1)

agrupado6 = cagedjun.groupby('Código do Município')
admitidos6 = agrupado6['Admitidos-Demitidos']
dif_ad6 = admitidos6.agg(np.sum)
cagedjun = (cagedjun.drop_duplicates('Código do Município'))
cagedjun.index = cagedjun['Código do Município']
cagedjun.sort_index(inplace=True)
cagedjun.drop(cagedjun.columns[[dropar]],inplace=True,axis=1)
cagedjun = pd.concat([cagedjun,dif_ad6],axis=1)

agrupado7 = cagedjul.groupby('Código do Município')
admitidos7 = agrupado7['Admitidos-Demitidos']
dif_ad7 = admitidos7.agg(np.sum)
cagedjul = (cagedjul.drop_duplicates('Código do Município'))
cagedjul.index = cagedjul['Código do Município']
cagedjul.sort_index(inplace=True)
cagedjul.drop(cagedjul.columns[[dropar]],inplace=True,axis=1)
cagedjul = pd.concat([cagedjul,dif_ad7],axis=1)

agrupado8 = cagedaug.groupby('Código do Município')
admitidos8 = agrupado8['Admitidos-Demitidos']
dif_ad8 = admitidos8.agg(np.sum)
cagedaug = (cagedaug.drop_duplicates('Código do Município'))
cagedaug.index = cagedaug['Código do Município']
cagedaug.sort_index(inplace=True)
cagedaug.drop(cagedaug.columns[[dropar]],inplace=True,axis=1)
cagedaug = pd.concat([cagedaug,dif_ad8],axis=1)

cagedest_emp = pd.merge(left=cagedjan,right=cagedfev,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedmar,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedabr,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedmai,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedjun,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedjul,on='Código do Município',left_index=True,how='left')
cagedest_emp = pd.merge(left=cagedest_emp,right=cagedaug,on='Código do Município',left_index=True,how='left')

#cagedest_emp.rename(columns={cagedest_emp.columns[6]: "Variacao Emprego - Jan/2020",
                            # cagedest_emp.columns[8]: "Variacao Emprego - Fev/2020",
                             #cagedest_emp.columns[10]: "Variacao Emprego - Mar/2020",
                             #cagedest_emp.columns[12]: "Variacao Emprego - Abr/2020",
                             #cagedest_emp.columns[14]: "Variacao Emprego - Mai/2020",
                             #cagedest_emp.columns[16]: "Variacao Emprego - Jun/2020",
                             #cagedest_emp.columns[18]: "Variacao Emprego - Jul/2020",
                             #cagedest_emp.columns[18]: "Variacao Emprego - Jul/2020"},inplace = True,axis=1)

cagedest_emp.drop(cagedest_emp.columns[[0,7,9,11,13,15,17]],inplace=True,axis=1)

cagedest_emp = cagedest_emp.replace('nan',0)
cagedest_emp = cagedest_emp.replace(np.nan,0)
cagedest_emp = cagedest_emp.fillna(0)

cagedest_emp.to_excel(excel_writer='/Users/lucasiancsamuels/Desktop/Res. Regional - COVID 19/Estrutura de Dados.xls')
