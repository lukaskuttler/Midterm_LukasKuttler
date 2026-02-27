# LIST (mutable)

swiss_cities = ["Geneva", "Zurich", "Bern"]
print("Original list:", swiss_cities)

# modify the same list
swiss_cities[1] = "Lausanne"
print("Modified list:", swiss_cities)


# STRING (immutable)

country = "Switzerland"
print("Original string:", country)

# country[0] = "s"   # This would cause a TypeError

# create a new string instead
new_country = "s" + country[1:]
print("New string:", new_country)