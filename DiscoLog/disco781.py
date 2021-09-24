import requests
from login12 import login
class message:
	def __init__(ps, id, message, token4,channel_id):
			ps.id = id
			ps.message = message
			ps.token4 = token4
			ps.channel_id = channel_id
	def message_resp(ps):
		list_id = []
		r = requests.get(f"https://discord.com/api/v9/channels/{ps.channel_id}/messages?limit=1", headers = {"Authorization" : ps.token4})
		if r.json()[0]["author"]["id"] != ps.id:
			re = requests.post(f"https://discord.com/api/v9/channels/{ps.channel_id}/messages?limit=1", headers = {"Authorization" : ps.token4}, data = {"content" : ps.message})
		else:
			return r.json()

					
