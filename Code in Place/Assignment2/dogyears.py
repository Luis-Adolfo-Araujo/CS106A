def main():
    humans = int(input("enter an age in human years: "))
    print(f"The age in dog years is {dogs_age(humans)}")


def dogs_age(humans):
    humans = humans * 7
    return humans


if __name__ == "__main__":
    main()
