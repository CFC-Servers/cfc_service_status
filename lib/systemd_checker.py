import threading
import subprocess

class SystemdChecker():
    def __init__(self, services):
        self.services = services

    def get_status_from_command(self, output):
        print(output)
        for l in output.split():
            print(l)
        print()

    def check_service(self, service):
        command = "systemctl status {}".format(service).split()
        output = subprocess.check_output(command)

        status = self.get_status_from_command(output)

    def check_services(self):
        [self.check_service(service) for service in self.services]
