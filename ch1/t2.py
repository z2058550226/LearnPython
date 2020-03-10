movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    [
        "Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
    ]
]


def print_lol(the_list, indent):
    i_string = ''
    i = 0
    while i < indent:
        i_string = i_string + '  '
        i = i + 1
    for item in the_list:
        if isinstance(item, list):
            print(i_string + '[')
            print_lol(item, indent + 1)
            print(i_string + ']')
        else:
            print(i_string + str(item))


print_lol(movies, 0)
