from flask import Flask, jsonify, request, Blueprint

from . import calculation

api = Blueprint("api" , __name__)

@api.get("/")
def index():
    return jsonify({"column": "value"}), 201

@api.post("/detect")
def detction():
    return calculation.detection(request)