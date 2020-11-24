import connexion
import mysql.connector
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server import util



def create_pet(body):  # noqa: E501
    if connexion.request.is_json:
        mydb = mysql.connector.connect(
            host="localhost",
            user="swagger_user",
            password="haslo123",
            database="swagger"
        )
        mycursor = mydb.cursor()

        query = "INSERT INTO pets (name, tag)\
            VALUES (%s, %s)"
        
        body = connexion.request.get_json()  # noqa: E501

        mycursor.execute(query, (body["name"], body["tag"]))

        mydb.commit()

    return connexion.request.get_json()
