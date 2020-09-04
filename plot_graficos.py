#%%

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#definindo como df o arquivo que será utilizado para analisar os dados
df = pd.read_csv('NFLX.csv')

#todos os dados da segunda coluna do dataset
x=df.iloc[:,1]

#todos os dados da primeira coluna do dataset
y=df.iloc[:,0]
#%%

plt.subplot(1,3,3)

#grafico linear
plt.plot(x,y)
plt.show()

#grafico em barra
sns.barplot(data=df,x=x,y=y)
plt.show()

#grafico de pizza
plt.pie(x, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis("equal")
plt.show()
# %%
