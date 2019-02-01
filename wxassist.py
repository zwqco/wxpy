#！/usr/bin/env/python3
#-*-coding:utf-8-*-

from wxpy import *
import  time
import random

class WxAssist(object):
    picAuto =['小样表情玩的挺溜啊！！','这表情可以。。','你是只会发表情么','滚吧不和你玩了']
    def __init__(self,type):
        self.type = type
    def handle(self):
        if self.type == '1':
            self.replyTuling()
        elif self.type == '2':
            self.replyCustom()
        else:
            self.fireMsg()
    def replyTuling(self):
        bot = Bot(cache_path=True)
        tuling = Tuling(api_key='07ef72bfc54844b088a834c547948edd')
        print('小蛋机器人正在为您服务.....')
        friends = input('请输入自动回复的朋友：')
        fri = bot.friends().search(friends.decode())[0]
        @bot.register(fri,msg_types=TEXT)
        def reply(msg):
            print("%s"%(msg))
            ty = tuling.do_reply(msg)
            print("机器人回复:%s"%ty)
        @bot.register(fri,msg_types=PICTURE)
        def repImg(msg):
            print("%s" % (msg))
            ty = random.choice(self.picAuto)
            msg.reply(ty)
            print("机器人回复:%s"%ty)
        embed()

    def replyCustom(self):
        bot = Bot(cache_path=True)
        while True:
            reMsg = input('请设置您要自动回复的内容:')
            @bot.register(msg_types=TEXT)
            def reply(msg):
                msg.reply(u'%s' % reMsg)
            while True:
                cmd = input('已经开启自动回复功能，如需重新设置回复内容，请输入r')
                if cmd == 'r':
                    break
    def fireMsg(self):
        bot = Bot(cache_path=True)
        while True:
            name = input('请输入要轰炸人的微信名或者备注:')
            num = input('请输入要轰炸的次数:')
            msg = input('请输入要发送的内容:')
            fri = bot.friends().search(u'%s' % name)[0]
            print('轰炸系统准备完毕,开始发射。。')
            for i in range(1,int(num)):
                fri.send(u'%s'%msg)
                print('====》》成功发送%s次' % i)
                if i % 70 == 0:
                    time.sleep(10)
                    print('避免微信拦截轰炸等待5秒...')
            print('本次轰炸执行完毕！！！')

if __name__ == '__main__':
    print(" ----------------------------------------------------------------")
    print("|       ********* 欢迎使用微信Robot author:Co *********         |")
    print('|       ====== 首次登陆请扫描程序弹出的登陆二维码 ======        |')
    print(" ----------------------------------------------------------------")
    while True:
        type = input('请选择您要使用的功能[1 小蛋自动回复 2 自定义回复 3 微信消息轰炸]:')
        func = ['1', '2', '3']
        if not type.isdigit():
            print('您的输入有误，请重新输入!')
            continue
        if type not in func:
            print('您的输入有误，请检查后重新输入!')
            continue
        robot = WxAssist(type)
        robot.handle()
        break




