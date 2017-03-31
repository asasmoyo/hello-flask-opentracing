import json
import os

import flask
import flask_zipkin
from py_zipkin import zipkin

import tracer

app = flask.Flask('example-app')
app.config['ZIPKIN_DSN'] = os.getenv('ZIPKIN_DSN')

_zipkin = flask_zipkin.Zipkin(sample_rate=100)
_zipkin.init_app(app)


@tracer.trace
@app.route('/')
def index():
    result = json.dumps({
        'result': compute(),
        'result2': 2
    })
    return result


def compute():
    with zipkin.zipkin_span(service_name='example-app', span_name='compute') as z:
        z.update_binary_annotations({'return': 10})
        return 10
