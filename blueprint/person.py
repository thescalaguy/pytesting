from flask import request
from playhouse.shortcuts import model_to_dict

import repository.person as pr
from blueprint import api
from dateutil.parser import parse


@api.route("/person", methods=["POST"])
def create_person():
    name = request.json["name"]
    dob = request.json["dob"]
    dob = parse(dob).date()

    person = pr.create(name, dob)
    return model_to_dict(person)
