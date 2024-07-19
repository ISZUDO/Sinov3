from transliterate import to_cyrillic, to_latin, transliterate
import regex

check = bool(regex.search(r'\p{IsCyrilic}', 'salom'))

def cril_or_latin(text):
  check = bool(regex.search(r'\p{IsCyrilic}', 'salom'))
  if check == True:
       result = to_latin(text)
  else:
      result = to_cyrillic(text)
  return result  