#kata100
#https://www.codewars.com/kata/68c31c23f0aee823d84cdd42
from datetime import datetime, timedelta
def set_the_alarms_up(time, n):
    wake_dt = datetime.strptime(time, "%H:%M")
    alarms = [(wake_dt + timedelta(minutes=5 * i)).strftime("%H:%M") for i in (range(n))]
    return alarms
print(set_the_alarms_up("07:00", 3))
