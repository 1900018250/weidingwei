接口文档

###用户信息
+ 接口名称： 获取用户信息
+ 接口地址： api/user/
+ 请求方式： get
+ 参数说明
    参数名称|是否必须|说明
    openid|是|微信的openid
+ 返回说明
    {
        "status": "success",
        "data": {
            "id": 1,
            "openid": "12345",
            "email": "1900@qq.com",
            "phone": "15870411",
            "is_email": false,
            "is_phone": false
        }
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "不存在此openid"
    }


+ 接口名称： 修改用户信息
+ 接口地址： api/user/
+ 请求方式： put
+ 参数说明
    参数名称|是否必须|说明
    openid|是|微信的openid
    email|是|邮箱
    phone|是|手机号码
    isEmail|是|是否开启邮箱提醒
    isPhone|是|是否开启短信提醒
+ 返回说明
    {
        "status": "success"
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "不存在此openid"
    }
    {
        "status": "error",
        "error": 1000,
        "data": {
            "isEmail": "这个字段是必填项。"
        }
    }



+ 接口名称  添加用户
+ 接口地址  api/user/
+ 请求方式  POST
    参数名称|是否必须|说明
    openid|是|微信的openid
    email|是|邮箱
    phone|是|手机号码
    isEmail|是|是否开启邮箱提醒
    isPhone|是|是否开启手机短信提醒
+ 返回说明
    {
        "status": "success"
    } 
    {
        "status": "error",
        "error": 1002,
        "msg": "此openid已存在"
    }
    {
        "status": "error",
        "error": 1000,
        "data": {
            "isEmail": "这个字段是必填项。"
        }
    }



### 定位item
+ 接口名称  获取用户的定位列表
+ 接口地址  api/itemlist/
+ 请求方式  GET
    参数名称|是否必须|说明
    openid|是|微信的openid
+ 返回说明
    {
        "status": "success",
        "data": [
            {
                "id": 3,
                "user_id": 1,
                "title": "",
                "name": "",
                "link": "",
                "details": "",
                "add_time": "2018-05-27 08:30:12",
                "update_time": null
            },
            .....
        ]
    }


+ 接口名称  用户添加定位item
+ 接口地址  api/itemlist/
+ 请求方式  POST
    参数名称|是否必须|说明
    openid|是|微信的openid
    title|是|定位的标题
    name|是|连接的名字
    link|是|连接地址
    details|是|连接说明
+ 返回说明
    {
        "status": "success"
    }
    {
        "status": "error",
        "error": 1000,
        "data": {
            "details": "这个字段是必填项。"
        }
    }


+ 接口名称  获取item详细信息
+ 接口地址  api/item/
+ 请求方式  GET
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
+ 返回说明
    {
        "status": "success",
        "data": {
            "id": 3,
            "user_id": 1,
            "title": "",
            "name": "",
            "link": "",
            "details": "",
            "add_time": "2018-05-27 08:30:12",
            "update_time": null
        }
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有数据"
    }


+ 接口名称  修改item详细信息
+ 接口地址  api/item/
+ 请求方式  PUT
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
    title|是|定位的标题
    name|是|连接的名字
    link|是|连接地址
    details|是|连接说明
+ 返回说明
    {
        "status": "success"
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有此条记录"
    }
    {
        "status": "error",
        "error": 1000,
        "data": {
            "itemid": "输入整数。",
            "details": "这个字段是必填项。"
        }
    }


+ 接口名称  删除item详细信息
+ 接口地址  api/item/
+ 请求方式  DELETE
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
+ 返回说明
    {
        "status": "success"
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有此条记录"
    }



### 定位结果result
+ 接口名称  获取openid下itemid下的定位结果result列表
+ 接口地址  api/resultlist/
+ 请求方式  GET
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
+ 返回说明
    {
        "status": "success",
        "data": [
            {
                "id": 7,
                "user_id": 1,
                "item_id": 6,
                "flag": false,
                "ip": "1",
                "lng": "123",
                "lat": "123",
                "address": "111",
                "add_time": "2018-05-27 11:35:09"
            },
          ......
        ]
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有数据"
    }


+ 接口名称  增加定位结果result
+ 接口地址  api/resultlist/
+ 请求方式  POST
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
    flag|是|定位是否成功 (0,1)
    ip|是|定位ip地址
    lng|是|定位经度
    lat|是|定位纬度
    address|是|定位地址
+ 返回说明
    {
        "status": "success"
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有此用户或定位"
    }
    {
        "status": "error",
        "error": 1000,
        "data": {
            "itemid": "输入整数。",
            "lat": "这个字段是必填项。"
        }
    }


+ 接口名称  获取openid下itemid下resultid的定位详细信息
+ 接口地址  api/resul/
+ 请求方式  POST
    参数名称|是否必须|说明
    openid|是|微信的openid
    itemid|是|定位item的id
    resultid|是|定位结果result的id
+ 返回说明
    {
        "status": "success",
        "data": {
            "id": 7,
            "user_id": 1,
            "item_id": 6,
            "flag": false,
            "ip": "1",
            "lng": "123",
            "lat": "123",
            "address": "111",
            "add_time": "2018-05-27 11:35:09"
        }
    }
    {
        "status": "error",
        "error": 1001,
        "msg": "没有此数据"
    }
