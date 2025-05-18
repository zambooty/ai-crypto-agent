from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Hello from the Trading Bot Web App!")

@app.route('/build-bot')
def build_bot_page():
    return render_template('build_bot.html', message="Configure your bot") # You can pass specific messages or data if needed

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 