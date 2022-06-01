from flask import Flask, render_template
import threading
import time
import mapgenerator

app = Flask(__name__)


def thread_function():
    events = ['#earthquake', '#forestfire', '#storm']
    while True:
        print("Generating map...")
        mapgenerator.generate_map(events)
        print("Done")
        time.sleep(120)


@app.route("/")
def main():
    return render_template("map.html")


if __name__ == "__main__":
    thread_1 = threading.Thread(target=thread_function)
    thread_1.start()
    app.run(host="0.0.0.0")
