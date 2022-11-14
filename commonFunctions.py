#
from datetime import datetime
from itertools import count
from pytz import common_timezones, country_timezones, timezone
from flask_restx import reqparse
import pycountry
import json
import convertdate, os.path, pkgutil

#
def getAllAlphaCode2Countries():

    #
    returningListOfAlphaCode2Countries = []

    #
    for country in pycountry.countries:

        #
        returningListOfAlphaCode2Countries.append(country.alpha_2)

    #
    return returningListOfAlphaCode2Countries

#
def getCountriesListFromPattern(countriesList, pattern=None):

    #
    print("Soon")

#
def getAllHistoricalCountriesFromSort(field='name', order = "asc", pattern=None):

    #
    historicalCountriesFromField = []
    historicalSortedCountriesList = []

    #
    for country in pycountry.historic_countries:

        #
        if field == "name":

            #
            historicalCountriesFromField.append(country.name)
            
        #
        elif field == "alpha_2":

            #
            historicalCountriesFromField.append(country.alpha_2)

        #
        elif field == "alpha_3":

            #
            historicalCountriesFromField.append(country.alpha_3)

        #
        elif field == "numeric":

            #
            historicalCountriesFromField.append(country.numeric)

        #
        else:

            #
            raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    if order == "desc":

        #
        historicalCountriesFromField.sort(reverse=True)

    #
    else:

        #
        historicalCountriesFromField.sort()

    #
    for fieldValueForCurrentCountry in historicalCountriesFromField:

        #
        if field == "name":

            #
            historicalSortedCountriesList.append(pycountry.historic_countries.get(name=fieldValueForCurrentCountry))

        #
        elif field == "alpha_2":

            #
            historicalSortedCountriesList.append(pycountry.historic_countries.get(alpha_2=fieldValueForCurrentCountry))

        #
        elif field == "alpha_3":

            #
            historicalSortedCountriesList.append(pycountry.historic_countries.get(alpha_3=fieldValueForCurrentCountry))

        #
        elif field == "numeric":

            #
            historicalSortedCountriesList.append(pycountry.historic_countries.get(numeric=fieldValueForCurrentCountry))

        #
        else:

            #
            raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    return historicalSortedCountriesList

#
def getAllCountriesFromSort(field='name', order = "asc", pattern=None):

    #
    countriesFromField = []
    sortedCountriesList = []

    #
    for country in pycountry.countries:

        #
        if field == "name":

            #
            countriesFromField.append(country.name)
            
        #
        elif field == "alpha_2":

            #
            countriesFromField.append(country.alpha_2)

        #
        elif field == "alpha_3":

            #
            countriesFromField.append(country.alpha_3)

        #
        elif field == "numeric":

            #
            countriesFromField.append(country.numeric)

        #
        else:

            #
            raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    if order == "desc":

        #
        countriesFromField.sort(reverse=True)

    #
    else:

        #
        countriesFromField.sort()

    #
    for fieldValueForCurrentCountry in countriesFromField:

        #
        if field == "name":

            #
            sortedCountriesList.append(pycountry.countries.get(name=fieldValueForCurrentCountry))

        #
        elif field == "alpha_2":

            #
            sortedCountriesList.append(pycountry.countries.get(alpha_2=fieldValueForCurrentCountry))

        #
        elif field == "alpha_3":

            #
            sortedCountriesList.append(pycountry.countries.get(alpha_3=fieldValueForCurrentCountry))

        #
        elif field == "numeric":

            #
            sortedCountriesList.append(pycountry.countries.get(numeric=fieldValueForCurrentCountry))

        #
        else:

            #
            raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    return sortedCountriesList

#
def getJSONofHistoricalCountriesFromSort(field='name', order = "asc", pattern=None):

    #
    allHistoricalCountriesFromSort = getAllHistoricalCountriesFromSort(field, order, pattern)

    #
    historicalCountriesDict = {}

    #
    for country in allHistoricalCountriesFromSort:

        #
        if field == 'name':

            #
            historicalCountriesDict[country.name] = {
                                                        "name": country.name,
                                                        "alpha_2": country.alpha_2,
                                                        "alpha_3": country.alpha_3,
                                                        "withdrawal_date": country.withdrawal_date
                                                    }

            #
            if "numeric" in json.dumps(country.__dict__):

                #
                historicalCountriesDict[country.name]["numeric"] = country.numeric

        #
        elif field == 'alpha_2':

            #
            historicalCountriesDict[country.alpha_2] = {
                                                            "name": country.name,
                                                            "alpha_2": country.alpha_2,
                                                            "alpha_3": country.alpha_3,
                                                            "withdrawal_date": country.withdrawal_date
                                                        }

            #
            if "numeric" in json.dumps(country.__dict__):

                #
                historicalCountriesDict[country.alpha_2]["numeric"] = country.numeric

        #
        elif field == 'alpha_3':

            #
            historicalCountriesDict[country.alpha_3] = {
                                                            "name": country.name,
                                                            "alpha_2": country.alpha_2,
                                                            "alpha_3": country.alpha_3,
                                                            "withdrawal_date": country.withdrawal_date
                                                        }

            #
            if "numeric" in json.dumps(country.__dict__):

                #
                historicalCountriesDict[country.alpha_3]["numeric"] = country.numeric

        #
        elif field == 'numeric':

            #
            historicalCountriesDict[country.numeric] = {
                                                            "name": country.name,
                                                            "alpha_2": country.alpha_2,
                                                            "alpha_3": country.alpha_3,
                                                            "withdrawal_date": country.withdrawal_date
                                                        }

            #
            if "numeric" in json.dumps(country.__dict__):

                #
                historicalCountriesDict[country.numeric]["numeric"] = country.numeric

        else:

            #
            raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    return historicalCountriesDict

#
def getJSONofCountriesFromSort(field='name', order = "asc", pattern=None):

    #
    allCountriesFromSort = getAllCountriesFromSort(field, order, pattern)

    #
    countriesDict = {}

    #
    for country in allCountriesFromSort:

            #
            if field == 'name':

                #
                countriesDict[country.name] = {
                                                "name": country.name,
                                                "alpha_2": country.alpha_2,
                                                "alpha_3": country.alpha_3,
                                                "numeric": country.numeric,
                                                "flag": country.flag
                                            }

                #
                try:
                    countriesDict[country.name]["official_name"] = country.official_name

                #
                except AttributeError:
                    countriesDict[country.name]["official_name"] = None

            #
            elif field == 'alpha_2':

                #
                countriesDict[country.alpha_2] = {
                                                "name": country.name,
                                                "alpha_2": country.alpha_2,
                                                "alpha_3": country.alpha_3,
                                                "numeric": country.numeric,
                                                "flag": country.flag
                                            }

                #
                try:
                    countriesDict[country.alpha_2]["official_name"] = country.official_name

                #
                except AttributeError:
                    countriesDict[country.alpha_2]["official_name"] = None

            #
            elif field == 'alpha_3':

                #
                countriesDict[country.alpha_3] = {
                                                "name": country.name,
                                                "alpha_2": country.alpha_2,
                                                "alpha_3": country.alpha_3,
                                                "numeric": country.numeric,
                                                "flag": country.flag
                                            }

                #
                try:
                    countriesDict[country.alpha_3]["official_name"] = country.official_name

                #
                except AttributeError:
                    countriesDict[country.alpha_3]["official_name"] = None

            #
            elif field == 'numeric':

                #
                countriesDict[country.numeric] = {
                                                "name": country.name,
                                                "alpha_2": country.alpha_2,
                                                "alpha_3": country.alpha_3,
                                                "numeric": country.numeric,
                                                "flag": country.flag
                                            }

                #
                try:
                    countriesDict[country.numeric]["official_name"] = country.official_name

                #
                except AttributeError:
                    countriesDict[country.numeric]["official_name"] = None

            else:

                #
                raise Exception('NotExistingFieldError', 'The wished field does not exist...')

    #
    return countriesDict

#
def getJSONOfHistoricalCountries(historicalCountriesList):

    #
    histCountryDict = {}

    #
    for country in historicalCountriesList:

        #
        currentCountry = {
                            "name": country.name,
                            "alpha_2": country.alpha_2,
                            "alpha_3": country.alpha_3,
                            "withdrawal_date": country.withdrawal_date
                        }
        
        #
        try:
            currentCountry["numeric"] = country.numeric

        #
        except AttributeError:
            currentCountry["numeric"] = None

        #
        finally:
            histCountryDict[country.name] = currentCountry

    #
    return histCountryDict

#
def getJSONOfCountries(countriesList, order="asc"):

    #
    countriesDict = {}

    #
    for country in countriesList:

        #
        currentCountry = {
                            "name": country.name,
                            "alpha_2": country.alpha_2,
                            "alpha_3": country.alpha_3,
                            "numeric": country.numeric,
                            "flag": country.flag
                        }

        #
        try:
            currentCountry["official_name"] = country.official_name

        #
        except AttributeError:
            currentCountry["official_name"] = None

        #
        finally:
            countriesDict[country.name] = currentCountry

    #
    return countriesDict

#
def getDateTimeInParticularCalendar(wishedCalendarSystem, wishedDateTime = datetime.now()):

    #
    if wishedCalendarSystem == "armenian":

        dateInArmenianCalendar = convertdate.armenian.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.armenian.format(dateInArmenianCalendar[0], dateInArmenianCalendar[1], dateInArmenianCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "bahai":

        dateInBahaiCalendar = convertdate.bahai.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.bahai.format(dateInBahaiCalendar[0], dateInBahaiCalendar[1], dateInBahaiCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "coptic":

        dateInCopticCalendar = convertdate.coptic.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.coptic.format(dateInCopticCalendar[0], dateInCopticCalendar[1], dateInCopticCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "daycount":

        dayCount = convertdate.daycount.DayCount()

        return {"calendar": wishedCalendarSystem, "date_and_time": str(dayCount)}, 200

    #
    elif wishedCalendarSystem == "dublin":

        dateDublinCalendar = convertdate.dublin.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(dateDublinCalendar)}, 200

    #
    elif wishedCalendarSystem == "french_republican":

        dateInFrenchRepublicanCalendar = convertdate.french_republican.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.french_republican.format(dateInFrenchRepublicanCalendar[0], dateInFrenchRepublicanCalendar[1], dateInFrenchRepublicanCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "gregorian":
        
        return {"calendar": wishedCalendarSystem, "date_and_time": convertdate.gregorian.format(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)}, 200

    #
    elif wishedCalendarSystem == "hebrew":

        dateInHebrewCalendar = convertdate.hebrew.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.hebrew.format(dateInHebrewCalendar[0], dateInHebrewCalendar[1], dateInHebrewCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "indian_civil":

        dateInIndicanCivil = convertdate.indian_civil.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.indian_civil.format(dateInIndicanCivil[0], dateInIndicanCivil[1], dateInIndicanCivil[2]))}, 200

    #
    elif wishedCalendarSystem == "islamic":

        dateInIslamicCalendar = convertdate.islamic.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.islamic.format(dateInIslamicCalendar[0], dateInIslamicCalendar[1], dateInIslamicCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "iso":

        dateInISOCalendar = convertdate.iso.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.iso.format(dateInISOCalendar[0], dateInISOCalendar[1], dateInISOCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "julian":

        dateInJulianCalendar = convertdate.julian.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.julian.format(dateInJulianCalendar[0], dateInJulianCalendar[1], dateInJulianCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "julianday":

        dateInJulianDayCalendar = convertdate.julianday.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(dateInJulianDayCalendar)}, 200

    #
    elif wishedCalendarSystem == "mayan":

        dateInMayanCalendar = convertdate.mayan.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        dateInMayanCalendarHaab = convertdate.mayan.lc_to_haab(dateInMayanCalendar[0], dateInMayanCalendar[1], dateInMayanCalendar[2], dateInMayanCalendar[3], dateInMayanCalendar[4])
        dateInMayanCalendarTzolkin = convertdate.mayan.lc_to_tzolkin(dateInMayanCalendar[0], dateInMayanCalendar[1], dateInMayanCalendar[2], dateInMayanCalendar[3], dateInMayanCalendar[4])

        return {"calendar": wishedCalendarSystem, "date_and_time": {
            "haab": str(dateInMayanCalendarHaab[0]) + " " + dateInMayanCalendarHaab[1],
            "tzolkin": str(dateInMayanCalendarTzolkin[0]) + " " + dateInMayanCalendarTzolkin[1],
            "haab_and_tzolkin": str(convertdate.mayan.lc_to_haab_tzolkin(dateInMayanCalendar[0], dateInMayanCalendar[1], dateInMayanCalendar[2], dateInMayanCalendar[3], dateInMayanCalendar[4]))
        }}, 200

    #
    elif wishedCalendarSystem == "ordinal":

        dateInOrdinalCalendar = convertdate.ordinal.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(dateInOrdinalCalendar[0]) + " - " + str(dateInOrdinalCalendar[1])}, 200

    #
    elif wishedCalendarSystem == "persian":

        dateInPersianCalendar = convertdate.persian.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        return {"calendar": wishedCalendarSystem, "date_and_time": str(convertdate.persian.format(dateInPersianCalendar[0], dateInPersianCalendar[1], dateInPersianCalendar[2]))}, 200

    #
    elif wishedCalendarSystem == "positivist":

        dateInPositivistCalendar = convertdate.positivist.from_gregorian(wishedDateTime.year, wishedDateTime.month, wishedDateTime.day)

        currentDname = convertdate.positivist.dayname(dateInPositivistCalendar[0], dateInPositivistCalendar[1], dateInPositivistCalendar[2])

        return {"calendar": wishedCalendarSystem, "date_and_time": str(dateInPositivistCalendar[0]) + " " + currentDname[0] + " " + currentDname[1]}, 200

    return {"calendar": wishedCalendarSystem, "date_and_time": "calendar system not available"}, 503

#
def getAllCalendars(all_infos=False):

    """
    Return all available calendars in an array...
    """
    
    pkgpath = os.path.dirname(convertdate.__file__)

    allCalendars = [calendar for _, calendar, _ in pkgutil.iter_modules([pkgpath])]

    _allCalendars = []

    for calendar in allCalendars:

        if calendar not in {"data", "holidays", "utils"}:

            _allCalendars.append(calendar)

    allCalendars = _allCalendars

    return allCalendars

#
def getAllTimezones():

    """
    Return all available timezones in an array...
    """

    #
    all_timezones = []

    #
    for current_timezone in common_timezones:

        #
        all_timezones.append(current_timezone)

    #
    return all_timezones

#
def getAllTimezonesByCountry(wished_country, all_infos):

    """
    Return all available timezones in an array for a specified country...
    """

    #
    timezones_array = country_timezones(pycountry.countries.get(name=wished_country).alpha_2)

    #
    if all_infos:

        timezones_dict = {}

        for tz in timezones_array:
            current_tz = {}

            #
            now_utc = datetime.now(timezone('UTC'))
            now_from_timezone = now_utc.astimezone(timezone(tz))

            current_tz["UTC offset"] = now_from_timezone.astimezone(timezone(tz)).strftime("%z")
            current_tz["date_and_time"] = now_from_timezone.strftime("%Y-%m-%d %H:%M:%S")

            timezones_dict[tz] = current_tz

        #
        return timezones_dict
    #
    else:
        return timezones_array

#
def getAllCountries():

    """
    Return all existing countries in an array...
    """

    #
    allCountries = []

    #
    allCountriesFromCountries = pycountry.countries

    #
    for countryFromCountries in allCountriesFromCountries:

        #
        allCountries.append(countryFromCountries.name)

    #
    return allCountries

#
def getCountry(timezone, country_flag_cdn = False):

    """
    Return the countries with all datas...
    """

    #
    timezones_list = country_timezones

    #
    timezone_index = -1

    #
    keys_from_timezones_list = list(timezones_list.keys())
    values_from_timezones_list = list(timezones_list.values())

    #
    for current_timezone_array in values_from_timezones_list:

        #
        if timezone in current_timezone_array:

            #
            timezone_index = values_from_timezones_list.index(current_timezone_array)

    #
    countryCode = keys_from_timezones_list[timezone_index]

    #
    countryName = pycountry.countries.get(alpha_2=countryCode).name
    countryFlag = pycountry.countries.get(alpha_2=countryCode).flag

    #
    try:
        countryOfficialName = pycountry.countries.get(alpha_2=countryCode).official_name

    #
    except AttributeError:

        #
        countryOfficialName = pycountry.countries.get(alpha_2=countryCode).name

    #
    finally:

        #
        if country_flag_cdn == True:

            #
            return {
                    "country_name": countryName,
                    "country_offical_name": countryOfficialName,
                    "country_code": countryCode,
                    "country_flag": {
                        "country_flag_unicode": countryFlag,
                        "country_flag_cdn": {
                                "16_x_12": "https://flagcdn.com/16x12/" + countryCode.lower() + ".png",
                                "20_x_15": "https://flagcdn.com/20x15/" + countryCode.lower() + ".png",
                                "24_x_18": "https://flagcdn.com/24x18/" + countryCode.lower() + ".png",
                                "28_x_21": "https://flagcdn.com/28x21/" + countryCode.lower() + ".png",
                                "32_x_24": "https://flagcdn.com/32x24/" + countryCode.lower() + ".png",
                                "36_x_27": "https://flagcdn.com/36x27/" + countryCode.lower() + ".png",
                                "40_x_30": "https://flagcdn.com/40x30/" + countryCode.lower() + ".png",
                                "48_x_36": "https://flagcdn.com/48x36/" + countryCode.lower() + ".png",
                                "56_x_42": "https://flagcdn.com/56x42/" + countryCode.lower() + ".png",
                                "60_x_45": "https://flagcdn.com/60x45/" + countryCode.lower() + ".png",
                                "64_x_48": "https://flagcdn.com/64x48/" + countryCode.lower() + ".png",
                                "72_x_54": "https://flagcdn.com/72x54/" + countryCode.lower() + ".png",
                                "80_x_60": "https://flagcdn.com/80x60/" + countryCode.lower() + ".png",
                                "84_x_63": "https://flagcdn.com/84x63/" + countryCode.lower() + ".png",
                                "96_x_72": "https://flagcdn.com/96x72/" + countryCode.lower() + ".png",
                                "108_x_81": "https://flagcdn.com/108x81/" + countryCode.lower() + ".png",
                                "112_x_84": "https://flagcdn.com/112x84/" + countryCode.lower() + ".png",
                                "120_x_90": "https://flagcdn.com/120x90/" + countryCode.lower() + ".png",
                                "128_x_96": "https://flagcdn.com/128x96/" + countryCode.lower() + ".png",
                                "144_x_108": "https://flagcdn.com/144x108/" + countryCode.lower() + ".png",
                                "160_x_120": "https://flagcdn.com/160x120/" + countryCode.lower() + ".png",
                                "192_x_144": "https://flagcdn.com/192x144/" + countryCode.lower() + ".png",
                                "224_x_168": "https://flagcdn.com/224x168/" + countryCode.lower() + ".png",
                                "256_x_192": "https://flagcdn.com/256x192/" + countryCode.lower() + ".png"
                                }
                        }
                    }
        
        #
        else:

            #
            return {
                    "country_name": countryName,
                    "country_offical_name": countryOfficialName,
                    "country_code": countryCode,
                    "country_flag": {
                        "country_flag_unicode": countryFlag
                    }
                }

#
parser_current_date_and_time_by_timezone_template = reqparse.RequestParser()
parser_current_date_and_time_by_timezone_template.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')
parser_current_date_and_time_by_timezone_template.add_argument('datetime_format', type=str, required=False, help='Available format code: \
                                                                                                           %a (abreviated weekday name), \
                                                                                                           %A (full weekday name), \
                                                                                                           %w (weekday as a decimal number), \
                                                                                                           %d (day of the month as a zero-padded decimal), \
                                                                                                           %-d (day of the month as a decimal number), \
                                                                                                           %b (abbreviated month name), %B (full month name), \
                                                                                                           %B (Full month name), \
                                                                                                           %m (Month as a zero-padded decimal number), \
                                                                                                           %-m (Month as a decimal number), \
                                                                                                           %y (Year without century as a zero-padded decimal number), \
                                                                                                           %-y (Year without century as a decimal number), \
                                                                                                           %Y (Year with century as a decimal number), \
                                                                                                           %z (UTC offset in the form +HHMM or -HHMM), \
                                                                                                           %Z (Time zone name), \
                                                                                                           %c (Locale’s appropriate date and time representation), \
                                                                                                           %x (locale’s appropriate date representation), \
                                                                                                           %X (locale’s appropriate time representation), \
                                                                                                           %% (a literal \'%\' character) \
                                                                                                           ...')