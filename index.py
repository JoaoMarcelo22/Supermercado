import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Dados.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


categoria = df.groupby('Categoria').size().reset_index(name='categoria')
categoria.plot(kind='pie', y='categoria',labels=categoria['Categoria'], autopct='%1.1f%%', legend=False)
plt.ylabel('')
plt.title('Categorias')

df['Faixa_etaria'] = pd.cut(df['Idade'], bins=range(10, 90, 10))
ct = pd.crosstab(df['Faixa_etaria'],df['Sexo'])
ax = ct.plot.bar()
ax.set_xlabel('Faixa Etária')
ax.set_ylabel('Quantidade')
plt.show()

estado = df.groupby('Estado').size().reset_index(name='estado')
estado['indice'] = range(len(estado))
ax = estado.plot(kind='bar',x='indice',y='estado', tick_label=estado['Estado'],legend=False)
ax.set_xticklabels(estado['Estado'])
plt.title('Resumo entre Estados')
plt.xlabel('Estados')
plt.ylabel('quantidade')
plt.show()
