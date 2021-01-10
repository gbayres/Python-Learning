#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:51:59 2021

@author: gabriel
"""

import pandas as pd
import seaborn as srn
import statistics as st

dataset = pd.read_csv("../dados/Churn.csv", sep=";")

dataset.columns = ["Id","Score","Estado","Genero","Idade","Patrimonio","Saldo","Produtos","TemCartCredito",
                    "Ativo","Salario","Saiu"]

agrupado = dataset.groupby(["Estado"]).size()

# agrupado.plot.bar(color = "#009bbb")

print(dataset["Score"].describe())

# srn.boxplot(x=dataset["Score"])

# srn.displot(dataset['Score'])

# srn.boxplot(dataset["Idade"]).set_title("Qual é")

# dataset.loc[dataset['Genero'] ==  'M', 'Genero'] = "Masculino"
dataset.loc[dataset['Genero'] ==  'M'] = "Masculino"
dataset.loc[dataset['Genero'].isin( ['Fem','F'])] = "Feminino"
agrupado = dataset.groupby(['Genero']).size()