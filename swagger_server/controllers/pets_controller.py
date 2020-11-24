import connexion
import six
import mysql.connector

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.pets import Pets  # noqa: E501
from swagger_server import util
import json



def _convert_to_json(description, query_results):
    headers=[x[0] for x in description]

    json_data=[]

    for result in query_results:
        json_data.append(dict(zip(headers, result)))

    return json_data



def create_pets():  # noqa: E501
    """Create a pet

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def list_pets(limit=None):  # noqa: E501
    mydb = mysql.connector.connect(
        host="localhost",
        user="swagger_user",
        password="haslo123",
        database="swagger"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM pets")

    result = json.dumps(_convert_to_json(
        mycursor.description, mycursor.fetchall()))

    print(result)

    return json.loads(result)


def show_pet_by_id(petId):  # noqa: E501
    mydb = mysql.connector.connect(
        host="localhost",
        user="swagger_user",
        password="haslo123",
        database="swagger"
    )
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM pets WHERE id ={petId}")

    result = json.dumps(_convert_to_json(
        mycursor.description, mycursor.fetchall()))

    print(type(result[0]), result[0])

    return json.loads(result)[0]
