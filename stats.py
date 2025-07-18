def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def make_dict_list(chars):
    dict_list = []
    for key, value in chars.items():
        dict_list.append({"char": key, "num": value})
        dict_list.sort(reverse=True, key=sort_on)
    return dict_list


