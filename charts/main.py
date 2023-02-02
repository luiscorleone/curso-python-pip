import utils
import leer_archivo_csv
import charts

def run():
    data = leer_archivo_csv.('./app/data.csv')
    data = list(filter(lambda item : item['Continent']=='South America',data))

    countries = list(map(lambda x : x['Country'], data))
    percentages = list(map(lambda x : x['World Population Porcentage'],data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')

    result = utils.population_by_country

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()