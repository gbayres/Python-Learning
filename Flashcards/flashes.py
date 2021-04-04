import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("dados2.csv")
SCORE_INDEX = df.columns.get_loc('Score')
TIME_INDEX = df.columns.get_loc("Tempo")

##### Calcular score conforme tempo
for i in range(len(df.index)):
    DIFERENCA = dt.today().timestamp() - df.iloc[i, TIME_INDEX]

    SEGUNDOS = DIFERENCA / 1000
    
    DIAS = int(SEGUNDOS / (24 * 60 * 60))

    INTERVALO = int(DIAS / 5)

    df.iloc[i, SCORE_INDEX] += INTERVALO


#####################################


lines = df.nlargest(50,"Score").index

for i in lines:
    current = df.iloc[i,]
    input(str(current.Frente) + '\n')
    answer = input(str(current.Verso) + '\n\n' + "Acertou?\n" )

    df.iloc[i, TIME_INDEX] = dt.today().timestamp()
    
    if answer != "":
        df.iloc[i, SCORE_INDEX] += 1
    else:
        df.iloc[i, SCORE_INDEX] -= 1
        
def novaEntrada(frente, verso, tema):
    pass

with open("dados2.csv", 'w') as file:
	file.write(df.to_csv(index=False))

