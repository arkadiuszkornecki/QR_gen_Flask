from flask import Flask, render_template, request, url_for
import base64
import io
import qrcode
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://google.com/"
    if request.method == 'GET':
        return render_template('qr_gen.html')
    else:
        if 'url' in request.form:
            url = request.form['url']

        qr_code = qrcode.make(url)
        buffer = io.BytesIO()
        qr_code.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")

        return render_template('qr_gen.html', url=url, qr_code=qr_base64)



if __name__ == '__main__':
    app.run()
