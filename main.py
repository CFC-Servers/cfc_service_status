import os
from lib.systemd_checker import SystemdChecker
from lib.webhooker import Webhooker

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    services = os.getenv("MONITORED_SERVICES").split(",")
    url = os.getenv("WEBHOOKER_URL")

    webhooker = Webhooker(url)

    checker = SystemdChecker(services, webhooker)
    checker.check_services()
