import math

PADDING = 9
NOMBRE_DECIMAL = 3

NOMBRE_QUATRE = 4

print("nombre PI = {0:9.3}, nombre quatre = {1}".format(math.pi, NOMBRE_QUATRE))

#print(f"nombre PI = {math.pi:9.3}")
print(f"nombre PI = {math.pi:{PADDING}.{NOMBRE_DECIMAL}}")
