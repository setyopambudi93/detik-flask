from flask import Flask, jsonify , render_template
from main import scraper

app = Flask(__name__)


@app.route("/api")
def api():
    source = scraper()
    return jsonify('item', source)


@app.route('/')
def helo():
    source = scraper()
    return render_template('index.html', data_list = source)


if __name__ == '__main__':
    app.run(debug=True)
