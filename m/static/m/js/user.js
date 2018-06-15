$(function() {
    const openid = mdm.getOpenid(), // 用户的openid
          $userEmail = $('input[name=email]'),
          $userPhone = $('input[name=phone]'),
          $isEmail = $('input[name=isemail]'),
          $isPhone = $('input[name=isphone]'),
          $userInfo = $('.user-info form'),
          $submit = $('#submit');
          
    let rgFlag = false; // 是否为注册行为的标志

    // 判断是否是注册行为， 如果不是取后台数据渲染form表单
    if (mdm.getParamsByUrl().register == 'true') {
        $submit.html('注册');
        rgFlag = true;
    } else {
        renderUserData();
    }

    // 表单提交处理
    $userInfo.on('submit', function (e) {
        e.preventDefault();
        let data = mdm.parseFormValue($(this).serialize());
        // 更新用户数据和添加用户
        if (!rgFlag) {
            updateUserInfo(data);
        } else {
            addUserInfo(data);
        }  
    })
    

    // 更新user数据函数
    const updateUserInfo = (data) => {
        ajaxUserInfo(data, () => {    // 更新成功回调
            swal({icon: "success", text: '更改成功'});
        }, (data) => {  // 更新失败回调
            console.log(data.error)
            if (data.error != 1000) {
                swal({icon: "error", text: 'openid不存在'});
                return
            } 
            swal({icon: "error", text: mdm.parseError(data.data)}); 
        });
    };

    // 添加user数据函数
    const addUserInfo = (data) => {
        ajaxUserInfo(data, () => {    // 添加成功回调
            swal({icon: "success", text: '注册成功'});
            setInterval(() => {
                window.location.href = '/m/index/' + openid;    // 跳转到此openid 的用户首页
            }, 1000);
        }, (data) => {  // 添加失败回调
            if (data.error != 1000) {
                swal({icon: "error", text: '此openid已存在'});
                return
            } 
            swal({icon: "error", text: mdm.parseError(data.data)}); 
        }, 'post');
    }


    // 渲染用户数据表单
    function renderUserData() {
        mdm.ajaxIf(mdm.getOpenid(), (data)=>{
            $userEmail.val(data.data.email);
            $userPhone.val(data.data.phone);
            $isEmail.prop('checked', data.data.is_email);
            $isPhone.prop('checked', data.data.is_phone);
        })
    }

    // 提交user数据
    function ajaxUserInfo(data, successCallback, errorCallback, type='put') {
        $.ajax({
            url: '/api/user/',
            type: type,
            data: {
                openid: openid,
                email: data.email,
                phone: data.phone,
                isEmail: data.isemail ? 1 : 0,
                isPhone: data.isphone ? 1 : 0
            },
            dataType: 'json',
            success: (data) => {
                if (!data.status == 'success') return
                successCallback && successCallback();
            },
            error: (data) => {
                data = JSON.parse(data.response)
                if (data.status != 'error') return
                errorCallback && errorCallback(data);
            }
        })
    }


})