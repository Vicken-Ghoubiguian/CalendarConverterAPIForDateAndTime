#
from datetime import datetime
from itertools import count
from pytz import common_timezones, country_timezones
from pycountry import countries

#
def getAllTimezones():

    """
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
def getCountry(timezone):

    """
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
    countryName = countries.get(alpha_2=countryCode).name
    countryFlag = countries.get(alpha_2=countryCode).flag

    #
    try:
        countryOfficialName = countries.get(alpha_2=countryCode).official_name

    #
    except AttributeError:

        #
        countryOfficialName = countries.get(alpha_2=countryCode).name

    #
    finally:

        #
        if 1 == 0:

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
