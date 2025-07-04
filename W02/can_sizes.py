import math



def main():
    can_sizes = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]

    best_storage = {'name': '', 'efficiency': 0}
    best_cost = {'name': '', 'efficiency': 0}

    print(f"{'Can':<15}{'Storage Eff.':>15}{'Cost Eff.':>15}")
    for can in can_sizes:
        radius = can["radius"]
        height = can["height"]
        cost = can["cost"]
        name = can["name"]
        volume = can_volume(radius, height)
        storage_eff = compute_storage_efficiency(radius, height)
        cost_eff = compute_cost_efficiency(volume, cost)
        print(f"{name:<15}{storage_eff:>15.4f}{cost_eff:>15.4f}")
        if storage_eff > best_storage['efficiency']:
            best_storage = {'name': name, 'efficiency': storage_eff}
        if cost_eff > best_cost['efficiency']:
            best_cost = {'name': name, 'efficiency': cost_eff}
    print(f"\nBest storage efficiency: {best_storage['name']} ({best_storage['efficiency']:.4f})")
    print(f"Best cost efficiency: {best_cost['name']} ({best_cost['efficiency']:.4f})")
    
def can_volume(radius, height):
    """Compute and return the volume of a right circular can."""
    return math.pi * radius**2 * height

def can_surface_area(radius, height):
    """Compute and return the surface area of a right circular can."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a can."""
    volume = can_volume(radius, height)
    surface_area = can_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    """Compute and return the cost efficiency of a can."""
    return volume / cost

main()