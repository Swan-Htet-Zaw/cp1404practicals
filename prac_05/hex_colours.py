"""
Hex Colour Lookup
Estimate: 15 minutes
Actual:   18 minutes
"""

HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

colour_name = input("Enter a colour name: ").strip()

while colour_name:
    hex_code = HEX_COLOURS.get(colour_name.capitalize())
    if hex_code:
        print(f"{colour_name.capitalize()} has hex code {hex_code}")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").strip()
