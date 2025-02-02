from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime     import datetime
from libs import my_functions 

#@respond_to('string')  bot宛のメッセージ
#                       sringは正規表現が可能[r'string']
#@listen_to('string')    チャンネル内のbot宛以外の投稿
#                       @botname: では反応しないことに注意
#                       他の人へのメンションでは反応する
#                       正規表現可能
# @default_reply()      DEFAULT_REPLY と同じ働き
#                       正規表現を指定すると,他のデコーダにヒットせず、
#                       正規表現にマッチするときに反応
#                       ・・・なのだが、正規表現を指定するとエラーになる?

# message.reply('string')       @発言者名：　string でメッセージを送信
# message.send('string')        string を送信
#message.react('icon_emoji')    発言者のメッセージにリアクションする
#                               文字列中に':'はいらない

@respond_to('メンション')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ') #メンション

@listen_to('何時')
@listen_to('なんじ')
def time_func(message):
    message.send('大体'+datetime.now().strftime("%H:%M"))