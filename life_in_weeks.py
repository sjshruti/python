
age = input("What is your current age?")


age_as_int = int(age)

years_remaining = 90 - age_as_int

day_remaining = years_remaining * 365

months_remaining = years_remaining * 12

weeks_remaining = years_remaining * 52

print(f"you have {day_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
