from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from gensim.summarization.summarizer import summarize

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def home():
    return jsonify(
        status=200,
        message="Hello, Text Rank!"
    )


@app.route('/', methods=['POST'])
def api_message():
    text = request.data.strip().decode('utf-8')
    return jsonify(
        status=200,
        message=summarize(text, ratio=0.1)
    )


if __name__ == '__main__':
    app.run()
