from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    content = request.json
    # print(content['lat'])
    markers = [
        {
            'lat': content['lat'],
            'lon': content['lon'],
            'popup': 'This is the middle of the map.'
        }
    ]
    return render_template('index.html', markers=markers)


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
