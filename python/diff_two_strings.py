# Source https://stackoverflow.com/a/17904977
import difflib

cases = [('afrykanerskojęzyczny', 'afrykanerskojęzycznym')]

for a, b in cases:
    print("{} => {}".format(a, b))
    for i, s in enumerate(difflib.ndiff(a, b)):
        if s[0] == " ":
            continue
        elif s[0] == "-":
            print(u'Delete "{}" from position {}'.format(s[-1], i))
        elif s[0] == "+":
            print(u'Add "{}" to position {}'.format(s[-1], i))
    print()
