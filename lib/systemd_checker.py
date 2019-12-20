import threading

from subprocess import Popen, PIPE
from lib.webhooker import Webhooker
from lib.systemd_status_parser import SystemdStatusParser

class SystemdChecker():
    def __init__(self, services, webhooker):
        self.services = services
        self.webhooker = webhooker

    def check_service(self, service):
        command = "systemctl status {}".format(service).split()
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        status_info = SystemdStatusParser(stdout).get_status_from_output()

        if status_info["status"] != "active":
            self.webhooker.alert_down(service, status_info["activity_line"])

    def check_services(self):
        [self.check_service(service) for service in self.services]
