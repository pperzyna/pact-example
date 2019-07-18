import pytest

from flask import json
from ..app import app

def test_get_users():        
    response = app.test_client().get(
        '/user',
        content_type='application/json',
    )

    assert response.status_code == 200

def test_get_user():        
    response = app.test_client().get(
        '/user/1',
        content_type='application/json',
    )

    assert response.status_code == 200

def test_add_user():        
    response = app.test_client().post(
        '/user',
        data=json.dumps({'name': 'Test'}),
        content_type='application/json',
    )

    assert response.status_code == 201

def test_del_user():        
    response = app.test_client().delete(
        '/user/1',
        content_type='application/json',
    )

    assert response.status_code == 200
