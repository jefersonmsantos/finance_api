import logging
import pandas as pd
from io import BytesIO

from flask import Flask, request, json, send_file

def create_app(name):
    app = Flask(name)
    app.logger.setLevel(logging.INFO)

    @app.route('/', methods = ['GET','POST'])
    def index():
        return ({'body':'Finance API'},200)
    
    @app.route('/lineage/cloudfunction', methods = ['POST'])
    def test_dataset():
        data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
        df = pd.DataFrame.from_dict(data)

        response_stream = BytesIO(df.to_csv(index=False).encode())
        return send_file(
            response_stream,
            mimetype="text/csv",
            download_name="export.csv",
        )

    return app