from flask import Flask
import json


class Response:
    def __init__(self, data):
        self.data = data

    def getResponse(self):
        return Flask.response_class(
            response=json.dumps(self.data),
            status=200,
            mimetype='application/json'
        )

    def postResponse(self):
        return Flask.response_class(
            response=json.dumps(self.data),
            status=201,
            mimetype='application/json'
        )
