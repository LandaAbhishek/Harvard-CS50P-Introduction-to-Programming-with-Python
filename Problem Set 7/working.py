# importing libraries
import re as r

# function to input hours
def main():
    print(convert(input("Hours: ")))

# converting input time
def convert(s):
    reg = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    m = r.search(r"^" + reg + " to " + reg + "$", s)
    if m:
        f_time = standard(m.group(1), m.group(2), m.group(3))
        time = standard(m.group(4), m.group(5), m.group(6))
        return f"{f_time} to {time}"
    else:
        raise ValueError

# standardising time in hrs, min and meridian
def standard(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"

# calling main function
if __name__ == "__main__":
    main()
