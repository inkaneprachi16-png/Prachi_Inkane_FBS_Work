class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    # Overload +operator
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm
        return(f"Addition of distances: {km} km {m} m {cm} cm")

    # Overload - operator
    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm
        return(f"Subtraction of distances: {km} km {m} m {cm} cm")

d1 = Distance(5, 500, 50)   
d2 = Distance(4, 200, 20)   

print(d1 + d2)   
print(d1 - d2) 