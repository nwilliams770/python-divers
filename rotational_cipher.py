
def _get_ascii_from_char(s):
  return ord(s)

def _get_char_from_ascii(num):
  return chr(num)

def rotationalCipher(input, rotation_factor):
  # Write your code here
  # If rotation_fator > 26, we've wrapped around for chars and
  # If > 10, wrapped around for nums
  char_rotation_factor = rotation_factor % 26
  num_rotation_factor = rotation_factor % 10

  # Iterate through each char
  for i in range(0, len(input)):
    ascii_val = _get_ascii_from_char(input[i])

    if ascii_val >= 65 and ascii_val <= 90:
      ascii_val += char_rotation_factor
      if ascii_val > 90:
        ascii_val = (ascii_val % 90) + 65 - 1
    elif ascii_val >= 97 and ascii_val <= 122:
      ascii_val += char_rotation_factor
      if ascii_val > 122:
        ascii_val = (ascii_val % 122) + 97 - 1
    elif ascii_val >= 48 and ascii_val <= 57:
      ascii_val += num_rotation_factor
      if ascii_val > 57:
        ascii_val = (ascii_val % 57) + 48 - 1

    new_char = _get_char_from_ascii(ascii_val)

    input = input[0:i] + new_char + input[i+1:]


  return input
