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
import urllib
import urllib2
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
		self.reqHeader = Chatwork.TOKEN_HEADER_KEY + self.apiToken
		self.getRooms()


	"""
	ルーム一覧取得
	"""
	def getRooms(self):
		uri = "https://api.chatwork.com/v1/rooms"
		req = urllib2.Request(uri)
		req.add_header(Chatwork.TOKEN_HEADER_KEY, self.apiToken)
		res = urllib2.urlopen(req)
		ret = res.read()		
		ret = json.loads(ret)
		
		self.rooms = {}
		for item in ret:
			self.rooms[item["name"].encode('utf-8')] = item["room_id"]	
			


	"""
	ルームＩＤを取得
	 - roomName: ルーム名
	 - roomNameが存在しない場合はfalseを返す
	"""
	def getRoomID(self, roomName):
		return self.rooms[roomName] if self.rooms.has_key(roomName) else False


	"""
	ルームＩＤを指定してメッセージを送る
	 - roomId: ルームID
	 - msg: メッセージ
	"""
	def sendMessage(self, roomId, msg):
		uri = "https://api.chatwork.com/v1/rooms/" + str(roomId) + "/messages"
		params = {"body": msg}
		params = urllib.urlencode(params)

		req = urllib2.Request(uri)
		req.add_header(Chatwork.TOKEN_HEADER_KEY, self.apiToken)
		req.add_data(params)
		res = urllib2.urlopen(req)
		ret = res.read()
		return json.loads(ret)

