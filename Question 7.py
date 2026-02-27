def days_since_birthday(birthday):
    # birthday format: "DD-MM-YYYY"

    parts = birthday.split("-")
    birth_year = int(parts[2])

    # manually set current year (since we cannot import anything)
    current_year = 2026

    # calculate full years only (exclude birth year and current year)
    full_years = current_year - birth_year - 1

    days = full_years * 365

    return days

print(days_since_birthday("26-05-2006"))