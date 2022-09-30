# Python Dictionaries
students_score = {"busko": 50, "anointing": 67, "toby": 83}

# To access
students_score["busko"]

# To edit
students_score["busko"] = 78

# To add new key-value pair
students_score["maxwell"] = 92

# loop through dictionary
for key in students_score:
   print(key)  # => busko, anointing, toby, maxwell

# Create a new and empty dictionary
food_prices = {}   # or dict()
