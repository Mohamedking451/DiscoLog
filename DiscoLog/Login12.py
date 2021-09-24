import requests
class login(object):
	def __init__(pt, email, password, token1):
		pt.email = email
		pt.password = password
		re = requests.post("https://discord.com/api/v9/auth/login", json = {"email" : pt.email, "password" : pt.password})
		if "token" in re.json():
			pt.token1 = re.json()["token"]



			
		
