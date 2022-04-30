from flask_restful import Resource

class PracticeApiController(Resource):
    def __init__(self):
        pass

    def get(self):
        return "hello!"