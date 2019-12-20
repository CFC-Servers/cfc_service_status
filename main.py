import os
from lib.systemd_checker import SystemdChecker

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    services = os.getenv("MONITORED_SERVICES").split(",")

    checker = SystemdChecker(services)
    checker.check_services()
