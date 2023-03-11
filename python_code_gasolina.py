import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gas_df = pd.read_csv('gasolina.csv')
gas_df.head(3)

gas_plot = sns.lineplot(x=gas_df['dia'], y=gas_df['venda'])

plt.xlabel("dia", fontdict={'size':14})
plt.ylabel("preço", fontdict={'size':14})
plt.title("Preço diário da gasolina", fontdict={'size':16, 'fontweight':'bold'})

gas_plot.figure.savefig('gasolina.png')