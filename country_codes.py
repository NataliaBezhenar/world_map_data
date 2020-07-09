import pygal

countries = pygal.maps.world.COUNTRIES


def get_country_code(country_name):
    """ Returns 2-digit country code for each country """
    for code, name in countries.items():
        if name == country_name:
            return code
    return None
