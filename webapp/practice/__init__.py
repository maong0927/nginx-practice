from flask import Blueprint
from flask_restful import Api
from .controller import PracticeApiController

practice_api_blueprint = Blueprint('practice_api', __name__, url_prefix='/')
practice_api = Api(practice_api_blueprint)
practice_api.add_resource(PracticeApiController, '/practice')