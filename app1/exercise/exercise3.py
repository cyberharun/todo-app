import math

liters=float(input("Please enter liters to convert to cubic meters: "))

def convert(liters):
    cubic_meter=float(liters/(1000))
    return f"{liters} liters is equal to {cubic_meter} cubic meters"

result=convert(liters)
print(result)
