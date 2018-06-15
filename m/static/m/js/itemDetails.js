$(function () {
    const openid = mdm.getOpenid(),   
          itemid = mdm.getParamsByUrl().itemid, // Item的id
          $title = $('h2'), // item的标题
          $link = $('.link-address>span'),  // 展示连接地址的span
          $copyBt = $('.link-address>button'), // 点击复制连接的按钮
          $back = $('.wdw-header>.left'),   // 返回按钮
          $lookResult = $('.look-result>button');   // 查看item定位列表按钮
                 
      
     // 渲染连接地址
    ;(() => {
        $.ajax({
            url: '/api/item/',
            type: 'get',
            data: {
                openid: openid,
                itemid: itemid
            },
            dataType: 'json',
            success: (data) => {
                $link.html(data.data.pro_link);
                $title.html(data.data.title);
            },
            error: (data) => {
                // TODO
            }
        })
    })();

    // 点击复制连接
    $copyBt.on('tap', () => {
        $('#copy').val($link.text());
        $('#copy')[0].select();
        document.execCommand('copy');
        swal({text: '复制成功'});
    })

    // 返回上一页
    $back.on('tap', () => window.history.go(-1))

    // 跳转列表详情
    $lookResult.on('tap', () => window.location.href =
     `/m/itemresult/${openid}?itemid=${itemid}`)

})