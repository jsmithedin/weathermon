import argparse

from Adafruit_IO import Client, Feed

ADAFRUIT_IO_USERNAME = 'jsmithedin'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("secret", help="Secret")
    args = parser.parse_args()

    aio = Client(ADAFRUIT_IO_USERNAME, args.secret)

    temperature_feed = aio.feeds('temperature')
    humidity_feed = aio.feeds('humidity')
    pressure_feed = aio.feeds('pressure')

    aio.send(temperature_feed.key, str(25.0))
    aio.send(humidity_feed.key, str(10.0))
    aio.send(pressure_feed.key, str(50.0))


if __name__ == '__main__':
    main()


