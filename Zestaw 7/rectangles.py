from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):   
        return f"[{self.pt1}, {self.pt2}]"       
    
    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):         
        return f"Rectangle{self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y}" 
    
    # obsługa rect1 == rect2 -> zwraca wartość bool
    def __eq__(self, other):    
        return bool(self.pt1 == other.pt1 and self.pt2 == other.pt2)
    
    # obsługa rect1 != rect2 -> zwraca wartość bool
    def __ne__(self, other):        
        return not self == other

    def center(self):         # zwraca środek prostokąta
        x = (self.pt2.x - self.pt1.x) / 2
        y = (self.pt2.y - self.pt1.y) / 2
        return Point(x, y)
    
    # pole powierzchni
    def area(self):            
        # Uzywamy funkcji abs poniewaz pole prostokata nie moze byc ujemne
        pole = (abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y))
        return pole

    def move(self, x, y):    # przesunięcie o (x, y)
        przesuniecie = Point(x,y)
        self.pt1 = self.pt1 + przesuniecie
        self.pt2 = self.pt2 + przesuniecie
        return f"[{self.pt1}, {self.pt2}]"

    # część wspólna prostokątów
    def intersection(self, other):  
        if(self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y or self.pt1.x > other.pt2.x or self.pt2.x < other.pt1.x ):
            raise ValueError("Brak częsci wspólnej")
        else:
            przeciecie = Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        return przeciecie

    # prostąkąt nakrywający oba
    def cover(self, other):
        nakrywanie = Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        return nakrywanie

    # zwraca krotkę czterech mniejszych
    def make4(self):          
        krotka = (Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y),
                  Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y),
                  Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y),
                  Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y))

        return krotka