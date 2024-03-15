#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 3
#Activity - Prove Prove Milestone: Testing and Fixing Functions

import pytest

from pytest import approx 
from water_flow import water_column_height, pressure_loss_from_pipe, pressure_gain_from_water_height


def test_water_column_height():

    assert water_column_height (0.0, 0.0) == 0.0
    assert water_column_height (0.0, 10.0) == 7.5
    assert water_column_height (25.0, 0.0) == 25.0
    assert water_column_height (48.3, 12.8) == 57.9
    
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height (0.0) == approx (0.000, rel=0.001)
    assert pressure_gain_from_water_height (30.2) == approx (295.628, rel=0.001)
    assert pressure_gain_from_water_height (50.0) == approx (489.450, rel=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe (0.048692, 0.00, 0.018, 1.75) == approx (0.000, rel=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.000, 1.75) == approx (0.000, rel=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 0.00) == approx (0.000, rel=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 1.75) == approx (-113.008, rel=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 1.65) == approx (-100.462, rel=0.001)
    assert pressure_loss_from_pipe (0.286870, 1000.00, 0.013, 1.65) == approx (-61.576, rel=0.001)
    assert pressure_loss_from_pipe (0.286870, 1800.75, 0.013, 1.65) == approx (-110.884, rel=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])