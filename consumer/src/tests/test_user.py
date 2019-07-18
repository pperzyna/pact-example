import pytest, atexit

from pactman import Consumer, Provider, Like
from ..user import UserClient

@pytest.fixture(scope="module")
def pact():
  pact = Consumer('Consumer').has_pact_with(Provider('Provider'), host_name='localhost', port=1234, pact_dir='/usr/src/app/pact')
  pact.start_service()
  atexit.register(pact.stop_service)
  return pact

@pytest.fixture
def client():
  return UserClient(
    'http://{host}:{port}'
    .format(host='localhost', port='1234')
  )

def test_get_user(pact, client):
  expected = {
    'id': 123,
    'name': 'Test User'
  }

  (pact
    .given('User with id 3 exists')
    .upon_receiving('a request for existing user')
    .with_request('get', '/user/3')
    .will_respond_with(200, body=Like(expected)))
  
  with pact:
    result = client.get_user(3)

  assert result == expected

def test_get_non_existing_user(pact, client):
  (pact
    .given('User with id 1 does not exist')
    .upon_receiving('a request for non existing user')
    .with_request('get', '/user/1')
    .will_respond_with(404))
  
  with pact:
    result = client.get_user(1)

  assert result is None