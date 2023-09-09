from MISW_EXP_1_CALIFICACION import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from random import random

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaCalificacion(Resource):

    def get(self):
        operand_1 = int(request.args.get("operand_1"))
        operand_2 = int(request.args.get("operand_2"))
        query_result = int(request.args.get("query_result"))

        prob_falla = 0.05

        resultado = operand_1 + operand_2 == query_result

        if random() < (1 - prob_falla):
            return {'correct_answer': resultado}, 200
        else:
            return {'correct_answer': not resultado}, 200

api.add_resource(VistaCalificacion, '/calificar')