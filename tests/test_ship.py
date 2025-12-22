import pytest
from battleship25.ship import Ship

def test_ship_has_name_and_length_and_health():
    ship = Ship("Cruiser", 3)
    assert ship.name == "Cruiser"
    assert ship.length == 3
    assert ship.health == 3

def test_hit_reduces_health_by_1():
    ship = Ship("Submarine", 2)
    ship.hit()
    assert ship.health == 1

def test_sunk_is_false_when_health_above_0():
    ship = Ship("Submarine", 2)
    ship.hit()
    assert ship.sunk() is False

def test_sunk_is_true_when_health_is_0():
    ship = Ship("Submarine", 2)
    ship.hit()
    ship.hit()
    assert ship.sunk() is True