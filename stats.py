def get_book_text(filepath): 
    with open(filepath) as text:
        contents = text.read()
        word_count = contents.split()
        print(f"Found {len(word_count)} total words")
    
def character_count(filepath):
    with open(filepath) as text:
        contents = text.read()
        lowercase_contents = contents.lower()
        char_counts = {}
        for char in lowercase_contents:
            char_counts[char] = char_counts.get(char, 0) + 1
        print(f"{char_counts}")
        return char_counts

def sort_on(chars):
    return chars["num"]

def character_sort(filepath):
    char_list = []
    char_dict = character_count(filepath)
    for char in char_dict:
        if not char.isalpha():
            continue
        count = char_dict[char]
        char_list.append({"char":char, "num":count})
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

