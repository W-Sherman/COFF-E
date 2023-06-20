'''
COFF-E - Cislunar Optimization of Formation Flight Experiment
by Will Sherrman - 2023

link: https://github.com/W-Sherman/COFF-E/tree/main


Planetary Data Library
'''
sun =   {
        'name'            : 'Sun',
        'SPICE_ID'        : 10,
        'mass'            : 1.989e30,
        'mu'              : 1.3271244004193938E+11,
        'radius'          : 695510.0,
        'deorbit_altitude': 1.2 * 695510.0,
        'cmap'            :'gist_heat'
        }

earth = {
		'name'            : 'Earth',
		'spice_name'      : 'EARTH',
		'SPICE_ID'        : 399,
		'mass'            : 5.972e24,
		'mu'              : 5.972e24 * G,
		'radius'          : 6378.0,
		'J2'              : 1.081874e-3,
		'sma'             : 149.596e6, # km
		'SOI'             : 926006.6608, # km
		'deorbit_altitude': 100.0, # km
		'cmap'            : 'Blues',
		'body_fixed_frame': 'IAU_EARTH',
		'traj_color'      : 'b'
		}

moon = {
		'name'            : 'Moon',
		'spice_name'      : 'MOON',
		'SPICE_ID'        : 301,
		'mass'            : 5.972e24,
		'mu'              : 5.972e24 * G,
		'radius'          : 1737.4,
		'J2'              : 1.081874e-3,
		'sma'             : 149.596e6, # km
		'SOI'             : 926006.6608, # km
		'deorbit_altitude': 100.0, # km
		'cmap'            : 'Blues',
		'body_fixed_frame': 'IAU_EARTH',
		'traj_color'      : 'b'
		}


bodies = [
	earth, moon, sun ]

for body in bodies:
	body[ 'diameter' ] = body[ 'radius' ] * 2