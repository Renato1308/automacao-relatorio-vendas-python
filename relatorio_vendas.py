import pandas as pd

#Ler a planilha
arquivo = "vendas.xlsx"
df = pd.read_excel(arquivo, engine="openpyxl")

# Criar coluna de total
df["Total"] = df["Quantidade"] * df["Valor Unitário"]

# Calcular total geral
total_geral = df["Total"].sum()

#Produto mais vendido
produto_top = df.loc[df["Total"].idxmax(), "Produto"]

#Gerar relatório em texto
with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO AUTOMÁTICO DE VENDAS\n")
    arquivo.write("=" * 40 + "\n\n")
    arquivo.write(f"Total geral vendido: R$ {total_geral:.2f}\n")
    arquivo.write(f"Produto com maior faturamento: {produto_top}\n\n")
    arquivo.write("Detalhamento por produto:\n\n")
    arquivo.write(df.to_string (index=False))
    
print("Relatório gerado com sucesso: relatorio.txt")
    