def main():
    path = input("Input relative path of text file from main.py: ")

    with open(path) as f:
        text = f.read()

    words = text.split()
    word_count = len(words)
    
    print("WORD COUNT =", word_count)

    letter_count = count_letters(words)

    sorted_list = sort_letter_counts(letter_count)

    report(path, sorted_list)


def count_letters(words):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"]  
    letter_counts = {letter: 0 for letter in alphabet}

    for word in words:
        for letter in word.lower():
            if letter in alphabet:
                letter_counts[letter] += 1

    return letter_counts

def sort_letter_counts(letter_dict):
    letter_count_list=[]
    for item in letter_dict:
        letter_count_list.append({item:letter_dict[item]}) 
   
    sorted_letter_count_list = sorted(letter_count_list, key=lambda x: list(x.values())[0], reverse=True)
    return sorted_letter_count_list
    
def report(path, sorted_list):
    print(f"Analysing {path}")
    print(".......")
    print(".......")
    for item in sorted_list:
        for key in item:
            print(f"I found the letter {key}, {item[key]} times!")


main()