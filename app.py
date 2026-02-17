from ast import Return
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from textblob.en import sentiment
import os 

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "") if data else ""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment_text = "Positive"
        color = "green"
        emoji = "👍"
    elif polarity < 0:
        sentiment_text = "Negative"
        color = "red"
        emoji = "👎"
    else:
        sentiment_text = "Neutral"
        color = "yellow"
        emoji = "😐"
    return jsonify({"sentiment": sentiment_text, "color": color, "emoji": emoji})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2000))
    app.run(host="0.0.0.0", debug=True, port=port)
