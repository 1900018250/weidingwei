window.mdm = {};   // 工具对象

// 替换模板的解析符
let rule = template.defaults.rules[0];
rule.test = new RegExp(rule.test.source.replace('<%', '<\\\?').replace('%>', '\\\?>')); 

// 让对象支持for of
function* objectEntries(obj) {
        let propKeys = Reflect.ownKeys(obj);
        for (let propKey of propKeys) {
                yield [propKey, obj[propKey]];
        }
}

// 底部footer链接跳转
$('.wdw-footer').on('tap', 'ul li', function () {
        window.location.href = `/m/${$(this).data('link')}/${mdm.getOpenid()}`;
})

// 解析地址的openid
mdm.getOpenid = () => {
        return window.location.pathname.split('/').pop();
}; 

// 得到地址栏上的参数
mdm.getParamsByUrl = () => {
        /*已对象存储地址栏信息*/
        var params = {};
        var search = location.search;
        if (search) {
                search = search.replace('?', '');
                /*如果有多个键值对*/
                var arr = search.split('&');
                arr.forEach(function (item, i) {
                var itemArr = item.split('=');
                params[itemArr[0]] = itemArr[1];
                });
        };
        return params;
};

// 解析表单提交的数据
mdm.parseFormValue = (formValue) => {
        let data = {}; 
        formValue.split('&').forEach((item, i) => {
                const temp = item.split('=');
                data[temp[0]] = decodeURIComponent(temp[1]);
        })
        return data;
}

// 查看后台是否有这个openid如果不存在转到注册
mdm.ajaxIf = (openid, callback) => {
        $.ajax({
                url: '/api/user/',
                type: 'get',
                data: {
                        openid: openid
                },
                dataType: 'json',
                success: (data) => {
                       callback && callback(data) 
                },
                error: (data) => {      // 失败跳转user 注册
                        window.location.href = '/m/user/' + mdm.getOpenid() + '?register=true'; 
                }
        })
};

// 解析后台返回的错误
mdm.parseError = (data) => {
        let errorText = '';
        for (let [key, value] of objectEntries(data)) {
                errorText += key + ': ' + value + '\n';
        }
        return errorText;
}