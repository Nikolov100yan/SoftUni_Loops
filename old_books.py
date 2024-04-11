favorite_book_name = input()
text_input = input()
number_checked_books = 0

while text_input != favorite_book_name:
    text_input = input()
    number_checked_books += 1
    if text_input == "No More Books":
        break
    continue

if text_input == favorite_book_name:
    print(f"You checked {number_checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {number_checked_books} books.")
