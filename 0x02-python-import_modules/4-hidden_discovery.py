#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all the names defined in hidden_4"""

    import hidden_4
    for name in dir(hidden_4):
        if name.startswith('__'):
            continue
        print("{:s}".format(name))
