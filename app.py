from flask import Flask, render_template, request as req, jsonify
from werkzeug.utils import secure_filename
import os
from kidney_diagnosis  import  check_kidney_stone, check_cdk
from flask_cors import CORS, cross_origin
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def home():
    if req.method == 'POST':
        file = req.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        print(check_kidney_stone(img))
        return render_template('index.html', img=img)
    return render_template('index.html')
'''
def testCDK():
    handtest = [50.00,70.00, 1.01, 1.00, 0.00, 1.00,1.00, 0.00,  0.00, 219.00, 176.00 , 13.80, 136.00, 4.50,  8.60, 24.00, 13200.00, 2.70,1.00, 0.00, 0.00,0.00, 1.00,1.00]
    r = check_cdk(handtest)
    print(bool(r))
'''


@app.route('/api/check_ckd', methods=['POST'])
@cross_origin()
def ckd_checker():
    data = req.json
    #print(data.get('data'))
    result = check_cdk(data.get('data'))
    #print("Has CDK?", result)
    return jsonify({ 'cdk_prediction': bool(result)})
                    


@app.route('/api/check_kidney_stone', methods=['POST'])
@cross_origin()
def kidney_stone():
    file = req.files['img']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD'], filename))
    img = os.path.join(app.config['UPLOAD'], filename)
    prediction = check_kidney_stone(img)
    print(prediction)
    os.remove(img)
    return  jsonify({'prediction': prediction})

 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 80)), threaded=True, debug=True)
       

