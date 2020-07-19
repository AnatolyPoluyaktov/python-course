from datetime import datetime
import  time
class counttime:
    def __init__(self):
        self.start = datetime.now()
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start)
        return True
time.sleep(10)
with counttime():
    time.sleep(10)
