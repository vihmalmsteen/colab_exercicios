import pandas as pd
import matplotlib.pyplot as plt

gas_df = pd.read_csv('gasolina.csv')
gas_df.head(3)

plt.figure(figsize=(14,10))
plt.plot(gas_df['dia'], 
         gas_df['venda'], 
         lw=4, c='green')
plt.hlines(y=gas_df['venda'].mean(), 
           xmin=gas_df['dia'].min(), 
           xmax=gas_df['dia'].max(), 
           ls='--', lw=4, color='red')
plt.title('GASOLINA: PREÇO/DIA E MÉDIA', 
          fontdict={'fontweight':'bold', 'fontsize':16})
plt.xlabel('DIAS', 
           fontdict={'fontsize':16})
plt.ylabel('PREÇOS', 
           fontdict={'fontsize':16})
plt.xticks(size=16)
plt.yticks(size=16)
plt.grid(visible=True, ls='--')
plt.savefig('gasolina.png')