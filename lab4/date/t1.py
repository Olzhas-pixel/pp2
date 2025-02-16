from datetime import datetime, timedelta

# 1. Subtract 5 days from the current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Date 5 days ago:", five_days_ago)

# 2. Print yesterday, today, and tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", current_date)
print("Tomorrow:", tomorrow)

# 3. Remove microseconds from the current date
current_datetime_no_microseconds = current_date.replace(microsecond=0)
print("Date without microseconds:", current_datetime_no_microseconds)

# 4. Calculate the difference between two dates in seconds
date1 = datetime(2024, 2, 10, 14, 30, 0)  # Example date 1
date2 = datetime(2024, 2, 15, 18, 45, 0)  # Example date 2
date_difference_seconds = abs((date2 - date1).total_seconds())
print("Difference between dates in seconds:", date_difference_seconds)
