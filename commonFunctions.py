#
from datetime import datetime
from itertools import count
from pytz import common_timezones, country_timezones
from pycountry import countries

#
def getAllTimezones():

    #
    all_timezones = []

    #
    for current_timezone in common_timezones:

        #
        all_timezones.append(current_timezone)

    #
    return all_timezones

#
def getCountry(timezone):

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
    countryName = countries.get(alpha_2=countryCode).name,

    #
    return {
                "country_name": countryName[0],
                "country_code": countryCode,
                "country_flag": {
                    "16_x_12": "https://flagcdn.com/16x12/" + countryCode + ".png",
                    "20_x_15": "https://flagcdn.com/20x15/" + countryCode + ".png",
                    "24_x_18": "https://flagcdn.com/24x18/" + countryCode + ".png",
                    "28_x_21": "https://flagcdn.com/28x21/" + countryCode + ".png",
                    "32_x_24": "https://flagcdn.com/32x24/" + countryCode + ".png",
                    "36_x_27": "https://flagcdn.com/36x27/" + countryCode + ".png",
                    "40_x_30": "https://flagcdn.com/40x30/" + countryCode + ".png",
                    "48_x_36": "https://flagcdn.com/48x36/" + countryCode + ".png",
                    "56_x_42": "https://flagcdn.com/56x42/" + countryCode + ".png",

                    "120_x_90": "https://flagcdn.com/120x90/" + countryCode + ".png",
                    "128_x_96": "https://flagcdn.com/128x96/" + countryCode + ".png",
                    "144_x_108": "https://flagcdn.com/144x108/" + countryCode + ".png",
                    "160_x_120": "https://flagcdn.com/160x120/" + countryCode + ".png",
                    "192_x_144": "https://flagcdn.com/192x144/" + countryCode + ".png",
                    "224_x_168": "https://flagcdn.com/224x168/" + countryCode + ".png",
                    "256_x_192": "https://flagcdn.com/256x192/" + countryCode + ".png"
                }
           }
