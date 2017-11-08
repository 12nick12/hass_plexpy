# hass_plexpy
PlexPy Integratin for HASS

I didn't find any solution that woudl give me a play count from Plex in HASS. For some reason I could never get the Plex Activity Monitor to work so I decided to try and create my own. 

As of now I prety much just made python scripts that do the couple things I want. To use in hass just:

- platform: command_line
  name: name
  command: 'python3 /path/to/python/file.py'
  unit_of_measurement: 'choice of measurement, not needed'
