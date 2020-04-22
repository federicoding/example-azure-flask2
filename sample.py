from flask import Flask
app = Flask(__name__)

@app.route("/sample")
def running():
    return 'FLask is running Bro!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
