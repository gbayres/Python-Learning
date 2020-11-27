import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string 

df = pd.read_csv("data.csv")
print(df)
print(df.head())
