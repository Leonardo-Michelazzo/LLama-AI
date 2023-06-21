import flask
import json

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

# @app.route('/api/choose/<id>')
# def choose(id):
#     json_data: dict[str, list[int]] = json.load(open('data.json'))


if __name__ == '__main__':
    app.run(debug=True)