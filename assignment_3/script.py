# CIS 231 / Scovil
# Assignment 3
# Justin Cook / justin_cook3@my.cuesta.edu

import json

jsonFile = open('WU-SLO-forecast-10day.json', 'r')
data = json.load(jsonFile)
jsonFile.close()

simpleforecast = data['forecast']['simpleforecast']['forecastday']


# print functions
def printMyInfo(forecasts):
    message_template = "Assignment 3 - SLO 10-Day Forecast Summary for {} through {}.\n"
    print(message_template.format(
        forecasts[0]["date"]["pretty"], forecasts[len(forecasts) - 1]["date"]["pretty"]))


def printDateInfo(date):
    message_template = "This is the data for {}, {} {} {}."
    print(message_template.format(
        date["weekday"], date["monthname"], date["day"], date["year"]))


def printTodaysConditions(condition):
    message_template = "Conditions: {:>22}{}"
    print(message_template.format(" ", condition))


def printHighAndLowTemps(high, low):
    print("High: {:>30}ºF or {}ºC".format(
        high["fahrenheit"], high["celsius"]))
    print("Low: {:>31}ºF or {}ºC".format(
        low["fahrenheit"], low["celsius"]))


def printWindInfo(avewind):
    print("Avg wind speed (mph): {:>14}".format(avewind["mph"]))
    print("Wind direction: {:>18}{}".format(" ", avewind["dir"]))


def printAvgHumidity(humidity):
    print("Avg humidity: {:>22}".format(humidity))


def printForecastData(forecast):
    printDateInfo(forecast["date"])
    printTodaysConditions(forecast["conditions"])
    printHighAndLowTemps(forecast["high"], forecast["low"])
    printWindInfo(forecast["avewind"])
    printAvgHumidity(forecast["avehumidity"])


def printForecasts(forecasts):
    print("------ ** Here is a day by day summary ** ------\n")

    for i in range(0, len(forecasts)):
        printForecastData(forecasts[i])

        if i != len(forecasts) - 1:
            print()


def printHighestAndLowest(high, low):
    print("\n------ ** Here are the highest and lowest temperatures. ** -----\n")

    printHighAndLowTemps(high, low)


def printAverageHighLow(highAvg, lowAvg):
    print("\n------ ** Here are the average high and low temperatures. ** -----\n")

    print("High: {:>32}ºF".format(highAvg))
    print("Low: {:>33}ºF".format(lowAvg))


def printMostFrequentCondititons(conditions):
    print("\n------ ** Here are the most frequently occuring conditions, from most frequent to least frequent. ** -----\n")

    for condition in conditions:
        print(condition[0] + '\n')


# non side affect functions
def findHighestAndLowestTempForecasts(forecasts):
    if (len(forecasts) == 0):
        return None

    minForecast = forecasts[0]
    maxForecast = forecasts[0]

    for forecast in forecasts:
        if int(forecast["high"]["fahrenheit"]) > int(maxForecast["high"]["fahrenheit"]):
            maxForecast = forecast

        if int(forecast["low"]["fahrenheit"]) < int(minForecast["low"]["fahrenheit"]):
            minForecast = forecast

    return (minForecast, maxForecast)


def avgHighAndLow(forecasts):
    lowTotal = 0.0
    highTotal = 0.0

    for forecast in forecasts:
        lowTotal = lowTotal + int(forecast["low"]["fahrenheit"])
        highTotal = highTotal + int(forecast["high"]["fahrenheit"])

    return (lowTotal / len(forecasts), highTotal / len(forecasts))


def conditionsFrequencies(forecasts):
    frequencies = {}

    for forecast in forecasts:
        condition = forecast["conditions"]
        frequencies[condition] = frequencies.get(condition, 0) + 1

    return frequencies


def listMostCommonConditions(frequencies):
    items = list(frequencies.items())

    def sortByFrequency(tupl):
        return tupl[1]

    items.sort(key=sortByFrequency, reverse=True)

    return items


# main method
def main(forecasts):
    printMyInfo(forecasts)

    printForecasts(forecasts)

    (minForecast, maxForecast) = findHighestAndLowestTempForecasts(forecasts)

    printHighestAndLowest(maxForecast["high"], minForecast["low"])

    (lowAvg, highAvg) = avgHighAndLow(forecasts)

    printAverageHighLow(highAvg, lowAvg)

    conditions = listMostCommonConditions(conditionsFrequencies(forecasts))

    printMostFrequentCondititons(conditions)


# call main
main(simpleforecast)
