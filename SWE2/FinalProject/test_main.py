import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import math
from main import *

TELORANCE = 0.001



circle_area_scenarios = [
    #pass
    (5, math.pi * (5 ** 2)),
    #fail
    (5, math.pi * (5 ** 3))
]

@pytest.mark.parametrize("radius, expected", circle_area_scenarios)
def test_circle_area(radius, expected):
    actual = circle(radius).area()
    assert actual == pytest.approx(expected, abs=TELORANCE)



circle_perimeter_scenarios = [
    #pass
    (5, 2 * math.pi * 5),
    #fail
    (5, 2 * math.pi * 2)
]

@pytest.mark.parametrize("radius, expected", circle_perimeter_scenarios)
def test_circle_perimeter(radius, expected):
    actual = circle(radius).perimeter()
    assert actual == pytest.approx(expected, abs=TELORANCE)



rectangle_area_scenarios = [
    # pass
    (5, 6, 30),
    # fail
    (5, 6, 35)
]

@pytest.mark.parametrize("width, length, expected", rectangle_area_scenarios)
def test_rectangle_area(width, length, expected):
    actual = rectangle(width, length).area()
    assert actual == expected



rectangle_perimeter_scenarios = [
    # pass
    (5, 6, 22),
    # fail
    (5, 6, 20)
]

@pytest.mark.parametrize("width, length, expected", rectangle_perimeter_scenarios)
def test_rectangle_perimeter(width, length, expected):
    actual = rectangle(width,length).perimeter()
    assert actual == expected



square_area_scenarios = [
    # pass
    (5, 25),
    # fail
    (5, 20)
]

@pytest.mark.parametrize("length, expected", square_area_scenarios)
def test_square_area(length, expected):
    actual = square(length).area()
    assert actual == expected



square_perimeter_scenarios = [
    # pass
    (5, 20),
    # fail
    (5, 15)
]

@pytest.mark.parametrize("length, expected", square_perimeter_scenarios)
def test_square_perimeter(length, expected):
    actual = square(length).perimeter()
    assert actual == expected



cube_volume_scenarios = [
    # pass
    (5, 125),
    # fail
    (5, 100)
]

@pytest.mark.parametrize("length, expected", cube_volume_scenarios)
def test_cube_volume(length, expected):
    actual = cube(length).volume()
    assert actual == expected



ball_volume_scenarios = [
    # pass
    (5, (4/3)*math.pi*(5**3)),
    # fail
    (5, (4/3)*math.pi*(5**2))
]

@pytest.mark.parametrize("radius, expected", ball_volume_scenarios)
def test_ball_volume(radius, expected):
    actual = ball(radius).volume()
    assert actual == pytest.approx(expected, abs=TELORANCE)





