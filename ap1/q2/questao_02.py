import pandas as pd

associados = pd.Series([12000, 17500, 14300, 16000, 19500], index=["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"])

print("Arrecadado na semana:", associados.sum())
print("Media das receitas:", associados.mean())
print("Mais arrecadou:", associados.idxmax())