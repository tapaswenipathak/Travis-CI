def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'world'


def main():
    hello(say_what())

if __name__=="__main__":
	main()
