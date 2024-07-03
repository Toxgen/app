from flask import Flask, render_template
import pymongo
import dotenv as env
import os

app = Flask(__name__)
env.load_dotenv()

uri = os.getenv("mongoURI")
client = pymongo.MongoClient(uri)
db = client.first

db.friends.insert_one({"name": "me", "age": 2173, "country": "siberia"})
@app.route("/")
def hello_world():
    return render_template('base.html')

@app.route("/other")
def other():
    return render_template('other.html')

if __name__ == '__main__':
    try:
        print(client.server_info())
    except Exception as e:
        print(e)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)