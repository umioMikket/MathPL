import math
from api.console import *

class module:
    def pi(): return math.pi
    def e(): return math.e
    def cos(n): return math.cos(n)
    def sin(n): return math.sin(n)
    def tan(n): return math.tan(n)
    def acos(n): return math.acos(n)
    def asin(n): return math.asin(n)
    def atan(n): return math.atan(n)
    def log(n, b): return math.log(n, b)

class area:
    def square(length): return length ** 2
    def rectangle(width, height): return width * height
    def triangle(base, height): return (base * height) / 2
    def rhombus(largeDiagonal, smallDiagonal): return (largeDiagonal * smallDiagonal) / 2
    def trapezoid(largeSide, smallSide, height): return ((largeSide * smallSide) / 2) * height
    def regularPolygon(perimeter, apothem): return (perimeter / 2) * apothem
    def circle(radius): return math.pi * radius ** 2
    def cone(radius, slantHeight): return (math.pi * radius) * slantHeight
    def sphere(radius): return 4*(math.pi*(radius**2))
