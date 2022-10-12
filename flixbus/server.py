import json
from flask import request, Flask, jsonify

app = Flask(__name__)
app.queue = []

@app.route('/')
def root():
    """[{"timestamp":16516818, "msg": "askdask-asd-as-dsa-dsa"}]"""
    msg = request.get_json()

    x = app.queue.append(msg)

    if len(x) >= 10:
        while len(x) > 0:
            current = x.pop(x)
            print(current)

    return {"message": "ok"}


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=65432,
        debug=True,
        # ssl_context=("cert.pem", "key.pem")
    )
