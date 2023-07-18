# importing the requests library
import json

import requests

URL = "<>"
KEY = "<>"  # TODO: do not
auth_header = {"x-api-key": KEY}


def get_raiders(static):
    qparams = {"static_name": static}
    r = requests.get(URL + "get_raiders", headers=auth_header, params=qparams)
    return r.json()


def get_builds(static, raider):
    qparams = {"static_name": static, "raider": raider}
    r = requests.get(URL + "get_builds", headers=auth_header, params=qparams)
    return r.json()


def get_wing(wing):
    qparams = {"wing": wing}
    r = requests.get(URL + "get_wing", headers=auth_header, params=qparams)
    return r.json()