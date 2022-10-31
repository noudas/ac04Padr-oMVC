from flask import Flask, request, jsonify, make_response
import json

tasks = [
    {
        'id': 1,
        'name': "dalma",
        "description": "dalma esteve aqui"
    },
    {
        "id": 2,
        "name": "ines",
        "description": "ines esteve aqui"
    },
    {
        "id": 3,
        "name": "amanda",
        "description": "amanda esteve aqui"
    }
]

tasksJSON = json.dumps(tasks)

class Model():

    def jsonReturn():
        return tasksJSON

    def soma():
        return '10'
