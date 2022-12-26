import my_modules.vsearch as vs
from pprint import pprint


def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(args):
    print('Before: ', args)
    args.append('More date')
    print('After: ', args)


pprint(__name__)
pprint(vs.search4letters('Alisha', 'alkalise'))
pprint(double(785))
pprint(change([156]))
