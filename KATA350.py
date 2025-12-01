#kata
#https://www.codewars.com/kata/586a1af1c66d18ad81000134/train/python

import datetime

def driver(data):
    forename, middle, surname, dob, gender = data
    surname_code = surname[:5].upper().ljust(5, '9')
    for fmt in ("%d-%b-%Y", "%d-%B-%Y"):
            try:
                dob_obj = datetime.datetime.strptime(dob, fmt)
                break
            except ValueError:
                continue
    year = dob_obj.year
    month = dob_obj.month
    day = dob_obj.day

    decade_digit = str(year)[2]
    month_code = month + (50 if gender.upper() == "F" else 0)
    month_code = f"{month_code:02d}"
    day_code = f"{day:02d}"
    year_digit = str(year)[3]
    initials = forename[0].upper()
    initials += middle[0].upper() if middle else "9"
    arbitrary_digit = "9"
    check_digits = "AA"
    license_number = (
        surname_code +
        decade_digit +
        month_code +
        day_code +
        year_digit +
        initials +
        arbitrary_digit +
        check_digits
    )
    return license_number.upper()



