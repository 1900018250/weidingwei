$(function() {
    const openid = mdm.getOpenid(),   
          itemid = mdm.getParamsByUrl().itemid, // Item的id
          resultid = mdm.getParamsByUrl().resultid,  // resultid定位结果id
          $back = $('.wdw-header>.left');   // 返回按钮

    // 返回上一页
    $back.on('tap', () => window.history.go(-1))

    // 渲染结果页面
    ;(($) => {
       $.ajax({
           url: '/api/result/',
           type: 'get',
           data: {
               openid: openid,
               itemid: itemid,
               resultid: resultid
           },
           dataType: 'json',
           success: (data) => {
                $('.map-details p:eq(0)').find('span').html(data.data.add_time);
                $('.map-details p:eq(1)').find('span').html(data.data.address);
                $('.map-details p:eq(2)').find('span').html(data.data.lng + '  ' + data.data.lat);
                $('.map-details p:eq(3)').find('span').html(data.data.ip);
                // 显示地图
                var map = new AMap.Map('container', {
                    resizeEnable: true,
                    zoom:15,
                    center: [data.data.lng, data.data.lat]
                });
           },
           error: () => {
               // TODO
           }
       }) 
    })($);
 })