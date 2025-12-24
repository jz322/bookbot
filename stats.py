def count_words(text):
    words = text.split()
    num_words = 0
    for i in range(0, len(words)):
        num_words += 1
    return num_words

def number_of_characters(text):
    character_dict = {}
    for char in text:
        char = char.lower()
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(items):
    return items["num"]
def sort_dict (unsorted_dict):
    sorting_list = []
    for key in unsorted_dict:
        sorting_dict = {}
        sorting_dict['char'] = key
        sorting_dict['num'] = unsorted_dict[key]
        sorting_list.append(sorting_dict)
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list


    