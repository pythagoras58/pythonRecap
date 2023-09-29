# breaking programs into smaller chunks - function

def hello_func() :
    print("Say Hello")


# call the function
hello_func()


# Arguments in functions
def hello_user(name) :
    print(f'Hello, {name}')


hello_user('Messi')
hello_user('Ronaldo')
hello_user('Salah')


def players(name, number) :
    print(f'{name} is Number {number}')


players('Messi', 10)
players('Ronaldo', 7)
players('Neymar', 11)

# List as function parameter
def food(fruits):
    print("=====Fruit List====")
    for x in fruits:
        print(x)


fruits = {'Banana','Orange','Mango','Apple'}
food(fruits)


# returning values
def numbers(x):
    return 10 * x


print(f'Values of x: {numbers(10)}')