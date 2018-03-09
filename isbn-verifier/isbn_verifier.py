def verify(isbn):
    isbn = str(isbn).replace('-', '')
    
    # Check length of the code
    if len(isbn) != 10:
        return False

    # Check the 9 main digits
    if not isbn[:-1].isnumeric(): 
        return False
        
    # Check the check digit
    if isbn[-1] != 'X' and not isbn[-1].isnumeric():
        return False

    # Check the validity formula
    else:
        isbn = [int(i) if i != 'X' else 10 for i in isbn]
        return (sum([(10 - k) * i for i, k in zip(isbn, range(10))]) % 11) == 0