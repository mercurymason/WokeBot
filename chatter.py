#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
#import os
#
#bot = ChatBot('Bot')
#bot.set_trainer(ListTrainer)
#
#for files in os.listdir("english/"):
#    data = open("english/" + files, "r").readlines()
#    bot.train(data)
#
#while True:
#    message = input("You:")
#    if message.strip() != "Bye":
#        reply = bot.get_response(message)
#        print("ChatBot:", reply)
#    if message.strip() == "Bye":
#        print("ChatBot:", "Bye")
#        break

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import copy

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

with open("cut.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
data = []

convo = []
for l in content:
    if "--" == l[:2]:
        convo.append(l[2:])
    elif "-" == l[:1]:
        convo.append(l[1:])
    elif "*" == l[:1]:
        convo.reverse()
        data.append(copy.deepcopy(convo))
        convo = []

length = len(data)
count = 0
for info in data:
    print(count / length * 100, f"%")
    bot.train(info)
    count += 1

while True:
    message = input("You:")
    if message.strip() != "Bye":
        reply = bot.get_response(message)
        print("ChatBot:", reply)
    if message.strip() == "Bye":
        print("ChatBot:", "Bye")
        break
