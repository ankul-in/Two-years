#kata
#https://www.codewars.com/kata/57cf3dad05c186ba22000348/train/python

def decode_resistor_colors(bands):
    colorCode = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
    }
    multiplierCode = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
        "green": 100000, "blue": 1000000, "violet": 10000000,
        "gray": 100000000, "white": 1000000000,
        "gold": 0.1, "silver": 0.01
    }
    toleranceCode = {
        "brown": "1%", "red": "2%", "green": "0.5%", "blue": "0.25%",
        "violet": "0.1%", "gray": "0.05%", "gold": "5%", "silver": "10%"
    }

    x = bands.split()
    base_value = int(str(colorCode[x[0]]) + str(colorCode[x[1]]))
    multiplier = multiplierCode.get(x[2], 1)
    tolerance = toleranceCode.get(x[3], "20%") if len(x) > 3 else "20%"

    def format_resistance(value):
        if value >= 1_000_000:
            return f"{value / 1_000_000:.0f}M"
        elif value >= 1000:
            return f"{value / 1000:.0f}k"
        else:
            return f"{int(value)}"
    resistance = base_value * multiplier
    return f"{format_resistance(resistance)} ohms, {tolerance}"