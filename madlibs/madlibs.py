# String concatenation
# Suppose we want to create a string that says "subscript to ____"

# Few ways to do this
# youtuber = "FreeCodeCamp"
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}!"

print(madlib)