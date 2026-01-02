# 20201027 - Make a Vessel of Height
def height_needed(volume):
    import math
    return round((volume * 3 / (math.pi * 5 ** 2))*1000, 2)

print(height_needed(0.5))