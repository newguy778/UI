import requests
import time

URL = "http://127.0.0.1:8000"


def get_data():
    resp = requests.get(f"{URL}/fake")
    # resp.close()
    return resp.text


start = time.perf_counter()
for i in range(500):
    print(get_data())
end = time.perf_counter()


print(f"Total Time = {(end - start)}")
