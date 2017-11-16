
import string

def alphabet_position(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter)

def rotate_character(char, rot):
    lowercase = list(string.ascii_lowercase)
    lower_char=char.lower()
    is_uppercase= True if lower_char != char else False   
    alph_position = alphabet_position(char)
    return_val=char
    if alph_position >= 0:
    
        return_val = (lowercase[(alph_position + rot) % 26])
    return return_val.upper() if is_uppercase else return_val

def encrypt(message, cypher=None):
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_message = ''
  for letter in message:
    if letter == ' ':
      new_message += ' '
    elif letter in lowercase:
      new_message += lowercase[(lowercase.index(letter) + cypher) % 26]
    elif letter in uppercase:
      new_message += uppercase[(uppercase.index(letter) + cypher) % 26]
    else:
        special_char=letter
        new_message=new_message+special_char
    
    
    
  return new_message