#%%

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#definindo como df o arquivo que será utilizado para analisar os dados
df = pd.read_csv('NFLX.csv')


#todos os dados de todas as colunas do dataset
lista=[]
count = len(df.columns)

for coluna in range(count):
    lista.append(df.iloc[:,coluna])
   

#%%

plt.subplot(1,3,3)
#grafico linear
plt.plot(lista[1],lista[0])
plt.show()


#grafico em barra
sns.barplot(data=df,x=lista[1],y=lista[0])
plt.show()

#grafico de pizza
plt.pie(lista[1], autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis("equal")
plt.show()


# %%
