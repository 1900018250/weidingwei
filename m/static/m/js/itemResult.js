$(function () {
    const openid = mdm.getOpenid(),   
          itemid = mdm.getParamsByUrl().itemid, // Item的id
          $title = $('h2'), // item的标题
          $refresh = $('.right'),   // 右上角刷新按钮
          $back = $('.wdw-header>.left'),   // 返回按钮
          $resultList = $('.result-list');  // result-list列表


    // 点击刷新resultList 进页面触发一次
    $refresh.on('tap', () => {
        $resultList.html('');   //  每次先置空resultList
        // 发起获取resultList请求   
        getResultList(openid, itemid, (data) => {  
            $resultList.append(template('result', {resultList: data.data}));
        });
    }).trigger('tap');

    // 返回上一页
    $back.on('tap', () => window.history.go(-1))

    // 绑定跳转定位结果详情页面
    $resultList.off('tap', 'li').on('tap', 'li', function(e) {    // 点击item跳转
        window.location.href = `/m/resultdetails/${openid}?itemid=${itemid}&resultid=${$(this).data('resultid')}`;
    });
          
    // 获取itemlist数据 
    function getResultList (openid, itemid, successCallback) {
        $.ajax({
            url: '/api/resultlist/',
            type: 'get',
            data: {
                openid: openid,
                itemid: itemid
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

})