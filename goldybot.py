# General Code
from flask import Flask, request, redirect
from oauth import Oauth

app = Flask(__name__)


@app.route("/", methods = ["get"])
def index():
	return redirect(Oauth.discord_login_url)


@app.route("/login", methods = ["get"])
def login():
	code = request.args.get("code")
	at = Oauth.get_access_token(code)

	user_json = Oauth.get_user_json(at)
	username, usertag = user_json.get("username"), user_json.get("discriminator")

	return f"{username}#{usertag}"


if __name__ == "__main__":
	app.run(debug = True)


############Oauth2 Code############
import requests


class Oauth:
	client_id = "994209392566210560"
	client_secret = "-fds1xlNPThqD8OTHO9MZNYFD9RZKPwY"
	redirect_uri = "https://goldybot.gq"
	scope = "identify%20email"
	discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
	discord_token_url = "https://discord.com/api/oauth2/token"
	discord_api_url = "https://discord.com/api"


	@staticmethod
	def get_access_token(code):
		payload = {
			"client_id": Oauth.client_id,
			"client_secret": Oauth.client_secret,
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": Oauth.redirect_uri,
			"scope": Oauth.scope
		}

		access_token = requests.post(url = Oauth.discord_token_url, data = payload).json()
		return access_token.get("access_token")


	@staticmethod
	def get_user_json(access_token):
		url = f"{Oauth.discord_api_url}/users/@me"
		headers = {"Authorization": f"Bearer {access_token}"}

		user_object = requests.get(url = url, headers = headers).json()
		return user_object
