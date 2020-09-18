#!/usr/bin/env python3

import redis
import os
import time

# step 1: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def refresh_heartbeat():
    """Example Hello Redis Program"""

    # step 2: create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        stream = os.popen('date +%s')
        output = stream.read()

        # step 3: Set the heartbeat in Redis
        r.set("heartbeat", output.strip("\n"))

        # step 5: Retrieve the hello message from Redis
        msg = r.get("heartbeat")
        print(msg)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    while True:
        refresh_heartbeat()
        time.sleep(10)
