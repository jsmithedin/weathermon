import time
import argparse

import requests

URL = 'https://corlysis.com:8087/write'
DB = 'Weather'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="Secret Token")
    args = parser.parse_args()

    corlysis_params = {"db": DB, "u": "token", "p": args.token, "precision": "ms"}

    payload = ""

    unix_time_ms = int(time.time()*1000)
    line = "sensor_data temperature={},pressure={},humidity={} {}`n".format(5, 6, 7, unix_time_ms)

    payload += line

    try:
        r = requests.post(URL, params=corlysis_params, data=payload)
        if r.status_code != 204:
            print(r.status_code)
            raise Exception(r.text)
    except:
        print("Couldn't write to influx")


if __name__ == "__main__":
    main()
