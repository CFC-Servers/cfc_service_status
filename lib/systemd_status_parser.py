class SystemdStatusParser():
    def __init__(self, output):
        self.output = output

    def get_status_from_output(self):
        output = self.output
        output = output.decode("utf-8")
        output = output.split("\n")

        # Active: active (running) since Wed 2019-12-18 19:58:50 EST; 1 day 8h ago
        # Active: failed (Result: signal) since Mon 2019-12-30 00:06:14 EST; 55min ago
        activity_line = output[2]

        # ['Active:', 'active', '(running)', 'since', 'Wed', '2019-12-18', '19:58:50', 'EST;', '1', 'day', '8h', 'ago']
        # ['Active:', 'failed', '(Result:', 'signal)', 'since', 'Mon', '2019-12-30', '00:06:14', 'EST;', '55min', 'ago']
        activity_line_spl = activity_line.split()

        # 'active'
        # 'failed'
        activity_status = activity_line_spl[1]

        # 3
        # 4
        since = activity_line_spl.index("since")

        # ['active', '(running)']
        # ['failed', '(Result:', 'signal)']
        activity_line = activity_line_spl[1:since]

        # 'active (running)'
        # 'failed (Result: signal)'
        activity_line = " ".join(activity_line)

        status = {
            "status": activity_status,
            "activity_line": activity_line
        }

        return status

        ## '(running)'
        #activity_status_info = activity_line_spl[2].strip("()")

        ## 'Wed 2019-12-18 19:58:50'
        #since = " ".join(activity_line_spl[4:7])

        #status = {
        #    "status": activity_status,
        #    "status_info": activity_status_info,
        #    "since": since
        #}

        #return status
