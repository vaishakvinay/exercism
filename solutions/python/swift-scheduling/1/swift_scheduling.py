from datetime import datetime, timedelta


def delivery_date(start, description):
    
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")

 

    if description == "NOW":
        result = start + timedelta(hours=2)

    elif description == "ASAP":
        if start.hour < 13:
            result = start.replace(hour=17, minute=0, second=0, microsecond=0)
        else:
            tomorrow = start + timedelta(days=1)
            result = tomorrow.replace(hour=13, minute=0, second=0, microsecond=0)

    elif description == "EOW":
        weekday = start.weekday()  # Monday=0 ... Sunday=6

        if weekday <= 2:  # Monday, Tuesday, Wednesday
            days_to_add = 4 - weekday  # Friday = 4
            result = start + timedelta(days=days_to_add)
            result = result.replace(hour=17, minute=0, second=0, microsecond=0)
        else:  # Thursday or Friday
            days_to_add = 6 - weekday  # Sunday = 6
            result = start + timedelta(days=days_to_add)
            result = result.replace(hour=20, minute=0, second=0, microsecond=0)

   

    elif description.endswith("M"):
        month = int(description[:-1])

        if start.month < month:
            year = start.year
        else:
            year = start.year + 1

        result = datetime(year, month, 1, 8, 0)

       
        while result.weekday() >= 5:  # Saturday=5, Sunday=6
            result += timedelta(days=1)

   

    elif description.startswith("Q"):
        quarter = int(description[1:])
        last_month = quarter * 3

        meeting_quarter = (start.month - 1) // 3 + 1

        if meeting_quarter <= quarter:
            year = start.year
        else:
            year = start.year + 1

        
        if last_month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, last_month + 1, 1)

        
        result = next_month - timedelta(days=1)

        
        result = result.replace(hour=8, minute=0, second=0, microsecond=0)

        
        while result.weekday() >= 5:
            result -= timedelta(days=1)

    return result.strftime("%Y-%m-%dT%H:%M:%S")