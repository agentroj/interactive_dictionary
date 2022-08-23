import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meriam(word):

    if word == "":
        print("Please input a word!")
        pass

    if word.lower() in data:
        return data[word]
        
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])

        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        print(f"No match found for the word {word}!")


in_str = input("Enter a word: ")

output = meriam(in_str)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
