def get_book_text(input):
    with open(input) as f:
        return f.read()

def get_num_words(input):
    text = get_book_text(input)
    return len(text.split())

def get_num_chars(input):
    char_dict = {}
    text = get_book_text(input)
    for c in text:
        if c.lower() in char_dict:
            char_dict[c.lower()] += 1
        else:
            char_dict[c.lower()] = 1
    return char_dict

def get_sort_on(dict):
    return dict["num"]

def get_sorted_list_of_dict(char_dict):
    result_list = []
    for k, v in char_dict.items():
        result_list.append({"char": k, "num": v})
    result_list.sort(key=get_sort_on, reverse=True)
    return result_list