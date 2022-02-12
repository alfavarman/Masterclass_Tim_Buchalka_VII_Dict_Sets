#  Unstructured collection of values stored via unique keys
#  Iterable, Mutable/Variable,
# Can't : use indexes, can use keys
# dictionary = {
#               'employer_1' : 'min income 1500 USD',
#               'employer_2' : 'min income 3000 USD',
#               'employer_3' : 'min income 7000 USD',
#               }
# 'key' : 'value',


employment = {
                'no_employment': 'income 0 USD',
                'employer_1': 'min income 1500 USD',
                'employer_2': 'min income 3000 USD',
                'employer_3': 'min income 7000 USD',
                'employer_4': 'min income 10000 USD',
            }

# 1. Pull value
#   indexing with key
#   wrong key -> error but faster
#my_income = employment['employer_1']
#print(my_income)
#
#   pull .get method
#   wrong key -> None but longer
#my_actual_inc = employment.get("no_employment")
#print(f"\n{my_actual_inc}")
#####################
#####################

# 2. Iterating
# # a. less efficient
# for key in employment:
#     print(key, employment[key], sep=": ")
# # b. dictionary `enumerate` PRO!
# for key, value in employment.items():
#     print(key, value, sep=":: ")

# 3. Adding elements: dictionaries doesnt have .append method
# dict preserve insertion order since p 3.6
employment["previous_employer"] = "variable income"
for key in employment:
    print(key, employment[key], sep=":: ")

# 4. Updating value same as adding but use same key:
employment["previous_employer"] = "Rainbow"
for key in employment:
    print(key, employment[key], sep=":: ")

# 5. deleting item
del employment["previous_employer"]
