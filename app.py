from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Render a simple template
    return render_template('index.html')


if __name__ == '__main__':
    # Run only when executed directly
    app.run(host='127.0.0.1', port=5000)
