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
pd.set_option("display.max_columns", 10)  # Show all columns
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
# Set de datos para intersectar y filtrar solo los nombres de países presentes en los tres archivos csv
countries_fp = set(unique_fp)
countries_le = set(unique_le)
countries_pou = set(unique_pou)

repeated_countries = countries_fp.intersection(countries_le, countries_pou)

sorted_countries = sorted(repeated_countries)
sorted_countries.remove("World")

extract_country_1 = df_1.loc[df_1["Entity"].isin(sorted_countries)]
extract_country_2 = df_2.loc[df_2["Entity"].isin(sorted_countries)]
extract_country_3 = df_3.loc[df_3["Entity"].isin(sorted_countries)]

# Set de datos para intersectar y filtrar solo los años presentes en los tres archivos csv
years_fp = set(years_column_fp)
years_le = set(years_column_le)
years_pou = set(years_column_pou)

repeated_years = years_fp.intersection(years_le, years_pou)


sorted_years = sorted(repeated_years)

extract_year_1 = extract_country_1.loc[extract_country_1["Year"].isin(sorted_years)]
extract_year_2 = extract_country_2.loc[extract_country_2["Year"].isin(sorted_years)]
extract_year_3 = extract_country_3.loc[extract_country_3["Year"].isin(sorted_years)]


extract_year_1 = extract_year_1.drop("Code", axis=1)
# extract_year_1 = extract_year_1.drop("Entity", axis=1)
# extract_year_1 = extract_year_1.drop("Aquaculture production (metric tons)", axis=1)
extract_year_2 = extract_year_2.drop("Code", axis=1)
# extract_year_2 = extract_year_2.drop("Entity", axis=1)
# extract_year_2 = extract_year_2.drop("Year", axis=1)
# extract_year_2 = extract_year_2.drop("Life expectancy at birth (historical)", axis=1)
extract_year_3 = extract_year_3.drop("Code", axis=1)
# extract_year_3 = extract_year_3.drop("Entity", axis=1)
# extract_year_3 = extract_year_3.drop("Year", axis=1)
# extract_year_3 = extract_year_3.drop("Prevalence of undernourishment (% of population)", axis=1)


Value_1 = "Aquaculture production (metric tons)"
extract_year_1[Value_1] = extract_year_1[Value_1].round(1)
"""
extract_year_1 = extract_year_1.drop(index=0)
extract_year_2 = extract_year_2.drop(index=0)
extract_year_3 = extract_year_3.drop(index=0)



extract_year_1 = extract_year_1.set_index("Year")
extract_year_2 = extract_year_2.set_index("Year")
extract_year_3 = extract_year_3.set_index("Year")


extract_year_1 = df_1.loc[df_1["Year"].isin(sorted_years)]
extract_year_2 = df_2.loc[df_2["Year"].isin(sorted_years)]
extract_year_3 = df_3.loc[df_3["Year"].isin(sorted_years)]
"""
extract_year_1.to_csv("fp.csv", encoding="utf-8", index=False, sep=";")
extract_year_2.to_csv("le.csv", encoding="utf-8", index=False, sep=";")
extract_year_3.to_csv("pou.csv", encoding="utf-8", index=False, sep=";")

"""
result = extract_year_1[extract_year_1["Year"] == 2003]

# Print the rows with the year 2002 for each entity
for entity, group in result.groupby("Entity"):
    print("Entity:", entity)
    print(group)
    print()

grouped_data = pd.DataFrame(columns=extract_year_1.columns)

# Group the data by entity and append the rows to the new DataFrame
for entity, group in result.groupby("Entity"):
    grouped_data = grouped_data._append(group)

# Reset the index of the new DataFrame
grouped_data.reset_index(drop=True, inplace=True)

# Print the grouped DataFrame
print(grouped_data)

grouped_data.to_csv("grouped_data.csv", encoding="utf-8", index=False, sep=";")
"""
"""
grouped_data_list = []
for year in sorted_years:
    # Filter rows with the current year for each entity
    result = extract_year_1[extract_year_1["Year"] == year]

    # Create a new DataFrame to store the grouped results
    grouped_data = pd.DataFrame(columns=extract_year_1.columns)

    # Group the data by entity and append the rows to the new DataFrame
    for entity, group in result.groupby("Entity"):
        grouped_data = grouped_data._append(group)

    # Reset the index of the new DataFrame
    grouped_data.reset_index(drop=True, inplace=True)

    # Add the current year as a column in the grouped DataFrame
    grouped_data["Year"] = year

    # Append the grouped DataFrame to the list
    grouped_data_list.append(grouped_data)

# Print the grouped DataFrames for each year
for grouped_data in grouped_data_list:
    print(len(grouped_data))
    print()
"""
useful_years = [2001, 2016, 2017, 2018]


def create_grouped_data(year_list, data):
    # Function to save DataFrame to CSV
    def save_to_csv(dataframe, year):
        filename = f"fp_data_{year}.csv"
        dataframe.to_csv(filename, index=False)
        print(f"Saved {filename}")

    # Iterate over each year in the list
    grouped_data_list = []
    for year in year_list:
        # Filter rows with the current year for each entity
        result = data[data["Year"] == year]

        # Create a new DataFrame to store the grouped results
        grouped_data = pd.DataFrame(columns=data.columns)

        # Group the data by entity and append the rows to the new DataFrame
        for entity, group in result.groupby("Entity"):
            grouped_data = grouped_data._append(group)

        # Reset the index of the new DataFrame
        grouped_data.reset_index(drop=True, inplace=True)

        # Add the current year as a column in the grouped DataFrame
        grouped_data["Year"] = year

        # Append the grouped DataFrame to the list
        grouped_data_list.append(grouped_data)

        # Save the DataFrame to a CSV file
        # save_to_csv(grouped_data, year)

    return grouped_data_list


grouped_data_list_1 = create_grouped_data(useful_years, extract_year_1)
grouped_data_list_2 = create_grouped_data(useful_years, extract_year_2)
grouped_data_list_3 = create_grouped_data(useful_years, extract_year_3)


group_list = [grouped_data_list_1, grouped_data_list_2, grouped_data_list_3]

# Print the grouped DataFrames for each year
# for grouped_data in group_list:
#    print(grouped_data)
# print(type(grouped_data))

fp_2001 = group_list[0][0]
fp_2016 = group_list[0][1]
fp_2017 = group_list[0][2]
fp_2018 = group_list[0][3]


country_filter_0 = fp_2001.iloc[:, 0]
country_filter_1 = fp_2018.iloc[:, 0]
country_filter_2 = fp_2017.iloc[:, 0]
country_filter_3 = fp_2018.iloc[:, 0]

filter_0 = set(country_filter_0)
filter_1 = set(country_filter_1)
filter_2 = set(country_filter_2)
filter_3 = set(country_filter_3)

repeated_entities = filter_0.intersection(filter_1, filter_2, filter_3)

# list_test = [country_filter_0, country_filter_1, country_filter_2, country_filter_3]
# print(sorted(repeated_entities))
# print(len(sorted(repeated_entities)))
# print(fp_2001)

"""
print(sorted(filter_0))
print()
print(sorted(filter_1))
print()
print(sorted(filter_2))
print()
print(sorted(filter_3))
"""

# print(fp_2001)
# print(fp_2016)
# print(fp_2017)
# print(fp_2018)
print()

le_2001 = group_list[1][0]
# le_2001 = le_2001.drop("Entity", axis=1)
le_2001 = le_2001.drop("Year", axis=1)

le_2016 = group_list[1][1]
le_2016 = le_2016.drop("Entity", axis=1)
le_2016 = le_2016.drop("Year", axis=1)

le_2017 = group_list[1][2]
le_2017 = le_2017.drop("Entity", axis=1)
le_2017 = le_2017.drop("Year", axis=1)

le_2018 = group_list[1][3]
# le_2018 = le_2018.drop("Entity", axis=1)
le_2018 = le_2018.drop("Year", axis=1)

# print(le_2001)
# print(le_2016)
# print(le_2017)
# print(le_2018)

pou_2001 = group_list[2][0]
# pou_2001 = pou_2001.drop("Entity", axis=1)
pou_2001 = pou_2001.drop("Year", axis=1)

pou_2016 = group_list[2][1]
pou_2016 = pou_2016.drop("Entity", axis=1)
pou_2016 = pou_2016.drop("Year", axis=1)

pou_2017 = group_list[2][2]
pou_2017 = pou_2017.drop("Entity", axis=1)
pou_2017 = pou_2017.drop("Year", axis=1)

pou_2018 = group_list[2][3]
# pou_2018 = pou_2018.drop("Entity", axis=1)
pou_2018 = pou_2018.drop("Year", axis=1)

# print(pou_2001)
# print(pou_2016)
# print(pou_2017)
# print(pou_2018)


df_2018_fp = pd.merge(fp_2001, fp_2018, on="Entity", how="inner")
df_2018_le = pd.merge(le_2001, le_2018, on="Entity", how="inner")
df_2018_pou = pd.merge(pou_2001, pou_2018, on="Entity", how="inner")

# Reset the index
df_2018_fp = df_2018_fp.reset_index(drop=True)
df_2018_le = df_2018_le.reset_index(drop=True)
df_2018_pou = df_2018_pou.reset_index(drop=True)


# print(df_2018_fp)
# print(df_2018_le)
# print(df_2018_pou)

df_2001_2018_fp_le = pd.merge(df_2018_fp, df_2018_le, on="Entity", how="inner")
df_2001_2018_fp_le_pou = pd.merge(
    df_2001_2018_fp_le, df_2018_pou, on="Entity", how="inner"
)


# print(df_2001_2018_fp_le_pou)

# Reordenar las columnas
ordered_columns = [
    "Entity",
    "Year_x",
    "Aquaculture production (metric tons)_x",
    "Life expectancy at birth (historical)_x",
    "Prevalence of undernourishment (% of population)_x",
    "Year_y",
    "Aquaculture production (metric tons)_y",
    "Life expectancy at birth (historical)_y",
    "Prevalence of undernourishment (% of population)_y",
]


main_df = df_2001_2018_fp_le_pou.reindex(columns=ordered_columns)


print(main_df)


# ------------------------------------------------------------------------ #
# DATAFRAME
## Crear dataframes con los filtros aplicados
concat_df_2016 = pd.concat([fp_2016, le_2016], axis=1)
concat_df_2016 = pd.concat([concat_df_2016, pou_2016], axis=1)

concat_df_2017 = pd.concat([fp_2017, le_2017], axis=1)
concat_df_2017 = pd.concat([concat_df_2017, pou_2017], axis=1)

concat_df_2018 = pd.concat([fp_2018, le_2018], axis=1)
concat_df_2018 = pd.concat([concat_df_2018, pou_2018], axis=1)

"""
print(concat_df_2016)
print()
print(concat_df_2017)
print()
print(concat_df_2018)
"""

# print(concat_df_2016.describe().round(1))
# print()
# print(concat_df_2017.describe().round(1))
# print()
# print(concat_df_2018.describe().round(1))


# ------------------------------------------------------------------------ #
# JOINTS
"""
comparison = extract_year_2.compare(extract_year_3)
print(comparison)


inner_join = pd.merge(
    extract_year_2, extract_year_3, on="Year", how="outter"
).drop_duplicates()
# inner_join_2 = pd.merge(inner_join, df_3, on="Year", how="inner")
# .drop_duplicates()

inner_join = pd.merge(
    extract_year_2, extract_year_3, on="Year", how="outer"
).drop_duplicates()

inner_join.to_csv("join.csv", encoding="utf-8", index=False, sep=";")
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

# print(concatenated_columns)

# print(extract_year_1)
# print(extract_year_2)
# print(extract_year_3)


# print(inner_join.iloc[0])
# inner_join.describe()
# print(inner_join.head(500))

# print(type(useful_years[0]))

# print(type(sorted_years[0]))
