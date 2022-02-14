# [dict] Unstructured collection of values stored via unique keys
# Iterable, Mutable/Variable,
# Can't : use indexes, can use keys
# KEY - must be hashable - must be immutable - constant or tuple
# But tuple CAN'T contain list!
# Value - any object
#
# dictionary = {
#               'employer_1' : 'min income 1500 USD',
#               'employer_2' : 'min income 3000 USD',
#               'employer_3' : 'min income 7000 USD',
#               }
# 'key' : 'value',
# different ways to create dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('three', 3), ('one', 1)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'three': 3, 'one': 1}, two=2)
print(a == b == c == d == e == f) # True :)


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
# print("\n 1. Pull Value")
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
# print("\n 2. Iterating")
# for key in employment:
#     print(key, employment[key], sep=": ")
# # b. dictionary `enumerate` PRO!
# for key, value in employment.items():
#     print(key, value, sep=":: ")

# 3. Adding elements: dictionaries doesnt have .append method
# dict preserve insertion order since p 3.6
print("\n 3. Adding elements")
employment["previous_employer"] = "variable income"
employment["dream employer"] = "dream income 40 000 USD"
for key in employment:
    print(key, employment[key], sep=":: ")


# 4. Updating value same as adding but use same key:
print("\n 4. Update elements")
employment["previous_employer"] = "Rainbow"
for key in employment:
    print(key, employment[key], sep=":: ")

# 5. deleting item
# del - just remove value, return error if wrong key
print("\n 5. remove elements")
del employment["previous_employer"]
# remove value dict/list and return value
employment.pop("dream employer")
for key in employment:
    print(key, employment[key], sep="==> ")
# wrong key handle with no error:
i = employment.pop("non_exist_employer", None)
ii = employment.pop("non_exist_employer2", "no value exist with such a key")
print(f"\n i = employment.pop(\"non_exist_employer\", None) Returns: \n {i}\n "
      f"\n ii = employment.pop(\"non_exist_employer2\", \"no value exist with such a key\") \n {ii} ")