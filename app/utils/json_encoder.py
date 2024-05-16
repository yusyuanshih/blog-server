import json
from collections import OrderedDict
from datetime import datetime

import flask
from flask_sqlalchemy.model import Model


class JSONEncoder(json.JSONEncoder):

    def default(self, o):

        def recursive(p):
            result = OrderedDict()
            for k in p.keys():
                result[k] = getattr(o, k)

                if isinstance(result[k], dict):
                    result[k] = recursive(result[k])
                if isinstance(result[k], datetime):
                    result[k] = result[k].timestamp()

            return result

        if isinstance(o, Model):
            return dict(recursive(o.__mapper__.c))

        return flask.json.JSONEncoder.default(self, o)
