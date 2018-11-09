def reverse_hash(n):
    letters = 'acdegilmnoprstuw'
    y = n
    l = list()
    l.append(n)
    s = ''
    while y/259 >= 7:
        y = y/37
        l.append(y)
    first_character = l[len(l)-1] - 259
    try:
        l.reverse()
        s = s + letters[first_character]
        for m in range(0, len(l)-1):
            s = s+letters[l[m+1] - l[m]*37]
        return s
    except IndexError:
        return 'Not a valid hash number'


