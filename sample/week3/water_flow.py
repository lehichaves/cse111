#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 3
#Activity - Prove Prove Milestone: Testing and Fixing Functions

def water_column_height(tower_height, tank_height):
    h_column_height = tower_height + (3 * tank_height / 4)
    return h_column_height

def pressure_gain_from_water_height(height):
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_lenght, friction_factor, fluid_velocity):
    pressure_lost = ( - friction_factor * pipe_lenght * 998.2 * (fluid_velocity**2) ) / (2000 * pipe_diameter)
    return pressure_lost