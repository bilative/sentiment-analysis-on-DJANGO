from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import pandas as pd

from libs.helpy import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getInfo():
    message = "This is REST API part of my weekend project!!"

    return jsonify({"message" : message}), 200


@app.route('/predict', methods=['POST'])
def postIdentity():

    try:
        data = request.get_json()

        clean_one = preprocess_text(data['comment'])
        new = pd.DataFrame({
            'comment' : [clean_one]
            })
            
        new["sentiment_label"] = "-"
        new[["sentiment_label", "sentiment_score"]] = sentiment_analysis(new['comment'][0])

        return jsonify({"sentiment": new['sentiment_label'][0]}), 200
    except Exception as e:
        print(f"""
        
        {e}
        
        """)
        return jsonify('There is a problem')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)