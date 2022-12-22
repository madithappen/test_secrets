import request

def login():
    """ Fake example of using a password in source code to assess GitHub secrets scanning """
    secret = "password123"
    data = { 'password': secret }
    headers = {'Content-Type': 'application/json'}
    url = 'https://fake.example.local'
    session = requests.post(url, json=data, headers=headers)
    return session
