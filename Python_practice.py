my_dictionary = {}
countries_dict = {}
countries_dict["Aarapahoe"] = 422829
countries_dict["Denver"] = 463353
countries_dict["Jefferson"] = 432438
countries_dict
voting_data = []
voting_data.append({"county": "El Paso", "registered_voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

