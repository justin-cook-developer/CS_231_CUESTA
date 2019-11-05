import json

jsonFile = open('WU-SLO-forecast-10day.json', 'r')
data = json.load(jsonFile)
jsonFile.close()

simpleforecast = data['forecast']['simpleforecast']['forecastday']


# print functions
def printDateInfo(date):
    message_template = "This is the data for {}, {} {} {}."
    print(message_template.format(
        date["weekday"], date["monthname"], date["day"], date["year"]))


def printTodaysConditions(condition):
    message_template = "The conditions are {}."
    print(message_template.format(condition.lower()))


def printHighAndLowTemps(high, low):
    message_template = "In the format of (fahrenheit, celsius), the high is ({}, {}) and the low is ({}, {})."

    print(message_template.format(
        high["fahrenheit"], high["celsius"], low["fahrenheit"], low["celsius"]))


def printWindInfo(avewind):
    message_template = "The wind is moving {} at {} mph."
    print(message_template.format(avewind["dir"], avewind["mph"]))


def printAvgHumidity(humidity):
    print("The average humidity is {}.".format(humidity))


def printForecastData(forecast):
    printDateInfo(forecast["date"])
    printTodaysConditions(forecast["conditions"])
    printHighAndLowTemps(forecast["high"], forecast["low"])
    printWindInfo(forecast["avewind"])
    printAvgHumidity(forecast["avehumidity"])


def printForecasts(forecasts):
    for i in range(0, len(forecasts)):
        printForecastData(forecasts[i])

        if i != len(forecasts) - 1:
            print("\n------------------\n")


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


def main(forecasts):
    print("------ ** Here is a day by day summary ** -----\n")

    printForecasts(forecasts)

    print("\n------ ** Here are the highest and lowest temperatures. ** -----\n")

    (minForecast, maxForecast) = findHighestAndLowestTempForecasts(forecasts)

    printHighAndLowTemps(maxForecast["high"], minForecast["low"])

    print("\n------ ** Here are the average high and low temperatures. ** -----\n")

    (lowAvg, highAvg) = avgHighAndLow(forecasts)

    print("In Fahrenheit, the average high is {} and the average low is {}.".format(
        highAvg, lowAvg))

    print("\n------ ** Here are the most frequently occuring Conditions. ** -----\n")

    conditions = listMostCommonConditions(conditionsFrequencies(forecasts))

    print("From most frequent to least frequent:\n")

    for condition in conditions:
      print(condition[0] + '\n')



main(simpleforecast)
