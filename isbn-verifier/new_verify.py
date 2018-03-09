def after_dash_check(isbn):
    # Takes in isbn as list without dashes
    numbers = "0123456789"

    for n in range(len(isbn)-1):    # Excludes the last one because of check digit
        if isbn[n] not in numbers:
            return False

    if isbn[9] == 'X':      # Checks if check digit is X or a number
        isbn[9] = '10'
    elif isbn[9] not in numbers:
        return False

    if sum([([int(i) for i in isbn][i])*(10-i) for i in range(10)]) % 11 == 0:
        # Changes isbn to int and uses validity formula
        return True
    else:
        return False

def verify(fed_isbn):
    # Main function; takes in isbn from test

    if "-" in fed_isbn and len(fed_isbn) == 13:
        # Checks if isbn has dashes and ensures length is 13 including dashes
        clean_isbn = list("".join(fed_isbn.split("-"))) # removes dashes
        return after_dash_check(clean_isbn) 

    elif len(fed_isbn) == 10:
        # Checks if isbn length is 10 withou dashes
        fed_isbn = list(fed_isbn) 
        return after_dash_check(fed_isbn)

    else: 
        return False

