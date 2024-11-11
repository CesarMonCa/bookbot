def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    
    # Print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    # Sort characters by frequency in descending order and print each alphabetic character's count
    for char, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    """Return a dictionary with the count of each character in the text."""
    text = text.lower()  # Convert text to lowercase
    character_counts = {}  # Initialize an empty dictionary to store character counts
    
    for char in text:  # Iterate over each character in the text
        if char in character_counts:
            character_counts[char] += 1  # Increment count if character exists
        else:
            character_counts[char] = 1   # Initialize count if character is new
    
    return character_counts

# Call the main function to run the program
main()

