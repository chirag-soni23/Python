# Find the First Non-Repeated Character
input_str = "teetery"

for char in input_str:
       print(char)
       if input_str.count(char) == 1:
              print("Char is ", char)
              break

