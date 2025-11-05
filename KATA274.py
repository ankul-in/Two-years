#kata
#https://www.codewars.com/kata/6707688c0f597511f6649270/train/python

def was_package_received_yesterday(tz_from, tz_to, start, duration):
    utc_send_time = start - tz_from
    utc_receive_time = utc_send_time + duration
    local_receive_time = utc_receive_time + tz_to
    return local_receive_time < 0
        
print(was_package_received_yesterday(7, 1, 5, 6))