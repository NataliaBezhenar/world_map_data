import csv
import pygal
from pycountry_convert import country_alpha2_to_continent_code
from country_codes import get_country_code

filename = "electricity_access.csv"
all_countries = {}
input_year = '2005'


def get_continent(country_code):
    """ Returns 2-digit continent code by 2-digit country code """
    try:
        cn_continent = country_alpha2_to_continent_code(country_code)
    except:
        cn_continent = 'Unknown'
    return cn_continent


def get_electrification_by_year(year):
    """ Returns data on the access to electricity for the certain year """
    try:
        if row[year] != '':
            return float(row[year])
        else:
            return None
    except KeyError:
        return None


europe, asia, north_america, south_america, africa, oceania, unsorted = {}, {}, {}, {}, {}, {}, {}

with open(filename, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        all_countries[get_country_code(row['Country Name'])] = get_electrification_by_year(input_year)

    for key, value in all_countries.items():
        if get_continent(str(key).upper()) == 'EU':
            europe[key] = value
        elif get_continent(str(key).upper()) == 'AS':
            asia[key] = value
        elif get_continent(str(key).upper()) == 'NA':
            north_america[key] = value
        elif get_continent(str(key).upper()) == 'SA':
            south_america[key] = value
        elif get_continent(str(key).upper()) == 'OC':
            oceania[key] = value
        elif get_continent(str(key).upper()) == 'AF':
            africa[key] = value
        else:
            unsorted[key] = value

wm = pygal.maps.world.World()
wm.title = "Access to electricity (% of population), year " + input_year
wm.add('Africa', africa)
wm.add('Europe', europe)
wm.add('North America', north_america)
wm.add('South America', south_america)
wm.add('Asia', asia)
wm.add('Oceania', oceania)

wm.render_to_file('electricity_percent.svg')
