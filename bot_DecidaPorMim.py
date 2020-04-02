from random import randint
import telepot
import sys
import time
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space

class Player(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.lucky = randint(0,1)
        self._answer = ['faça!','não faça!']
    
    def open(self, initial_msg, seed):
        self.sender.sendMessage('O que você deseja fazer?')
        return True
    
    def on_chat_message(self, msg):
        self.sender.sendMessage(self._answer[self.lucky])
        self.sender.sendMessage("Caso tenha outra duvida, faça a pergunta após 10 segundos.")

    def on__idle(self, event):
        self.sender.sendMessage('Pode fazer-me outra pergunta' % self._answer)
        self.close()

TOKEN = '1271922467:AAEWLw4j3_OsaZUIJs2BRoq0RMnsgBu8bGU'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Player, timeout = 10),
])

MessageLoop(bot).run_as_thread()
print('listening ...')

while 1:
    time.sleep(10)