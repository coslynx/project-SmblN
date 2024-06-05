from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']
        payload = {'content': message}
        webhook_url = 'YOUR_DISCORD_WEBHOOK_URL_HERE'
        requests.post(webhook_url, json=payload)
        return 'Message sent successfully!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)