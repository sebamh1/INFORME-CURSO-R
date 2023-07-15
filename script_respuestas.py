# ------------------- LIBRERÍAS ------------------ #
import pandas as pd


# ------------------- PASO 1: ------------------ #


# ------------------- PASO 2: SELECCIÓN DE DATA ------------------ #
# Set de datos a utilizar:

csv_path_fish_production = "aquaculture-farmed-fish-production.csv"
csv_path_life_expec = "life-expectancy.csv"
csv_path_pou = "prevalence-of-undernourishment.csv"


# ------------------- PASO 3: DATA WRANGLING ------------------ #
# Read the CSV file and create a DataFrame

fp = csv_path_fish_production
le = csv_path_life_expec
pou = csv_path_pou

df_1 = pd.read_csv(fp)
df_2 = pd.read_csv(le)
df_3 = pd.read_csv(pou)

# Imprimir raw DataFrame para analizar la magnitud de cada archivo .csv
"""
print(df_1)
print(" ")
print(df_2)
print(" ")
print(df_3)
"""

# Seleccionar la primera columna con el nombre de los paises
column_fp = df_1.iloc[:, 0]
column_le = df_2.iloc[:, 0]
column_pou = df_3.iloc[:, 0]

# Obtener el nombre de cada país en la lista
unique_fp = column_fp.unique()
unique_le = column_le.unique()
unique_pou = column_pou.unique()

# Obtener la cantidad de paises en la lista
num_unique_fp = len(unique_fp)
num_unique_le = len(unique_le)
num_unique_pou = len(unique_pou)

# Set de datos para intersectar y obtener solo los países presentes en los tres archivos csv
countries_fp = set(unique_fp)
countries_le = set(unique_le)
countries_pou = set(unique_pou)

repeated_countries = countries_fp.intersection(countries_le, countries_pou)

sorted_countries = sorted(repeated_countries)

## Crear un df con los países repetidos
repeated_df = pd.DataFrame({"Country": list(sorted_countries)})


# Imprimir el output
print("Cantidad de países considerados en el set de datos fp: ", num_unique_fp)
print("Cantidad de países considerados en el set de datos le: ", num_unique_le)
print("Cantidad de países considerados en el set de datos pou: ", num_unique_pou)

print(repeated_df)
"""
for country in unique_countries:
    print(country)
"""
