#  Funcion q recibe el diccionario de un pais y filtra las columnas q necesita ej: '2022 Population' 
def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']), # las claves se crean manualmente porque ya las conocemos al tener el archivo csv
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

# data = [
#     {
#         'Country': 'Colombia',
#         'population': 500
#     },
#     {
#         'Country': 'Bolivia',
#         'population': 300
#     }
# ]

# funcion q recibe un archivo csv transformado a diccionarios # q retorna el diccionario 
# q contiene ese pais con alguna coincidencia por ej: 'Country/Territory'] == country
def population_by_country(data,country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

# aqui la invocamos
# result = population_by_country(data, 'Colombia')
# print(result)

