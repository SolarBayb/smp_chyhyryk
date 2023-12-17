def get_color_from_code(code):
    color_map = {
        1: 'yellow',
        2: 'red',
        3: 'blue',
        4: 'green',
        5: 'purple',
        6: 'orange',
        7: 'pink',
        8: 'grey',
        9: 'brown',
        10: 'cyan'
    }
    return color_map.get(code, "unknown")  # Default to "unknown" if the code is not found

def generate_ascii_art(star):
    # Assuming star is an instance of Star3D and has a color_code attribute.
    color = get_color_from_code(star.color_code)
    # Placeholder for ASCII art generation logic
    art = f"A {color} 3D star with {star.spikes} spikes, outer radius {star.outer_radius}, inner radius {star.inner_radius}, and depth {star.depth}."
    return art
