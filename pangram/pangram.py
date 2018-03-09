def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'     
    for i in alphabet:
        if i in sentence.lower():
            check = True
        else:
            check = False
            break
    return check
