# coding=utf-8
"""Exemple of Regular Expressions

"""

import re

pattern = r'(Via|Rd.) (L.|Luigi) Rizzo? (n|nr|numero)? (sei|sEi|6)?$'
"""Esempio di pattern da ricercare

r = specifica raw pattern (da mettere sempre)

^ = inizio riga
? = opzionale
()= Set di alternative: match exactly and remember as group
| = esclusivo uno dei

Per esempio questo pattern metcha con:
L. Rizzo
Via Luigi Rizzo numero 6
ecc...

ATTENZIONE AGLI SPAZZI !!

"""


def es1():
    print re.search(pattern, 'Via')  # return None
    print re.search(pattern, "Via L. Rizzo  ")  # found and return object (con 2 spazzi bianchi)


def es2():
    # Dato che è difficile decifrare un pattern conviene usare la modalità VERBOSE in questo modo

    my_pattern = '''
        ^                   # beginning of string
        M{0,3}              # thousands - 0 to 3 Ms
        (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                            #            or 500-800 (D, followed by 0 to 3 Cs)
        (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                            #        or 50-80 (L, followed by 0 to 3 Xs)
        (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                            #        or 5-8 (V, followed by 0 to 3 Is)
        $                   # end of string
        '''

    # modaità verbose
    print re.search(my_pattern, 'MCD', re.VERBOSE)


def es_phone_number():
    #     Here are the phone numbers I needed to be able to accept

    a = '800-555-1212'
    b = '800 555 1212'
    c = '800.555.1212'
    d = '(800) 555-1212'
    e = '1-800-555-1212'
    f = '800-555-1212-1234'
    g = '800-555-1212x1234'
    h = '800-555-1212 ext. 1234'
    i = 'work 1-(800) 555.1212 #1234'

    test = "{0:20}{1:20}{2:20}{3:20}\n{4:20}{5:20}{6:20}{7:20}\n{8:20}\n".format(a, b, c, d, e, f, g, h, i)
    print test

    my_pattern = '''
        (\d{3})     # 3 numbers digit ()= match exactly and remember groups
        (\D*|.|-)   # Separator can be a number (between 0 to any) of not number digit
                    # or .
                    # or -
        (\d{3})
        (\D*|.|-)
        (\d{4})     # 4 numbers digit
        '''

    result = re.search(my_pattern, test, re.VERBOSE)
    print result
    print result.groups()


if __name__ == '__main__':
    es1()
    es2()
    print '\nPhone Numbers Test:'
    es_phone_number()

    # this chapter covered a lot of notation, so here’s a quick review of what you learned:
    # the ? matches zero or one of the preceding group.
    # the * matches zero or more of the preceding group.
    # the + matches one or more of the preceding group.
    # the {n} matches exactly n of the preceding group.
    # the {n,} matches n or more of the preceding group.
    # the {,m} matches 0 to m of the preceding group.
    # the {n,m} matches at least n and at most m of the preceding group.
    # {n,m}? or *? or +? performs a nongreedy match of the preceding group.
    # ^spam means the string must begin with spam.
    # spam$ means the string must end with spam.
    # the . matches any character, except newline characters.
    # \d, \w, and \s match a digit, word, or space character, respectively.
    # \D, \W, and \S match anything except a digit, word, or space character, respectively.
    # [abc] matches any character between the brackets (such as a, b, or c).
    # [^abc] matches any character that isn’t between the brackets.
