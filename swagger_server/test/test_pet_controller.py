# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPetController(BaseTestCase):
    """PetController integration test stubs"""

    def test_create_pet(self):
        """Test case for create_pet

        Create a pet
        """
        body = Pet()
        response = self.client.open(
            '/v1/pet',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
