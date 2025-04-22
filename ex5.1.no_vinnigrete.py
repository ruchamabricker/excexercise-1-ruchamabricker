import datetime
import random

def get_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def generate_random_date(start, end):
    delta_days = (end - start).days
    random_days = random.randint(0, delta_days)
    return start + datetime.timedelta(days=random_days)

def main():
    print("Enter two dates in the format YYYY-MM-DD:")
    date1 = get_date("First date: ")
    date2 = get_date("Second date: ")

    start_date = min(date1, date2)
    end_date = max(date1, date2)

    random_date = generate_random_date(start_date, end_date)
    print("Random date generated:", random_date)

    if random_date.weekday() == 0:  # Monday is 0
        print("I have no vinaigrette!")

if __name__ == "__main__":
    main()