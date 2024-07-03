import schedule
import time
from datetime import datetime

def task_to_run():
    print("Executing task...")
    # Aquí pones el código que quieres ejecutar a las 4:00 AM
    # Por ejemplo:
    print("Task executed at:", datetime.now())

def schedule_task():
    schedule.every().day.at("11:03").do(task_to_run)
    print("Task scheduled to run at 11:03 AM")

    while True:
        schedule.run_pending()
        time.sleep(1)  # Espera 1 segundo entre verificaciones

if __name__ == "__main__":
    schedule_task()