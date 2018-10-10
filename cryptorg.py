import requests
import json
import time
import hashlib
import base64
import hmac

class Api():

	""" This is API for Cryptorg.net """

	apiKey = ''
	apiSecret = ''
	apiUrl = 'https://api.cryptorg.net/'

	""" Cryptorg api constructor """
	def __init__(self, apiKey, apiSecret):
		self.apiKey = apiKey
		self.apiSecret = apiSecret

	""" GetCryptorg.net current status """
	def status(self):
		return self.sendRequest('GET', 'api/status')

	""" Get list of user's bots """
	def botList(self):
		return self.sendRequest('GET', 'bot/all')

	""" Get bot details """
	def botInfo(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/info', query)

	""" Advanced create bot """
	def createBot(self, params, attributes):

		try:
			query = "pair=" + params['pair'] + "&exchange=" + params['exchange']
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('POST', 'bot/create', query, attributes)

	""" Create bot with preset """
	def createPreset(self, params, attributes):

		try:
			query = "pair=" + params['pair'] + "&exchange=" + params['exchange']
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('POST', 'bot/create-preset', query, attributes)

	""" Update bot settings """
	def updateBot(self, params, attributes):

		try:
			query = "pair=" + params['pair'] + "&botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('POST', 'bot/configure', query, attributes)

	""" Delete bot """
	def deleteBot(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/delete', query)

	""" Activate bot """
	def activateBot(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/activate', query)

	""" Deactivate bot """
	def deactivateBot(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/deactivate', query)

	""" Start bot force"""
	def startBotForce(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/start-force', query)

	""" Get bot logs """
	def getBotLogs(self, params):
		
		try:
			query = "botId=" + str(params['botId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'bot/logs', query)

	""" Freeze deal """
	def freezeDeal(self, params):
		
		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'deal/freeze', query)

	""" Freeze deal """
	def unFreezeDeal(self, params):
		
		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'deal/unfreeze', query)

	""" Update TakeProfit """
	def updateTakeProfit(self, params):
		
		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'deal/update-take-profit', query)

	""" Cancel deal """
	def cancelDeal(self, params):
		
		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'deal/cancel', query)

	""" Get deal info """
	def dealInfo(self, params):

		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'deal/info', query)

	""" Get analytics """
	def getAnalytics(self, params = ''):

		try:
			query = "dealId=" + str(params['dealId'])
			pass

		except Exception as e:
			return { 'status': 'ok', 'result': 'false', 'message': e}

		else:
			return self.sendRequest('GET', 'analytics/get', query)

	""" Send request to api.cryptorg.net """
	def sendRequest(self, method, url, query = '', params = ''):

		nonce = str(int(time.time()))

		authStr = url + '/' + nonce + '/' + query
		strForSign = base64.b64encode(authStr.encode('utf-8'))

		hash = hmac.new(self.apiSecret.encode('utf-8'), strForSign, hashlib.sha256).hexdigest()

		headers = {

			"CTG-API-SIGNATURE": str (hash), 
			"CTG-API-KEY": str (self.apiKey), 
			"CTG-API-NONCE": nonce
		}

		signUrl = self.apiUrl + url + '?' + query

		if (method == 'GET'):
			response = requests.get(url = signUrl, headers = headers).text

		if (method == 'POST'):
			response = requests.post(url = signUrl, headers = headers, json=params).text

		return json.dumps(json.loads(response), indent=4, sort_keys=True)
		