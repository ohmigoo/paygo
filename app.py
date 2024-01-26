from flask import Flask, render_template, send_file
import qrcode
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/qrcodes/'

@app.route('/generate_qr')
def generate_qr():
    data = "Your Payment Data"  # This should be dynamically fetched or generated
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Save QR code image to static folder
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'payment_qr.png')
    img.save(img_path)
    
    return send_file(img_path, mimetype='image/png')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
