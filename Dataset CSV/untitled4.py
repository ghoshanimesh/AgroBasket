# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QdCJU2K_8ZFihOe57g54IztPY8o3LL6K
"""

import pandas as pd
df_wd = pd.read_csv ('WeatherData.csv')
df_final = pd.DataFrame(columns=['Crop', 'State', 'District', 'Season' ,'SowingMonth', 'MinTemp', 'MaxTemp', 'SoilPHMin', 'SoilPHMax', 'MinRainfall','MaxRainfall'])
print(df_final)

df_bajara = pd.read_csv ('Bajra.csv')

df_wd_bajra = df_wd.loc[df_wd['Crop'] == "Bajra"]
df_bajara_kharif = df_bajara.loc[df_bajara['Kharif'] == 1]
df_wd_bajara_kharif = df_wd_bajra.loc[df_wd_bajra['Season'] == "Kharif"]
df_bajara_summer = df_bajara.loc[df_bajara['Summer'] == 1]
df_wd_bajara_summer = df_wd_bajra.loc[df_wd_bajra['Season'] == "Summer"]
#print(len(df_bajara_kharif) + len (df_bajara_summer))
for index, row in df_bajara_kharif.iterrows(): 
    res = df_wd_bajara_kharif.loc[df_wd_bajara_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Bajra","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_bajara_summer.iterrows(): 
    res = df_wd_bajara_summer.loc[df_wd_bajara_summer['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Bajara","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_cashewnut = pd.read_csv ('Cashewnut.csv')

df_wd_cashewnut = df_wd.loc[df_wd['Crop'] == "Cashewnut"]

df_cashewnut_kharif = df_cashewnut.loc[df_cashewnut['Kharif'] == 1]
df_wd_cashewnut_kharif = df_wd_cashewnut.loc[df_wd_cashewnut['Season'] == "Kharif"]

df_cashewnut_rabi = df_cashewnut.loc[df_cashewnut['Rabi'] == 1]
df_wd_cashewnut_rabi = df_wd_cashewnut.loc[df_wd_cashewnut['Season'] == "Rabi"]

df_cashewnut_wholeyear = df_cashewnut.loc[df_cashewnut['Whole Year'] == 1]
df_wd_cashewnut_wholeyear = df_wd_cashewnut.loc[df_wd_cashewnut['Season'] == "WholeYear"]


for index, row in df_cashewnut_kharif.iterrows(): 
    res = df_wd_cashewnut_kharif.loc[df_wd_cashewnut_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Cashewnut","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_cashewnut_rabi.iterrows(): 
    res = df_wd_cashewnut_rabi.loc[df_wd_cashewnut_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Cashewnut","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_cashewnut_wholeyear.iterrows(): 
    res = df_wd_cashewnut_wholeyear.loc[df_wd_cashewnut_wholeyear['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Cashewnut","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_coconut = pd.read_csv ('Coconut.csv')

df_wd_coconut = df_wd.loc[df_wd['Crop'] == "Coconut"]

df_coconut_wholeyear = df_coconut.loc[df_coconut['WholeYear'] == 1]
df_wd_coconut_wholeyear = df_wd_coconut.loc[df_wd_coconut['Season'] == "WholeYear"]


for index, row in df_coconut_wholeyear.iterrows(): 
    res = df_wd_coconut_wholeyear.loc[df_wd_coconut_wholeyear['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Coconut","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_cotton = pd.read_csv ('Cotton.csv')

df_wd_cotton = df_wd.loc[df_wd['Crop'] == "Cotton"]

df_cotton_kharif = df_cotton.loc[df_cotton['Kharif'] == 1]
df_wd_cotton_kharif = df_wd_cotton.loc[df_wd_cotton['Season'] == "Kharif"]

df_cotton_rabi = df_cotton.loc[df_cotton['Rabi'] == 1]
df_wd_cotton_rabi = df_wd_cotton.loc[df_wd_cotton['Season'] == "Rabi"]


for index, row in df_cotton_kharif.iterrows(): 
    res = df_wd_cotton_kharif.loc[df_wd_cotton_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Cotton","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_cotton_rabi.iterrows(): 
    res = df_wd_cotton_rabi.loc[df_wd_cotton_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Cotton","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_gram = pd.read_csv ('Gram.csv')

df_wd_gram = df_wd.loc[df_wd['Crop'] == "Gram"]

df_gram_rabi = df_gram.loc[df_gram['Rabi'] == 1]
df_wd_gram_rabi = df_wd_gram.loc[df_wd_gram['Season'] == "Rabi"]

for index, row in df_gram_rabi.iterrows(): 
    res = df_wd_gram_rabi.loc[df_wd_gram_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Gram","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_jowar = pd.read_csv ('Jowar.csv')

df_wd_jowar = df_wd.loc[df_wd['Crop'] == "Jowar"]

df_jowar_kharif = df_jowar.loc[df_jowar['Kharif'] == 1]
df_wd_jowar_kharif = df_wd_jowar.loc[df_wd_jowar['Season'] == "Kharif"]

df_jowar_rabi = df_jowar.loc[df_jowar['Rabi'] == 1]
df_wd_jowar_rabi = df_wd_jowar.loc[df_wd_jowar['Season'] == "Rabi"]


for index, row in df_jowar_kharif.iterrows(): 
    res = df_wd_jowar_kharif.loc[df_wd_jowar_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Jowar","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_jowar_rabi.iterrows(): 
    res = df_wd_jowar_rabi.loc[df_wd_jowar_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Jowar","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_rice = pd.read_csv ('Rice.csv')

df_wd_rice = df_wd.loc[df_wd['Crop'] == "Rice"]

df_rice_kharif = df_rice.loc[df_rice['Kharif'] == 1]
df_wd_rice_kharif = df_wd_rice.loc[df_wd_rice['Season'] == "Kharif"]

df_rice_rabi = df_rice.loc[df_rice['Rabi'] == 1]
df_wd_rice_rabi = df_wd_rice.loc[df_wd_rice['Season'] == "Rabi"]

df_rice_autumn = df_rice.loc[df_rice['Autumn'] == 1]
df_wd_rice_autumn = df_wd_rice.loc[df_wd_rice['Season'] == "Autumn"]

df_rice_winter = df_rice.loc[df_rice['Winter'] == 1]
df_wd_rice_winter = df_wd_rice.loc[df_wd_rice['Season'] == "Winter"]

for index, row in df_rice_kharif.iterrows(): 
    res = df_wd_rice_kharif.loc[df_wd_rice_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Rice","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_rice_rabi.iterrows(): 
    res = df_wd_rice_rabi.loc[df_wd_rice_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Rice","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

for index, row in df_rice_autumn.iterrows(): 
    res = df_wd_rice_autumn.loc[df_wd_rice_autumn['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Rice","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

for index, row in df_rice_winter.iterrows(): 
    res = df_wd_rice_winter.loc[df_wd_rice_winter['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Rice","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_small_millets = pd.read_csv ('Small Millets.csv')

df_wd_small_millets = df_wd.loc[df_wd['Crop'] == "Small Millets"]

df_small_millets_kharif = df_small_millets.loc[df_small_millets['Kharif'] == 1]
df_wd_small_millets_kharif = df_wd_small_millets.loc[df_wd_small_millets['Season'] == "Kharif"]

df_small_millets_rabi = df_small_millets.loc[df_small_millets['Rabi'] == 1]
df_wd_small_millets_rabi = df_wd_small_millets.loc[df_wd_small_millets['Season'] == "Rabi"]


for index, row in df_small_millets_kharif.iterrows(): 
    res = df_wd_small_millets_kharif.loc[df_wd_small_millets_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Small Millets","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_small_millets_rabi.iterrows(): 
    res = df_wd_small_millets_rabi.loc[df_wd_small_millets_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Small Millets","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_soyabean = pd.read_csv ('Soyabean.csv')

df_wd_soyabean = df_wd.loc[df_wd['Crop'] == "Soyabean"]

df_soyabean_kharif = df_soyabean.loc[df_soyabean['Kharif'] == 1]
df_wd_soyabean_kharif = df_wd_soyabean.loc[df_wd_soyabean['Season'] == "Kharif"]

for index, row in df_soyabean_kharif.iterrows(): 
    res = df_wd_soyabean_kharif.loc[df_wd_soyabean_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Soyabean","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_tobacco = pd.read_csv ('Tobacco.csv')

df_wd_tobacco = df_wd.loc[df_wd['Crop'] == "Tobacco"]

df_tobacco_kharif = df_tobacco.loc[df_tobacco['Kharif'] == 1]
df_wd_tobacco_kharif = df_wd_tobacco.loc[df_wd_tobacco['Season'] == "Kharif"]

df_tobacco_rabi = df_tobacco.loc[df_tobacco['Rabi'] == 1]
df_wd_tobacco_rabi = df_wd_tobacco.loc[df_wd_tobacco['Season'] == "Rabi"]

df_tobacco_whole_year = df_tobacco.loc[df_tobacco['WholeYear'] == 1]
df_wd_tobacco_whole_year = df_wd_tobacco.loc[df_wd_tobacco['Season'] == "WholeYear"]

df_tobacco_summer = df_tobacco.loc[df_tobacco['Summer'] == 1]
df_wd_tobacco_summer = df_wd_tobacco.loc[df_wd_tobacco['Season'] == "Summer"]

for index, row in df_tobacco_kharif.iterrows(): 
    res = df_wd_tobacco_kharif.loc[df_wd_tobacco_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tobacco","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_tobacco_rabi.iterrows(): 
    res = df_wd_tobacco_rabi.loc[df_wd_tobacco_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tobacco","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

for index, row in df_tobacco_whole_year.iterrows(): 
    res = df_wd_tobacco_whole_year.loc[df_wd_tobacco_whole_year['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tobacco","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

for index, row in df_tobacco_summer.iterrows(): 
    res = df_wd_tobacco_summer.loc[df_wd_tobacco_summer['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tobacco","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_tur = pd.read_csv ('Tur.csv')

df_wd_tur = df_wd.loc[df_wd['Crop'] == "Tur"]

df_tur_kharif = df_tur.loc[df_tur['Kharif'] == 1]
df_wd_tur_kharif = df_wd_tur.loc[df_wd_tur['Season'] == "Kharif"]

df_tur_rabi = df_tur.loc[df_tur['Rabi'] == 1]
df_wd_tur_rabi = df_wd_tur.loc[df_wd_tur['Season'] == "Rabi"]


for index, row in df_tur_kharif.iterrows(): 
    res = df_wd_tur_kharif.loc[df_wd_tur_kharif['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tur","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)


for index, row in df_tur_rabi.iterrows(): 
    res = df_wd_tur_rabi.loc[df_wd_tur_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Tur","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

df_wheat = pd.read_csv ('Wheat.csv')

df_wd_wheat = df_wd.loc[df_wd['Crop'] == "Wheat"]

df_wheat_rabi = df_wheat.loc[df_wheat['Rabi'] == 1]
df_wd_wheat_rabi = df_wd_wheat.loc[df_wd_wheat['Season'] == "Rabi"]


for index, row in df_wheat_rabi.iterrows(): 
    res = df_wd_wheat_rabi.loc[df_wd_wheat_rabi['State'] == row['State']]
    df_tobeadded = pd.DataFrame({"Crop": "Wheat","State":row['State'], "District":row['District'], "Season": res['Season'].values[0],"SowingMonth":res['SowingMonth'].values[0], "MinTemp" : res['MinTemp'].values[0], "MaxTemp": res['MaxTemp'].values[0], "SoilPHMin": res['SoilPHMin'].values[0], "SoilPHMax": res['SoilPHMax'].values[0], "MinRainfall": res['MinRainfall'].values[0],"MaxRainfall":res["MaxRainfall"].values[0]}, index=[0])
    df_final = df_final.append(df_tobeadded, ignore_index = True)

print(len(df_final))
print(df_final)
df_final.to_csv(r'Final.csv', index = False)