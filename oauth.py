import requests

#Store a few variables to test API connection
app_name = 'apitesttool'
client_id = '370b8ba9-a004-4950-aa27-8af6b8ef25e5'
client_secret = 'yoxhApjjthpOZMq9vOW2hsc4WKsXpK5wArqaCrFYcsE'
scope = 'core:*:*'
auth_url = 'https://auth.brightspace.com/oauth2/auth'
redirect_uri = 'https://localhost:8000'
grant_type = 'client_credentials'

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    print(response)
    return response.json()["access_token"]

