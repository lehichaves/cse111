#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 7
#W07 Project

from maintenance_control import PM_orders_closed, AM_orders_opened, PM_orders_opened
import pytest

def test_PM_orders_closed():
    preventive = "project/preventive.csv"
    result = PM_orders_closed(preventive)
    assert result >= 1

def test_PM_orders_opened():
    preventive = "project/preventive.csv"
    result = PM_orders_opened(preventive)
    assert result >= 1   

def test_AM_orders_opened():
    corrective = "project/corrective.csv"
    result = AM_orders_opened(corrective)
    assert result >= 1



pytest.main(["-v", "--tb=line", "-rN", __file__])

