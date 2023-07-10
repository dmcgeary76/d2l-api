import os, requests
from requests_oauthlib import OAuth2Session
from django.shortcuts import render


# Important for OAuth config
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create your views here.
def index(request):
    context = {}
    get_token()
    return render(request, 'auto/index.html', context)

#Store a few variables to test API connection
app_name = 'apitesttool'
client_id = '370b8ba9-a004-4950-aa27-8af6b8ef25e5'
client_secret = 'yoxhApjjthpOZMq9vOW2hsc4WKsXpK5wArqaCrFYcsE'
scope = 'core:*:*'
auth_url = 'https://auth.brightspace.com/oauth2/auth'
redirect_uri = 'https://d2l-api-ef3d222f3fa5.herokuapp.com/'
grant_type = 'client_credentials'

curl_text = 'https://auth.brightspace.com/oauth2/auth?client_id=370b8ba9-a004-4950-aa27-8af6b8ef25e5&client_sceret=yoxhApjjthpOZMq9vOW2hsc4WKsXpK5wArqaCrFYcsE&scope=core:*:*&redirect_uri=https://localhost:8000&grant_type=client_credentials&response_type=code'

def get_token():
    # Create the OAuth object
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    
    # Get the auth url and state
    authorization_url, state = oauth.authorization_url("https://auth.brightspace.com/oauth2/auth")
    print(authorization_url)
    
    response = requests.post(authorization_url)
    print(response)
    
    authorization_code = 'ac.us-east-1.czelmLbPSmoq2xnzZDm56Ot8kLxW080uuYa7ty5qFNU&state=CrqqcTFCI3JKk3WDtZwzUyX0AOvflK'
    
    token = oauth.fetch_token(
        "https://auth.brightspace.com/core/connect/token",
        authorization_response=authorization_code,
        client_secret = client_secret
    )
    
