def get_amount_of_words(text):
    count = 0
    words = text.split()
    for x in words:
        count = count + 1
    return count

def get_amount_of_characters(text):
    characters ={}
    lower_text = text.lower()
    for x in lower_text:
        if x not in characters:
            characters[x] = 1
        else:
            characters[x] = characters.get(x,0) + 1
    return characters

def sort_on(items):
    return items["num"]
def sort_dictionary(dictionary):
    new_dictionary = {"char":"","num":0}
    new_list = []
    for x in dictionary:
        new_dictionary["char"] = x
        new_dictionary["num"] = dictionary[x]
        new_list.append(new_dictionary)
        new_dictionary = {"char":"","num":0}
    new_list.sort(reverse=True,key=sort_on)
    return new_list



