class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_in_seconds = 31557600.0
        
        self.orbital_periods = {
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "earth": 1.0,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132
        }

    def on_mercury(self):
        return self._calculate_age("mercury")
    def on_venus(self):
        return self._calculate_age("venus")
    def on_earth(self):
        return self._calculate_age("earth")
    def on_mars(self):
        return self._calculate_age("mars")
    def on_jupiter(self):
        return self._calculate_age("jupiter")
    def on_saturn(self):
        return self._calculate_age("saturn")
    def on_uranus(self):
        return self._calculate_age("uranus")
    def on_neptune(self):
        return self._calculate_age("neptune")

    def _calculate_age(self, planet):
        return round(self.seconds / self.earth_year_in_seconds / 
                     self.orbital_periods[planet],2)
