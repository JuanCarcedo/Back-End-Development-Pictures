from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))


######################################################################
# RETURN HEALTH OF THE APP
######################################################################
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200


######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################
@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures() -> tuple:
    """
    Retrieve the full list of pictures/data.
    :return: tuple
        list of json: data
        http status code 200 if found -- Code: OK
    """
    response: tuple = data, 200

    return response


######################################################################
# GET A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id: int) -> tuple:
    """
    Retrieve picture from the data using id.
    If the id does not exist, return error code and message.
    :param id: id of the picture for searching.
    :return: tuple
        dict: data (json) or message (json) if not found.
        http status code:
            200 Found                   -- Code: OK
            404 Not found/invalid id    -- Code: Not Found
    """
    search_result: dict = find_data(id)

    if search_result:
        response: tuple = search_result.get('data'), 200

    else:
        response: tuple = {"message": "Not a valid ID"}, 404

    return response


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture() -> tuple:
    """
    Create a new picture.
    Step 1) Check if picture exists, if it does, then return error message and http 302
    Step 2) Only if 1 is False. Create new picture.
    :return: tuple
        dict: data for new picture (json) or message (json) if duplicated.
        http status code:
            201 Picture added           -- Code: Created
            302 Picture already exists  -- Code: Found
    """
    new_picture_data = request.json

    # Check if the picture exists
    if find_data(new_picture_data.get("id")):
        response: tuple = {"Message": f"picture with id {new_picture_data.get('id')} already present"
                           }, 302

    else:
        data.append(new_picture_data)
        response: tuple = new_picture_data, 201

    return response


######################################################################
# UPDATE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id: int) -> tuple:
    """
    Update a picture currently in the data.
    :return: tuple
        dict: data for new picture (json) or message (json) if not found.
        http status code:
            200 Picture updated    -- Code: OK
            404 Picture not found  -- Code: Not Found
    """
    new_picture_data = request.json

    # Check if the picture exists and gather data
    search_result = find_data(id) if (new_picture_data and id) else {}

    if search_result:
        response: tuple = new_picture_data, 200
        # Update picture's data
        data[search_result.get('index')] = new_picture_data

    else:
        response: tuple = {"message": "picture not found"}, 404

    return response


######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id: int) -> tuple:
    """
    Delete a picture if it is in the data.
    :return: tuple
        dict: empty body or message (json) if not found.
        http status code:
            204 Picture deleted    -- Code: No content
            404 Picture not found  -- Code: Not Found
    """
    # Check if the picture exists and gather data
    search_result = find_data(id) if id else {}

    if search_result:
        response: tuple = {}, 204
        # Remove picture's data
        data.remove(search_result.get('data'))

    else:
        response: tuple = {"message": "picture not found"}, 404

    return response


######################################################################
# JCA Additional code -- support actions
def find_data(id_to_search: int = -99) -> dict:

    data_to_return: dict = {}

    if id_to_search != -99 and data:
        # Search through the data based on id
        for index in range(0, len(data)):
            if data[index].get('id') == id_to_search:
                data_to_return = {'data': data[index],
                                  'index': index}
                # Found, end loop
                break

    return data_to_return
