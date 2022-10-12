import json
import random
import socket
import time
import uuid

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
NUM_MESSAGES = 3

if __name__ == "__main__":
    msgs = []
    for _ in range(NUM_MESSAGES):
        msgs.append(
            {
                "timestamp": int(time.time()) + random.randint(1, 10),
                "msg": str(uuid.uuid4()),
            }
        )

    msg_str = json.dumps(msgs)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(msg_str, encoding="utf-8"))