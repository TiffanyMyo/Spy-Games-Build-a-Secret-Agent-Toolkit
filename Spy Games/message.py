def decode(text):
   result = ''
   for char in text:
       if char.isalpha():
           base = ord('A') if char.isupper() else ord('a')
           shifted = (ord(char) - base - 3) % 26 + base
           result += chr(shifted)
       else:
           result += char
   return result
