# months list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# input date
while True:
    date = input("Date: ").strip()

    # date is numeric format
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        # defining errors
        except (ValueError, AttributeError, NameError, KeyError):
            pass

    # date is word format
    elif "," in date:
        try:
            month_day, year2 = date.split(",")
            month2, day2 = month_day.split(" ")
            year2 = int(year2)
            day2 = int(day2)
            month2 = months.index(month2) + 1
            if month2 <= 12 and day2 <= 31:
                print(f"{year2}-{month2:02}-{day2:02}")
                break
            else:
                continue
        # defining errors
        except (ValueError, AttributeError, NameError, KeyError):
            pass
    else:
        continue

