from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

barcode_data = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    global barcode_data
    data = request.json
    barcode = data.get('barcode', '')
    if barcode == 'enter':
        response = barcode_data
        barcode_data = ""
        return jsonify({'barcode': response})
    else:
        barcode_data += barcode
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(debug=True)