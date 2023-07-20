from datetime import date, timedelta
import inflect
import sys


def main():
    print(minsCalculator(input("Date of Birth: ")))

def minsCalculator(s):
    try:
        #get the day user's born in particular format
        bornDay = date.fromisoformat(s)

        #get today's day
        today = date.today()

        if bornDay < today:
            #caculate the days between these two dates
            totalMin = (today - bornDay)/timedelta(minutes = 1)

            #transform mins to word format
            p = inflect.engine()
            words = p.number_to_words(int(totalMin), andword="").capitalize()

            return (f"{words} minutes")

        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid date")






if __name__ == "__main__":
    main()
