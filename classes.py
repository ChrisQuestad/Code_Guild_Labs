# Instance- Takes self as an argument, access to the instance properties.
# Static- Always do the same thing for every class
import time

class Utilities():
    @staticmethod
    def log_the_time():
        with open('log.txt', 'w') as f:
            f.write(time.strftime('%X', time.gmtime()))

Utilities.log_the_time()
