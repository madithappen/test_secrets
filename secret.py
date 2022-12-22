import request

def login():
    """ Fake example of using a password in source code to assess GitHub secrets scanning """
    secret = "password123"
    data = { 'password': secret }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    session = requests.POST("https://#" data={"password": secret})
    return session
