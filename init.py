from flask import Flask
from flask import request
from flask_cors import CORS
from gensim.summarization.summarizer import summarize
from newspaper import Article

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/", methods=['GET'])
def home():
    url = 'https://techcrunch.com/2021/03/16/patsnap-300-million-fundraise/'
    news = Article(url, language='ko')
    news.download()
    news.parse()
    return summarize(news.text)


@app.route('/', methods=['POST'])
def api_message():
    text = request.data.strip().decode('utf-8')
    return summarize(text, ratio=0.1)


if __name__ == '__main__':
    app.run()
