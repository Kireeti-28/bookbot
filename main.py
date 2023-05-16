def count_letters(text):
  mp = {}
  for char in ''.join(text.split()):
    if char.isalpha():
      if char.lower() not in mp:
        mp[char.lower()] = 1
      else:
        mp[char.lower()] += 1

  # Printing
  items = sorted(mp.items(), key=lambda x: x[1], reverse=True)
  for item in items:
    print(f"The '{item[0]}' character was found {item[1]} times")



def count_total_words(text):
  print('{0} words found in the document'.format(len(text.split())))

with open("books//frankenstein.txt") as f:
  file_contents = f.read()
  print('--- Begin report of books/frankenstein.txt ---')
  count_total_words(file_contents)
  count_letters(file_contents)
  print('--- End report ---')