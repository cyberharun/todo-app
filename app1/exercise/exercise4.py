def years(year_of_birth,current_year=2023):
    number_of_years=current_year-year_of_birth
    return number_of_years

year_of_birth=int(input("Please enter your birth year: "))

year=years(year_of_birth)

print(year)

if year>120:
    print("You are so old.")
else:
    print("You are under 120 years.")
