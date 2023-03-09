from app1.exercise.converters13 import convert
from app1.exercise.parsers13 import parse

feet_inches=input("Enter feet and inches: ")

parsed= parse(feet_inches)
result= convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")
if result<1:
    print("Kis is too small.")
else:
    print("Kid can use the slide.")
