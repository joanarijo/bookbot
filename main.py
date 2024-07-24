def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
    words_counter = words_count(file_contents)
    characters_dict = characters_count(file_contents)
    sorted_dictionary = sort_dict(characters_dict)
    report(file, words_counter, sorted_dictionary)

def words_count(content):
    words_split = content.split()
    words_counter = len(words_split)
    return words_counter

def characters_count(content):
    lowered_content = content.lower()
    characters_dict = {};
    for character in lowered_content:
            if character.isalpha():
                if character in characters_dict:
                    characters_dict[character] += 1
                else:
                    characters_dict[character] = 1
    return characters_dict

def sort_dict(dictionary, reverse=True):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict

def report(file, words_counter, dictionary):
    print(f"--- Begin report of {file} ---")
    print(f"{words_counter} words found in the document \n")
    for character in dictionary:
        print(f"The '{character}' character was found {dictionary[character]} times")
    print(f"--- End report ---")

if __name__ == "__main__":
    main()