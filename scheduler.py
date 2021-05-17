import time
import schedule

from config import INFORMATION_TIME, USER_ID
from controller import EveryDayReporter

schedule.every().day.at(INFORMATION_TIME).do(EveryDayReporter.run, user_id=USER_ID)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
