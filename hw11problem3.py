# Fix this code below line 11! Don't change the rainbow variable!
rainbow = {
  "name": "Roy G. Biv",
  "colors": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
  "end": "Pot Of Gold!",
  "number": "double",
  "count": 2,
  "gold": 100
}

# ------------------------------------------------------
# Start Fixing Below Here
# You may encounter: NameError, SyntaxError, IndentationError, KeyError, TypeError, etc.
print("The rainbow's name is", rainbow["name"])

if rainbow["end"] == "Pot Of Gold!":
    print("I'll be taking that gold!")
else:
    print("No money for me!")

for color in rainbow["colors"]:
    if color is not "indigo":
      print(color)
    else:
      print("What color is indigo?")

print(100 + rainbow["count"])

gold_amount = rainbow["gold"]
print('{0:.1f}'.format(gold_amount))