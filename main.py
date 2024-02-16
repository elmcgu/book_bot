def main():
    print("WORD COUNT = " + str(count_words(get_text(get_path()))))

def get_path():
    return input("Input relative path of text file from main.py: ")

def get_text(path_to_file):    
    with open(path_to_file) as f:
        return f.read()
    
def count_words(file_contents):
    return len(file_contents.split())
    

    
main()