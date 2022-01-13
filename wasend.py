import json
import requests

class WAsend():    
    def __init__(self):
        self.APIUrl = 'https://dev.wapp.im/v3/'
        self.token = '4sDQ0NRcbvJCtofU'

    def get_chatid(self):
        # немного не понял, как получить чат. 
        # в эту функцию надо записать получение ID чата
        pass #тут будет вывод ID инстанса

    #------------------------------------------------------------------#
    # Выполнение запросов

    def send_postrequests(self, method, data):
        ID = self.get_chatid()
        url = f"{self.APIUrl}instance{ID}/{method}?token={self.token}"
        headers = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_getrequests(self, method):
        #ID = self.get_chatid()
        #url = f"{self.APIUrl}instance{ID}/{method}?token={self.token}"
        url = f"{self.APIUrl}instance33/{method}?token={self.token}"
        headers = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
        answer = requests.get(url, headers=headers)
        return answer.json()

    #-------------------------------------------------------------------#
    # Функции получения и отправки информации

    def check_status(self):
        answer = self.send_getrequests('status')
        return answer

    def get_qrcode(self):
        answer = self.send_getrequests('qr_code')
        return answer

    def send_message(self, chatId, text):
        data = {"chatId" : chatId,
                "body" : text}
        answer = self.send_postrequests('sendMessage', data)
        return answer

    def del_chat(self, chatId):
        data = {"chatId" : chatId}
        answer = self.send_postrequests('removeChat', data)
        return answer




