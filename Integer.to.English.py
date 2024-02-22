# Integer to English: Zero to One Million. This code turns the integers 0 to 1,000,000
# into its representative English word.

def int_to_english_digit(n):
    """
    Returns a string with the equivalent English text of each digit

    Parameters:
        n (int): an integer greater than or equal to zero

    Returns:
        str: returns '"zero", "one", "two", "three", "four", "five", "six",
        "seven","eight", "nine" depending on the integers in parameter "n"

    Examples:
        >>> int_to_english_digit (789)
        'seven eight nine'

        >>> int_to_english_digit (1234)
        'one two three four'
    """

    list_eng_num = ["zero", "one", "two", "three", "four", "five", "six",
                    "seven", "eight", "nine"]

    all_eng_num = ""
    for num in str(n):
      eng_num = list_eng_num[int(num)]
      all_eng_num += eng_num + " "

    return all_eng_num.strip()


def zero_to_nine(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to zero less than or equal 9

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> zero_to_nine (5)
        'five'

        >>> zero_to_nine (9)
        'nine'
  """

  str_n = str(n)

  if len(str_n) > 1 and str_n[len(str_n)-1] == "0":
    return "" #takes away zero from large numbers (ex.20 twenty zero)

  else:
    for num in str_n[len(str_n)-1]:
      return int_to_english_digit(int(num)).strip()


def ten_to_nineteen(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to 10 and less than or equal 19

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> ten_to_nineteen (10)
        'ten'

        >>> ten_to_nineteen (19)
        'nineteen'
  """

  str_n = str(n)

  num_10_to_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                    "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]

  # looks for a one in the tens digit and returns number based on ones digit
  if str_n[len(str_n)-2] == "1":
    for num in str_n[len(str_n)-1]:
      eng_num = num_10_to_19[int(num)]

    return eng_num.strip()

def twenty_to_ninetynine(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to twenty and less than or
        equal to ninety-nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (20)
        'twenty'su

        >>> twenty_to_ninetynine (99)
        'ninety-nine'
  """

  str_n = str(n)

  num_0_to_90 = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty",
                    "seventy","eighty", "ninety"]

#list numbers based on tens digit and concats ones digit if not zero
  if str_n[len(str_n)-2] != "1" and str_n[len(str_n)-1] != "0":
    for num in str_n[len(str_n)-2]:
      eng_num = num_0_to_90[int(num)]

    return (eng_num + "-" + zero_to_nine(n)).strip()

#list numbers based on tens digit
  else:
    for num in str_n[len(str_n)-2]:
      eng_num = num_0_to_90[int(num)]
    return eng_num.strip()

def twenty_to_ninetynine_without_dash(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to twenty and less than or
        equal to ninety nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (20)
        'twenty'

        >>> twenty_to_ninetynine (99)
        'ninety nine'
  """
#same as the function above although hyphen is removed in order to use this
#function later on for larger numbers where hyphen is not needed

  str_n = str(n)

  num_0_to_90 = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty",
                    "seventy","eighty", "ninety"]

  if str_n[len(str_n)-2] != "1" and str_n[len(str_n)-1] != "0":
    for num in str_n[len(str_n)-2]:
      eng_num = num_0_to_90[int(num)]

    return (eng_num + " " + zero_to_nine(n)).strip()

  else:
    for num in str_n[len(str_n)-2]:
      eng_num = num_0_to_90[int(num)]
    return eng_num.strip()



def hundred_to_999(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to one hundred and less than
        or equal to nine hundred ninety-nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (120)
        'one hundred twenty'

        >>> twenty_to_ninetynine (999)
        'nine hundred ninety-nine'
  """
  str_n = str(n)

  num_0_to_900 = ["", "one hundred", "two hundred", "three hundred",
                    "four hundred", "five hundred", "six hundred",
                    "seven hundred", "eight hundred","nine hundred"]

#list numbers based on hundreds digit and concats tens digit using prior functions

  if str_n[len(str_n)-2] > "1":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + twenty_to_ninetynine(n)).strip()

  elif str_n[len(str_n)-2] == "1":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + ten_to_nineteen(n)).strip()

#list numbers based on hundreds digit and concats ones digit using prior functions

  elif str_n[len(str_n)-2] == "0" and str_n[len(str_n)-1] > "0":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + zero_to_nine(n)).strip()

#list numbers based on hundreds digit

  elif str_n[len(str_n)-2] == "0" and str_n[len(str_n)-1] == "0":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num).strip()


def hundred_to_999_no_dash(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to one hundred and less than
        or equal to nine hundred ninety-nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (120)
        'one hundred twenty'

        >>> twenty_to_ninetynine (999)
        'nine hundred ninety-nine'
  """
#same as the function above although hyphen is removed in order to use this
#function later on for larger numbers where hyphen is not needed

  str_n = str(n)

  num_0_to_900 = ["", "one hundred", "two hundred", "three hundred",
                    "four hundred", "five hundred", "six hundred",
                    "seven hundred", "eight hundred","nine hundred"]

  if str_n[len(str_n)-2] > "1":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + twenty_to_ninetynine_without_dash(n)).strip()

  elif str_n[len(str_n)-2] == "1":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + ten_to_nineteen(n)).strip()

  elif str_n[len(str_n)-2] == "0" and str_n[len(str_n)-1] > "0":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num + " " + zero_to_nine(n)).strip()

  elif str_n[len(str_n)-2] == "0" and str_n[len(str_n)-1] == "0":
    for num in str_n[len(str_n)-3]:
      eng_num = num_0_to_900[int(num)]

    return (eng_num).strip()


def thousand_to_9999(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to one thousand and less than
        or equal to nine thousand nine hundred ninety-nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (1120)
        'one thousand one hundred twenty'

        >>> twenty_to_ninetynine (9999)
        'nine thousand nine hundred ninety-nine'
  """

  str_n = str(n)
  n = str_n[len(str_n)-3:]

  num_0_to_9000 = ["", "one thousand", "two thousand", "three thousand",
                    "four thousand", "five thousand", "six thousand",
                    "seven thousand", "eight thousand","nine thousand"]

#list numbers based on thousands digit and concat hundred function
#using prior functions

  for num in str_n[len(str_n)-4]:
      eng_num = num_0_to_9000[int(num)]

  return (eng_num + " " + hundred_to_999(n)).strip()

def tenthousand_to_99999(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to ten thousand and less than
        or equal to ninety nine thousand ninety-nine

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (35120)
        'thirty five thousand one hundred twenty'

        >>> twenty_to_ninetynine (99999)
        'ninety nine thousand nine hundred ninety-nine'
  """
#slices ten thousands place value and concat hundred function using prior functions

  str_n = str(n)
  n1 = str_n[len(str_n) - 5:len(str_n) - 3]
  n2 = str_n[len(str_n)-3:]

  if int(n1) >= 10 and int(n1) <= 19:
    return (ten_to_nineteen(n1) + " thousand " + hundred_to_999(n2)).strip()

  if int(n1) >= 20 and int(n1) <= 99:
    return (twenty_to_ninetynine_without_dash(n1) + " thousand " +
            hundred_to_999(n2)).strip()

def onehundredthousand_to_million(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to one hundred thousand
        and less than or equal to one million

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> twenty_to_ninetynine (655120)
        'six hundred fifty five thousand one hundred twenty'

        >>> twenty_to_ninetynine (999999)
        'nine hundred ninety nine thousand nine hundred ninety-nine'
  """
#slices hundred thousands place value and concat hundred function
#using prior functions

  str_n = str(n)
  n1 = str_n[len(str_n) - 6:len(str_n) - 3]
  n2 = str_n[len(str_n)-3:]

  if int(n1) >= 100 and int(n1) <= 999:
    return (hundred_to_999_no_dash(n1) + " thousand " +
            hundred_to_999(n2)).strip()

  if n > 999999:
    return "one million"

def int_to_eng(n):
  """
    Returns a string with the equivalent English word

    Parameters:
        n (int): an integer greater than or equal to zero and less than or equal
        to one million

    Returns:
        str: returns English word depending on the integers in parameter "n"

    Examples:
        >>> int_to_english_digit (789)
        'seven hundred eighty-nine'

        >>> int_to_english_digit (999999)
        'nine hundred ninety nine thousand ninety-nine'
  """
#Testing 
#returns one of the functions above based on the integer n

  if n <= 9:
    return zero_to_nine(n)
  elif n >= 10 and n <= 19:
    return ten_to_nineteen(n)
  elif n >= 20 and n <= 99:
    return twenty_to_ninetynine(n)
  elif n >= 100 and n <= 999:
    return hundred_to_999(n)
  elif n >= 1000 and n <= 9999:
    return thousand_to_9999(n)
  elif n >= 10000 and n <= 99999:
    return tenthousand_to_99999(n)
  elif n >= 100000:
    return onehundredthousand_to_million(n)
  
  # single digit in the ones
assert int_to_eng(0) == "zero"
assert int_to_eng(4) == "four"

# numbers >= 10 and <= 20
assert int_to_eng(10) == "ten"
assert int_to_eng(14) == "fourteen"
assert int_to_eng(20) == "twenty"

# numbers >= 21 and <= 999
assert int_to_eng(65) == "sixty-five"
assert int_to_eng(100) == "one hundred"
assert int_to_eng(303) == "three hundred three"
assert int_to_eng(817) == "eight hundred seventeen"
assert int_to_eng(999) == "nine hundred ninety-nine"

# numbers >= 1000 and <= 9999
assert int_to_eng(1000) == "one thousand"
assert int_to_eng(2005) == "two thousand five"
assert int_to_eng(2098) == "two thousand ninety-eight"
assert int_to_eng(2700) == "two thousand seven hundred"
assert int_to_eng(2698) == "two thousand six hundred ninety-eight"
assert int_to_eng(9999) == "nine thousand nine hundred ninety-nine"

# numbers >= 10000 and <= 99999
assert int_to_eng(10000) == "ten thousand"
assert int_to_eng(10008) == "ten thousand eight"
assert int_to_eng(10015) == "ten thousand fifteen"
assert int_to_eng(10068) == "ten thousand sixty-eight"
assert int_to_eng(10300) == "ten thousand three hundred"
assert int_to_eng(10453) == "ten thousand four hundred fifty-three"
assert int_to_eng(13999) == "thirteen thousand nine hundred ninety-nine"
assert int_to_eng(92479) == "ninety two thousand four hundred seventy-nine"

# numbers >= 100000 and <= 999999
assert int_to_eng(100000) == "one hundred thousand"
assert int_to_eng(100002) == "one hundred thousand two"
assert int_to_eng(100011) == "one hundred thousand eleven"
assert int_to_eng(300471) == "three hundred thousand four hundred seventy-one"
assert int_to_eng(999999) == "nine hundred ninety nine thousand nine hundred ninety-nine"
assert int_to_eng(1000000) == "one million"


# User is asked for an integer between 0 and 1,000,000
def main():
    while True:
        try:
            n = int(input("Enter an integer between 0 and 1,000,000: "))
            if n < 0 or n > 1000000:
                print("Please enter a valid integer between 0 and 1,000,000.")
                continue
            print("Equivalent English word:", int_to_eng(n))
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()