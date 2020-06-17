from flask import Flask, request, render_template, redirect, session
from oauth import Oauth
from info import files

global avatars
global ids
avatars = {}
ids = {}

app = Flask(__name__)

@app.route("/", methods = ["get"])
def index():
    return redirect(Oauth.discord_login_url)
@app.route("/bots", methods = ["get"])
def bots():
    #avatars = files.get_avatars()
    #ids = files.get_ids()
    code = request.args.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    username = user_json.get("username")
    user_hash = user_json.get("discriminator")
    email = user_json.get("email")
    user_id = user_json.get("id")
    avatar_hash = user_json.get("avatar")
    server_json = Oauth.join_support(access_token, user_id)
    avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png"
    name = f"{username}#{user_hash}"
    return redirect('https://sorkopiko.github.io')


if(__name__ == "__main__"):
    app.run(debug=True)
