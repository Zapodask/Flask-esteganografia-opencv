from flask_restx import Resource
from flask import request, send_file

from .functions.steganography import encode, decode


class Encrypt(Resource):
    def post(self):
        img = request.files.get("image")
        msg = request.form.get("message")

        if not img:
            return {"error": "missing image"}, 400

        if not msg:
            return {"error": "missing message"}, 400

        # image = encode(img, msg)
        # send_file(image, mimetype="image")
        return {"encrypt": msg}, 200


class Decrypt(Resource):
    def post(self):
        img = request.files.get("image")

        if not img:
            return {"error": "missing image"}, 400

        try:
            msg = decode(img)
        except:
            return {"error": "image does not contain secret message"}, 400

        return {"message": msg}, 200
