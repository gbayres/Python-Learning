#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:53:57 2021

@author: gabriel
"""

import pandas as pd
import seaborn as sbn
import statistics as st

df = pd.read_csv("../dados/tempo.csv", sep=";")

#========Aparencia processing===================
to_exclude = set(df["Aparencia"].unique()) - {'chuva', 'nublado', 'sol'}

moda_aparencia = st.mode(df["Aparencia"])

df.loc[df["Aparencia"].isin(to_exclude), "Aparencia"] = moda_aparencia

#=========Temperatura processing===================

median_temp = st.median(filter(lambda a: type(a) in (int, float), df["Temperatura"]))

def criteria(item):
    if type(item) in (int, float):
        if -130 <= item <= 130:
            return False
    return True


df.loc[df["Temperatura"].apply(criteria), "Temperatura"] = median_temp

#=========Umidade processing =====================

median_umid = st.median(filter(lambda a: type(a) in (int, float), df["Umidade"]))

def criteria_umidade(item):
    if type(item) in (int, float):
        if 0 <= item <= 100:
            return False
    return True

df.loc[df["Umidade"].apply(criteria_umidade), "Umidade"] = median_umid

#========Vento processing ===================

mode_vento = st.mode(df["Vento"])

df["Vento"].fillna(mode_vento, inplace=True)