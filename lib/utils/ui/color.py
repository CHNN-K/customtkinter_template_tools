import re

class Color:
    def __init__(self):
        self.background = "#2A2A2A"
        self.background_frame = "#181717"
        self.white = "#F2F2F2"
        self.red = "#C00000"
        self.green = "#00B050"
        self.blue = "#0078D4"
        self.black = "#0D0D0D"
        self.pink = "#F24171"
        self.gray = "#424242"
        self.yellow = "#FFDE21"
        self.darkblue = "#000080"
        self.orange = "#FFA500"
        
        self.transparent = "transparent"
        self.disable = "#626262"
        
        self.toplevel_background = "#D9D9D9"
        self.widget_background = "#D9D9D9"
        self.table_background = "#909090"
    
    def darker_color(self, hex_color : str, percentage : int = 20):
        percentage = percentage/100
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')

        # Convert hex to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        # Darken each channel by the percentage
        r = int(r * (1 - percentage))
        g = int(g * (1 - percentage))
        b = int(b * (1 - percentage))

        # Ensure values are within the RGB range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        # Convert RGB back to hex
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def brighter_color(self, hex_color : str, percentage : int = 20):
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')

        # Convert hex to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        # Lighten each channel by the percentage
        r = int(r + (255 - r) * percentage)
        g = int(g + (255 - g) * percentage)
        b = int(b + (255 - b) * percentage)

        # Ensure values are within the RGB range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        # Convert RGB back to hex
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def rgb_to_hex(self, rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)
    
    def hex_to_rgb(self, hex : str):
        hex = hex.lstrip('#')
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    def is_hex(self, color):
        hex_pattern = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}|[A-Fa-f0-9]{8})$'
        return bool(re.match(hex_pattern, color))
    
    def is_rgb_color(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            return all(isinstance(i, int) and 0 <= i <= 255 for i in color)
        return False