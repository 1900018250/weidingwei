import werobot

from werobot.replies import ArticlesReply, Article
robot = werobot.WeRoBot(token='tokenhere')

@robot.handler
def hello(message):
    # 发送者的openid
    print(message.source)
    return 'Hello World!'


@robot.key_click("enter")
def articles(message):
    return [
        [
            "title",
            "description",
            "img",
            "url"
        ],
        [
            "登录首页",
            "https://www.baidu.com/img/bd_logo1.png?where=super",
            "https://www.baidu.com/img/bd_logo1.png?where=super",
            'http://wdw.summeroo.club/m/index/{0}'.format(message.source)
        ]
    ]


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '127.0.0.1'
robot.config['PORT'] = 8080
robot.config["APP_ID"] = "wx309ada1f5dd6c40f"
robot.config["APP_SECRET"] = "2bd0bed85e618e3070687079e4093232"
client = robot.client


def sendMessage():
    client.send_template_message('o2Rmf0eiF3ytDihgfdLYo3ZYFfuE', 'IJim1sZqgw8cVJbejmahz-uWJ-v_d6T0Lt6bH4Qt75M', {
        "first": {
            "value":"定位成功点击查看！",
            "color":"#173177"
        },
        "keyword1":{
            "value":"精准定位",
            "color":"#173177"
        },
        "keyword2": {
            "value":"2018-1-1",
            "color":"#173177"
        },
        "remark":{
            "value":"点击查看详情哦",
            "color":"#173177"
        }
    }, 'www.baidu.com')

    # url = '127.0.0.1/{0}'.format(message.source)
    # return url


# client.create_menu({
#     "button": [
#         {
#             "type": "click",
#             "name": "进入定位",
#             "key": "enter"
#         },
#         {
#             "type": "click",
#             "name": "帮助信息",
#             "key": "help"
#         }]
# })
# robot.run()