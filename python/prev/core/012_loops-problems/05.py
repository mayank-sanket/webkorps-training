# string = "ASSAMTRIPURA"

input_str = "ASSAMTRIPURA"

for char in input_str:
    if input_str.count(char) == 1:
        print(char)
        break  # here break keyword is necessary because if we don't use it, then it will also print the next non-repeating character in the string

