def is_isogram(string):
    for i in string:
        if string.lower().count(i) > 1 and i != " " and i != "-":
            return False
    return True
    
        
