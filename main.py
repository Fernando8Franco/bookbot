def main():
  book_path = "books/frankenstein.txt"
  book = read_book(book_path)
  book_words = count_book_words(book)
  book_letters_list = chars_dict_to_sorted_list(count_book_letters(book))
  print_report(book_words, book_letters_list)

def read_book(path):
  with open(path) as file:
    file_content = file.read()
  return file_content

def count_book_words(book):
  return (len(book.split()))

def count_book_letters(book):
  dictionary = {}
  for i in book.lower():
    if (not i.isalpha()):
      continue
    if(i in dictionary):
      dictionary[i] = dictionary[i] + 1
    else:
      dictionary[i] = 1
  return dictionary

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(dictionary):
  list = []
  for c in dictionary:
    list.append({"char": c, "num": dictionary[c]})
    list.sort(reverse=True, key=sort_on)
  return list

def print_report(book_words, book_letters_list):
  print(f"{book_words} is the number of words of the book")
  for c in book_letters_list:
    print(f"The '{c['char']}' character was found {c['num']} times")

main()