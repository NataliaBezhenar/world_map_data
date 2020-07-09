import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'data_json.json'
with open(filename) as f:
    pop_data = json.load(f)

updated_codes_population_dict = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            updated_codes_population_dict[code] = population

""" Group countries by 3 levels of population """
upd_pops_1, upd_pops_2, upd_pops_3 = {}, {}, {}
for code, population in updated_codes_population_dict.items():
    if population < 10000000:
        upd_pops_1[code] = population
    elif population < 1000000000:
        upd_pops_2[code] = population
    else:
        upd_pops_3[code] = population

wm_style = RotateStyle('#339944', base_style=LightColorizedStyle)

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2016, by Country'
wm.add('0-10m', upd_pops_1)
wm.add('10m - 1bl', upd_pops_2)
wm.add('>1bl', upd_pops_3)
wm.render_to_file('world_population.svg')


def get_population_by_country_code(country_code):
    try:
        return updated_codes_population_dict[country_code]
    except KeyError:
        return 1
