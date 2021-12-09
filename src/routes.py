from flask_restx import Resource
from flask import request, send_file

from .functions.steganography import encode, decode


class Encrypt(Resource):
    def post(self):
        data = request.get_json()
        img = data.get("image")
        msg = data.get("message")

        if not img:
            return {"error": "missing image"}, 400

        if not msg:
            return {"error": "missing message"}, 400

        encrypted_image = encode(img, msg)

        return {"encrypted_image": str(encrypted_image)}, 200


class Decrypt(Resource):
    def post(self):
        img = request.json.get("image")

        if not img:
            return {"error": "missing image"}, 400

        try:
            msg = decode(img)
        except:
            return {"error": "image does not contain secret message"}, 400

        return {"message": msg}, 200
