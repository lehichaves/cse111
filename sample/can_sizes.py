import math

def main ():

    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#1 Picnic - {storage_efficiency:.2f}")   

    name = "#Tall"
    radius = 7.78
    height = 11.91
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#Tall - {storage_efficiency:.2f}")   

    name = "#2"
    radius = 8.73
    height = 11.59
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#2 - {storage_efficiency:.2f}")   

    name = "#2.5"
    radius = 10.32
    height = 11.91
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#2.5 - {storage_efficiency:.2f}")   

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#3 Cylinder - {storage_efficiency:.2f}")   

    name = "#5"
    radius = 13.02
    height = 14.29
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#5 - {storage_efficiency:.2f}")   

    name = "#6Z"
    radius = 5.40
    height = 8.89
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#6Z - {storage_efficiency:.2f}")   

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#8Z short - {storage_efficiency:.2f}")   

    name = "#10"
    radius = 15.72
    height = 17.78
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#10 - {storage_efficiency:.2f}")   

    name = "#211"
    radius = 6.83
    height = 12.38
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#211 - {storage_efficiency:.2f}")   

    name = "#300"
    radius = 7.62
    height = 11.27
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)
    storage_efficiency = volume / surface_area
    
    print(f"#300 - {storage_efficiency:.2f}")   

    name = "#303"
    radius = 8.10
    height = 11.11
    
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)

    storage_efficiency = volume / surface_area
    
    print(f"#303 - {storage_efficiency:.2f}")   


def compute_volume(radius, height):
    
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):

    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main ()




