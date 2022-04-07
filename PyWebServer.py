from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "박주형의 비밀저장소!"

if __name__ == "__main__":
    app.run(host='10.100.111.195', port=5005)
    
