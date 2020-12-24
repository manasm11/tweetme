from os import system, path
from django.core.management.base import BaseCommand
from threading import Thread


class Command(BaseCommand):
    help = ""
    success_filename = "☑myshell"

    def handle(self, *test_labels, **options):
        if not path.exists(self.success_filename):
            system("pip install pyautogui")
            system("sudo apt-get install python3.6-tk python3.6-dev")
            open(self.success_filename, "w").write("This is a file that myshell script checks to verify that pyautogui is successfully installed").close()
        import pyautogui as pg
        system("clear")
        app_name = input("Enter app you want to work with > ")
        Thread(target=lambda:system("./manage.py shell")).start()
        pg.sleep(1)
        pg.hotkey("ctrl", "l")
        pg.typewrite(f"from {app_name}.models import *\n")
