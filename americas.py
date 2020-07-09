import pygal
from world_population import get_population_by_country_code as gpcc

wm = pygal.maps.world.World()
wm.title = "North, Central and South America"
wm.add('North America', {'ca': gpcc('ca'), 'mx': gpcc('mx'), 'us': gpcc('us')})
wm.add('Central America', {'bz': gpcc('bz'), 'cr': gpcc('cr'), 'gt': gpcc('gt'), 'hn': gpcc('hn'), 'ni': gpcc('ni'),
                           'pa': gpcc('pa'), 'sv': gpcc('sv')})
wm.add('South America', {'ar': gpcc('ar'), 'bo': gpcc('bo'), 'br': gpcc('br'), 'cl': gpcc('cl'), 'co': gpcc('co'),
                         'ec': gpcc('ec'), 'gf': gpcc('gf'), 'gy': gpcc('gy'), 'pe': gpcc('pe'), 'py': gpcc('py'),
                         'sr': gpcc('sr'), 'uy': gpcc('uy'), 've': gpcc('ve')})

wm.render_to_file('americas.svg')
