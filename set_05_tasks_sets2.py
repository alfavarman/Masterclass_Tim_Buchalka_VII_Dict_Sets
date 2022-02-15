favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.
# suggestion - sorted list of favourites - items in basket
# suggestions = sorted(favourites - basket)
# print(suggestions)

suggestion = favourites.difference(basket)
print(sorted(suggestion))
