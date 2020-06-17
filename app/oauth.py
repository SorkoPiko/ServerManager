import requests

class Oauth(object):
    client_id = "699422804294238248"
    client_secret = "4uZJZYiOkPdt_NMbcq97gSVHoDDy4ZAm"
    scope = "identify%20email%20guilds%20guilds.join%20gdm.join%20connections%20rpc%20rpc.notifications.read%20applications.builds.read%20applications.store.update%20applications.entitlements%20messages.read"
    redirect_uri = "http://127.0.0.1:5000/bots"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
    discord_token_url = 'https://discord.com/api/oauth2/token'
    discord_api_url = "https://discord.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            'client_id':Oauth.client_id,
            'client_secret':Oauth.client_secret,
            'grant_type':"authorization_code",
            'code':code,
            'redirect_uri':Oauth.redirect_uri,
            'scope':Oauth.scope
        }

        headers = {
    	    'Content-Type': 'application/x-www-form-urlencoded'
  	}

        access_token = requests.post(url=Oauth.discord_token_url, data=payload, headers=headers)
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authorization": f"Bearer {access_token}"        
        }
        user_object = requests.get(url=url, headers=headers)
        user_json = user_object.json()
        return user_json

    @staticmethod
    def join_support(access_token, user_id):
        url = Oauth.discord_api_url+f"/guilds/709943998948704338/members/{user_id}"
        
        headers = {
            "Authorization": "Njk5NDIyODA0Mjk0MjM4MjQ4.XuVsjQ.0HkpNMg8mPnvUCDYwfYeh8i4wyY",
            "access_token": access_token,
            "nick": "Auto-Join"
        }
        user_put = requests.put(url=url, headers=headers)
        user_put_json = user_put.json()
        return user_put_json