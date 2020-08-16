from datetime import datetime


def check_birthdate(year, month, day):
    # write code here
    todays_date = datetime(2019, 9, 4)
    birthdate = datetime(year, month, day)
    if birthdate > todays_date:
        return False
    else:
        return True


def calculate_age(year, month, day):
    # write code here
    todays_date = datetime(2019, 9, 4)
    birthdate = datetime(year, month, day)
    difference = todays_date - birthdate
    print("You are %d years old." % (difference.days / 365))


def main():
    # write main code here
    year = int(input("Enter year of birth: "))
    month = int(input("Enter month of birth: "))
    day = int(input("Enter day of birth: "))
    if check_birthdate(year, month, day):
        calculate_age(year, month, day)
    else:
        print("birthdate is invalid")


if __name__ == '__main__':
    main()
