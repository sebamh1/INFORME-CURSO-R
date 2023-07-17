# ------------------- LIBRERÍAS ------------------ #
import pandas as pd


# ------------------- PASO 1: ------------------ #
# Pregunta de Investigación:
# ¿Es la piscicultura un indicador de la calidad y expectativa de vida de las naciones en el mundo?

# ------------------- PASO 2: SELECCIÓN DE DATA ------------------ #
# Set de datos a utilizar:
csv_path_fish_production = "aquaculture-farmed-fish-production.csv"
csv_path_life_expec = "life-expectancy.csv"
csv_path_pou = "prevalence-of-undernourishment.csv"


# ------------------- PASO 3: DATA WRANGLING ------------------ #

# Leer los archivos CSV
fp = csv_path_fish_production
le = csv_path_life_expec
pou = csv_path_pou

df_1 = pd.read_csv(fp)
df_2 = pd.read_csv(le)
df_3 = pd.read_csv(pou)

# Imprimir raw DataFrame para analizar visualmente las diferencias de cada set de datos en los archivos .csv
"""
print(df_1)
print(" ")
print(df_2)
print(" ")
print(df_3)
"""

# Pandas Display Options ----------------------------------------------
# Set display options to show all columns and rows
# pd.set_option("display.max_columns", 6)  # Show all columns
# pd.set_option("display.max_rows", None)  # Show all rows
# pd.set_option("display.width", 10)  # Adjust the width of the display


# ------------------------------------------------------------------------ #
# SELECCIÓN DE DATOS
# Seleccionar la primera columna con el nombre de los paises
country_column_fp = df_1.iloc[:, 0]
country_column_le = df_2.iloc[:, 0]
country_column_pou = df_3.iloc[:, 0]

# Seleccionar la tercera columna con los años
years_column_fp = df_1.iloc[:, 2]
years_column_le = df_2.iloc[:, 2]
years_column_pou = df_3.iloc[:, 2]


# Obtener el nombre de cada país en la lista
unique_fp = country_column_fp.unique()
unique_le = country_column_le.unique()
unique_pou = country_column_pou.unique()

# Obtener la cantidad de paises en la lista
num_unique_fp = len(unique_fp)
num_unique_le = len(unique_le)
num_unique_pou = len(unique_pou)


# ------------------------------------------------------------------------ #
# INTERSECCIONES
# Set de datos para intersectar y obtener solo los nombres de países presentes en los tres archivos csv
countries_fp = set(unique_fp)
countries_le = set(unique_le)
countries_pou = set(unique_pou)

repeated_countries = countries_fp.intersection(countries_le, countries_pou)

sorted_countries = sorted(repeated_countries)
sorted_countries.remove("World")

extract_country_1 = df_1.loc[df_1["Entity"].isin(sorted_countries)]
extract_country_2 = df_2.loc[df_2["Entity"].isin(sorted_countries)]
extract_country_3 = df_3.loc[df_3["Entity"].isin(sorted_countries)]

# Set de datos para intersectar y obtener solo los años presentes en los tres archivos csv
years_fp = set(years_column_fp)
years_le = set(years_column_le)
years_pou = set(years_column_pou)

repeated_years = years_fp.intersection(years_le, years_pou)

sorted_years = sorted(repeated_years)

extract_year_1 = extract_country_1.loc[extract_country_1["Year"].isin(sorted_years)]
extract_year_2 = extract_country_2.loc[extract_country_2["Year"].isin(sorted_years)]
extract_year_3 = extract_country_3.loc[extract_country_3["Year"].isin(sorted_years)]

extract_year_1 = extract_year_1.drop("Code", axis=1)
extract_year_2 = extract_year_2.drop("Code", axis=1)
extract_year_3 = extract_year_3.drop("Code", axis=1)

extract_year_1 = extract_year_1.set_index("Year")
extract_year_2 = extract_year_2.set_index("Year")
extract_year_3 = extract_year_3.set_index("Year")

"""
extract_year_1 = df_1.loc[df_1["Year"].isin(sorted_years)]
extract_year_2 = df_2.loc[df_2["Year"].isin(sorted_years)]
extract_year_3 = df_3.loc[df_3["Year"].isin(sorted_years)]
"""
extract_year_1.to_csv("fp.csv", encoding="utf-8", index=False, sep=";")
extract_year_2.to_csv("le.csv", encoding="utf-8", index=False, sep=";")
extract_year_3.to_csv("pou.csv", encoding="utf-8", index=False, sep=";")

# ------------------------------------------------------------------------ #
# DATAFRAMES
## Crear un df con los países repetidos
# fix_df = pd.DataFrame({"Country": list(sorted_countries)})

# fixed_df = df.drop(index=152)

# ------------------------------------------------------------------------ #
# JOINTS
"""
inner_join = pd.merge(
    extract_year_1, extract_year_2, on="Entity", how="inner"
).drop_duplicates()
# inner_join_2 = pd.merge(inner_join, df_3, on="Year", how="inner")
# .drop_duplicates()
"""

# ------------------------------------------------------------------------ #
# OUTPUTS
# ------- Países
# Imprimir el output
# print("Cantidad de países considerados en el set de datos fp: ", num_unique_fp)
# print("Cantidad de países considerados en el set de datos le: ", num_unique_le)
# print("Cantidad de países considerados en el set de datos pou: ", num_unique_pou)

# print(fixed_df)
# print(sorted_countries)

# ----- Años
# print(years_column_fp)
# print(years_column_le)
# print(years_column_pou)

# print(sorted_years)

# ----- Data Frames
# print(extract_country_1)
# print(extract_country_2)
# print(extract_country_3)


print(extract_year_1)
print(extract_year_2)
print(extract_year_3)


# print(inner_join)
# inner_join.describe()
# print(inner_join.head(500))
