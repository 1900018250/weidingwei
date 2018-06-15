$(function () {
    const openid = mdm.getOpenid(), // 用户的openid
          $itemList = $('.item-list'),  // item-list容器
          $refresh = $('.right'),   // 右上角刷新按钮
          $addItemBt = $('.add-item-bt'),   // 添加item按钮
          $addBox = $('.add-item'),  // 添加item的弹出box
          $mask = $('.mask');   // 弹出的遮挡层

    // 点击刷新itemlist 和 绑定跳转Item详情页面和删除item事件 进页面触发一次
    $refresh.on('tap', () => {
        $itemList.html('');   //  每次先置空itemlist
        // 发起获取itemList请求 
        mdm.ajaxIf(openid, () => {
            getItemList(openid, (data) => {
                // 渲染数据
                if(data.status != 'success') return false;
                $itemList.append(template('item', {itemList: data.data}));

                bindDel2Details();
            })
        })
    }).trigger('tap');

    // 点击添加按钮 弹出添加界面
    $addItemBt.on('tap', () => {
        $addBox.show();
        $mask.show().on('tap', () => {   // 点击task关闭
            $addBox.hide();
            $mask.hide();
        });
    })

    // 表单提交处理 添加item
    $addBox.on('submit', 'form', function (e) {
        let data = mdm.parseFormValue($(this).serialize());
        // 添加item请求
        addItem(data, () => {   //成功的回调函数
            $addBox.hide();
            $mask.hide();
            this.reset();   // 重置表单
            swal({icon: "success", text: '添加成功'});
            $refresh.trigger('tap');    // 刷新item-list
        }, (data) => {  // 失败的回调函数
            $addBox.hide();
            $mask.hide();
            swal({icon: "error", text: mdm.parseError(data)});
        });
        return false;
    }).on('tap', 'button[type=button]', () => {   // 点击返回隐藏弹出层
        $addBox.hide();
        $mask.hide();
    })

    // 绑定删除item 和 跳转 item请求事件
    const bindDel2Details = () => {
        // 必须渲染完成的时候绑定 
        // 不然无法保持这样的父子关系就不能阻止冒泡事件
        $('.item-list').off('tap', 'li').on('tap', 'li', function(e) {    // 点击item跳转
            window.location.href = `/m/itemdetails/${openid}?itemid=${$(this).data('itemid')}`;
        });

        $('.item-list li').off('tap', 'i').on('tap', 'i', function(e) { // 删除item
            e.stopPropagation();
            // 确认是否删除
            swal({
                title: "你确定要删除吗？",
                text: "删除后无法找回,相关定位结果也会失去",
                icon: "warning",
                buttons: true,
                dangerMode: true,
                }) .then((willDelete) => {
                if (willDelete) {
                    delItem(openid, $(this).parent().data('itemid'), (data) => {
                        $refresh.trigger('tap');
                    }, (data) => {
                        // TODO
                    })
                }
            });            
        });

    };


    // 获取itemlist数据 
    function getItemList (openid, successCallback) { // *successCallback渲染数据的回调函数
        $.ajax({
            url: '/api/itemlist/',
            type: 'get',
            data: {
                openid: openid
            },
            dataType: 'json',
            success: (data) => {
                successCallback && successCallback(data);
            },
            error: () => {
                //TODO
            }
        })
    }

    // 发起添加定位Item的请求
    function addItem (data, successCallback, errorCallback) {
        $.ajax({
            url: '/api/itemlist/',
            type: 'post',
            data: {
                openid: openid,
                title: data.title,
                name: data.name,
                link: data.link,
                details: data.details
            },
            dataType: 'json',
            success: (data) => {
                if (!data.status == 'success') return
                successCallback && successCallback();
            },
            error: (data) => {
                data = JSON.parse(data.response)
                if (!(data.status == 'error' && data.error == 1000)) return
                errorCallback && errorCallback(data.data);
            }
        })
    }

    // 删除item请求
    function delItem (openid, itemid, successCallback, errorCallback) {
        $.ajax({
            url: '/api/item/',
            type: 'delete',
            data: {
                openid: openid,
                itemid: itemid
            },
            dataType: 'json',
            success: (data) => {
                if (!data.status == 'success') return
                successCallback && successCallback();
            },
            error: (data) => {
                // TODO
            }
        })
    }

 })