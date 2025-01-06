import pandas as pd

df = pd.read_excel('potpisi.xlsx')

# prazni redovi
missing_indices = df[df.isnull().any(axis=1)].index.tolist()
missing_indices = [i + 2 for i in missing_indices]  # +2 zbog indeksiranja
print("Redni brojevi redova sa nedostajućim poljima:")
print(missing_indices)

df_cleaned = df.dropna()

# dupli redovi
duplicate_indices = df_cleaned[df_cleaned.duplicated()].index.tolist()
duplicate_indices = [i + 2 for i in duplicate_indices]
print("Redni brojevi duplih redova:")
print(duplicate_indices)

df_final = df_cleaned.drop_duplicates()

# nova Excell tabela
df_final.to_excel('ispravljeni_potpisi.xlsx', index=False)

print("Provera završena i podaci su sačuvani u 'ispravljeni_potpisi.xlsx'")
