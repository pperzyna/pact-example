#!/usr/local/bin/python

import os

from user import UserClient

def main():
  API_PROVIDER_URL=os.getenv('API_USER_HOST', 'http://localhost:5000')

  user = UserClient(API_PROVIDER_URL)

  print("The user with ID 1 is:", user.get_user(1)['name'])
  
main()