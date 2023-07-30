from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days_ahead)

def convert_date(date):
    return datetime.strftime(date, DATE_FORMAT)

def get_weeks(start, end):
    nearestSunday = next_weekday(start, 6)
    if nearestSunday >= end:
        return [f"{convert_date(start)} {convert_date(end)}"]

    datesList = [f"{convert_date(start)} {convert_date(nearestSunday)}"]
    currDate = nearestSunday + timedelta(days=1)
    while currDate + timedelta(days=7) <= end:
        datesList.append(f"{convert_date(currDate)} {convert_date(currDate + timedelta(days=7))}")
        currDate += timedelta(days=7)
    else:
        datesList.append(f"{convert_date(currDate + timedelta(days=1))} {convert_date(end)}")

    return datesList

def get_months(start, end):
    nxt_mnth = start.replace(day=28) + timedelta(days=4)
    nearestLastDay = nxt_mnth - timedelta(days=nxt_mnth.day)

    if nearestLastDay >= end:
        return [f"{convert_date(start)} {convert_date(end)}"]
    
    datesList = [f"{convert_date(start)} {convert_date(nearestLastDay)}"]
    currDate = nearestLastDay + timedelta(days=1)
    while currDate.replace(day=28) + timedelta(days=4) - timedelta(days=nxt_mnth.day) <= end:
        nxt_mnth = currDate.replace(day=28) + timedelta(days=4)
        endMonth = nxt_mnth - timedelta(days=nxt_mnth.day)
        datesList.append(f"{convert_date(currDate)} {convert_date(endMonth)}")
        currDate = nxt_mnth - timedelta(days=nxt_mnth.day - 1)
    else:
        datesList.append(f"{convert_date(currDate)} {convert_date(end)}")

    return datesList


with open("input.txt", 'r') as readFile:
    code = readFile.readline()[:-1]
    dates = readFile.readline().split()
    start = datetime.strptime(dates[0], DATE_FORMAT)
    end = datetime.strptime(dates[1], DATE_FORMAT)
    result = []
    if code == "MONTH":
        result = get_months(start, end)
    if code == "WEEK":
        result = get_weeks(start, end)
    with open("output.txt", 'w') as writeFile:
        writeFile.write(f"{len(result)}\n")
        for i in result:
            writeFile.write(f"{i}\n")
