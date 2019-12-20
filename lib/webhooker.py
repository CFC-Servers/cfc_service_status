import json
import requests

class Webhooker():
    def __init__(self, url):
        self.url = url

    def alert_down(self, service, activity_line):
        data = {
            "service": service,
            "activity_line": activity_line
        }

        requests.post(self.url, data=json.dumps(data))
