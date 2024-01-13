from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    print("Index page loaded")
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    print(f"Received data: {data}")
    img = qrcode.make(data)
    img.save('static/qrcode.png')
    print("QR code generated successfully")
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)