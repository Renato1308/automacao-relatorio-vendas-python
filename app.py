import pandas as pd
import matplotlib.pyplot as plt

# Ler arquivo CSV
df = pd.read_csv("vendas.csv")
df.columns = df.columns.str.strip()

print("DADOS DE VENDAS")
print(df)

# Criar coluna faturamento total
df["faturamento"] = df["vendas"] * df["valor"]


print("\nFATURAMENTO TOTAL")
print(df)

# Mostrar total geral
total = df["faturamento"].sum()
print(f"\nFaturamento geral da empresa: R$ {total}")

# Criar gráfico
df.plot(x="produto", y="faturamento", kind="bar")

plt.title("Faturamento por Produto")
plt.ylabel("Valor em R$")
plt.xlabel("Produtos")
plt.tight_layout()

plt.show()