def main():
    n = int(input('Number to count to: '))
    fizzbuzz(n)


def fizzbuzz(n):

    for number in range(1, n + 1):

        if number % 5 == 0:
            if number % 3 == 0:
                print('FizzBuzz')

        if number % 3 == 0:
            print('Fizz')

        elif number % 5 == 0:
            print('Buzz')

        else:
            print(number)


if __name__ == "__main__":
    main()
