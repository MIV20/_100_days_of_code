# fucntions with outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print("Testing")
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("bELla", "THE raTY"))


def is_leap(year):
    """ Tests if a year is a leap year. Leap years have 29 days in the month of February"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month > 1:
        print("You have selected an invalid month.")

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
     month_days[1] += 1

    days = month_days[month -1]

    return days

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
