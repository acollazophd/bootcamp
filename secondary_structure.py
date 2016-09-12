def validate_para(structure):
    a = structure.count('(')
    b = structure.count(')')
    return a == b

def dotparen_to_bp(structure):
    mylist = []
    result = []
    for i, letter in enumerate(structure):
        if letter == '(':
            mylist.append(i)
        if letter == ')':
            closelist = mylist.pop()
            result.append((closelist, i))
    return result
