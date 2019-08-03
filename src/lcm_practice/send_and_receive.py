import multiprocessing

import select
import time

import lcm

from .test_message import test_message


def sender():
    counter = 0
    while True:
        message = test_message()
        message.utime = counter
        counter += 1
        message.speed = 0.1 * counter
        message.direction = 'forward'

        _lcm = lcm.LCM()
        _lcm.publish("TEST_MESSAGE", message.encode())
        print("\nSent test_message")
        time.sleep(2)


def listener(channel, data):
    message = test_message.decode(data)
    print(f"\nReceived test_message on {channel}")
    print(f"    {message.utime}")
    print(f"    {message.speed}")
    print(f"    {message.direction}")


if __name__ == '__main__':
    sender_process = multiprocessing.Process(target=sender)
    sender_process.start()

    _lcm = lcm.LCM()
    _lcm.subscribe("TEST_MESSAGE", listener)

    timeout = 2
    while True:
        try:
            rfds, wfds, efds = select.select([_lcm.fileno()], [], [], timeout)
            if rfds:
                _lcm.handle()
            else:
                print("\nWaiting...")
        except KeyboardInterrupt:
            break
