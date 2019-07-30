""" A phone book with numbers """

# using dictionary to create a phone book 
# names are the keys and the numbers are the values

phone_book = {"Sam": 6399160096,
              "Aaron": 7489809897,
              "Zoe": 6380989798,
              "Mia": 3068780909}

# creating a function to do the reverse look up
def caller_id(number):
    for key, value in phone_book.items():
        if number == value:
            print(key)
        else:
            print("Opps not this one, this is {}'s number".format(key))

caller_id(6399160096)
