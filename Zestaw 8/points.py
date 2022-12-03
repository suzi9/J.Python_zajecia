class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y
    
    # zwraca string "(x, y)"
    def __str__(self):  
        return f"({self.x}, {self.y})"

    # zwraca string "Point(x, y)"
    def __repr__(self):        
        return f"Point({self.x}, {self.y})"
        
    # obsługa point1 == point2 -> zwraca wartość bool
    def __eq__(self, other):    
        return bool(self.x == other.x and self.y == other.y)

    # obsługa point1 != point2 -> zwraca wartość bool
    def __ne__(self, other):        
        return not self == other

    # Punkty jako wektory 2D  ----------------------------------------------
    
    # v1 + v2
    def __add__(self, other):   
        r = self.x + other.x
        w = self.y + other.y
        # zwracamy nowy obiekt którym jest punkt
        return Point(r, w)

    # v1 - v2
    def __sub__(self, other):   
        r = self.x - other.x
        w = self.y - other.y
        # zwracamy nowy obiekt którym jest punkt
        return Point(r, w)

    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):   
       r = self.x * other.x
       w = self.y * other.y
       return r + w

    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):         
        return self.x * other.y - self.y * other.x
    
    # długość wektora
    def length(self):          
        dlugosc = ((self.x)**2 + (self.y)**2)**(1/2)
        return dlugosc

    # bazujemy na tuple, immutable points
    def __hash__(self):
        return hash((self.x, self.y))   