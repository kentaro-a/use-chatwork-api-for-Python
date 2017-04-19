# -*- coding: utf-8 -*-
"""
 * Chatwork API
 * @source: http://developer.chatwork.com/ja/
 * ex)
	cw = Chatwork("your apiToken")
	roomid = cw.getRoomID("マイチャット")
	if roomid:
        	cw.sendMessage(roomid, "テスト\nてすと")

"""
import requests
import json

class Chatwork: 

	# リクエストヘッダーのキー
	TOKEN_HEADER_KEY = "X-ChatWorkToken"

	"""
	イニシャライズ
	 - apiToken: APIトークン
	"""
	def __init__(self, apiToken):
		self.apiToken = apiToken
		self.reqHeader = {Chatwork.TOKEN_HEADER_KEY: self.apiToken}
		self.getRooms()


	"""
	ルーム一覧取得
	"""
	def getRooms(self):
		uri = "https://api.chatwork.com/v2/rooms"
		req = requests.get(uri, headers=self.reqHeader)
		ret = json.loads(req.text)
		self.rooms = {}
		for item in ret:
			self.rooms[item["name"]] = item["room_id"]	
			


	"""
	ルームＩＤを取得
	 - roomName: ルーム名
	 - roomNameが存在しない場合はfalseを返す
	"""
	def getRoomID(self, roomName):
		return self.rooms[roomName] if roomName in self.rooms else False


	"""
	ルームＩＤを指定してメッセージを送る
	 - roomId: ルームID
	 - msg: メッセージ
	"""
	def sendMessage(self, roomId, msg):
		uri = "https://api.chatwork.com/v2/rooms/" + str(roomId) + "/messages"
		data = {"body": msg}
		req = requests.post(uri, headers=self.reqHeader, data=data)
		return json.loads(req.text)

