import requests

class UserClient(object):
  def __init__(self, base_uri):
    self.base_uri = base_uri

  # Fetch a user object by user_id from the server
  def get_user(self, user_id):
    uri = self.base_uri + '/user/' + str(user_id)
    response = requests.get(uri)
    if response.status_code == 404:
      return None
    return response.json()