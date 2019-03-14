$(document).ready(function(){
    // 登陆
    $(".icon-digg").mouseenter(function () {
        $(this).css("background-position","0 0")
    });

    $(".icon-digg").mouseleave(function () {
        $(this).css("background-position","0 -40px")
    });

    $(".discus-a span").mouseenter(function () {
        $(this).css("background-position","0 -60px")
    });

    $(".discus-a span").mouseleave(function () {
        $(this).css("background-position","0 -100px")
    });

    //点赞
    for (var i = 0; i < $('.likes').length; i++) {
        var ran = Math.floor(Math.random() * 1000 + 1)
        $('.likes').eq(i).text(ran)
    }
    $(".digg-a span").click(function () {
        var num = $(this).next().text()
        num++;
        $(this).next().text(num);
    });

    $(".login-btn-a").click(function () {
        $(".module-login-mask").show()
    })

    $("#close_cli").click(function () {
        $(".module-login-mask").hide()
    });

    $("#pub_id").click(function () {
        $("#digg-dialog-publish").show()
        $(".module-pub-mask").show()

    })

    $("#dialog-btn-close").click(function () {
        $("#digg-dialog-publish").hide()
        $(".module-pub-mask").hide()

    });


    //评论
    $("#due1").click(function () {
        if ($("#comment-box-area-25076146").css("display")=="none") {
            $("#comment-box-area-25076146").show()
        } else {
            $("#comment-box-area-25076146").hide()
        }
    })

    $(".close-comt,.hiddenCom-Btn").click(function () {
        $("#comment-box-area-25076146").hide()
    })

    $("#due2").click(function () {
        if ($("#comment-box-area-25076147").css("display")=="none") {
            $("#comment-box-area-25076147").show()
        } else {
            $("#comment-box-area-25076147").hide()
        }
    })

    $(".close-comt,.hiddenCom-Btn").click(function () {
        $("#comment-box-area-25076147").hide()
    })

    $("#pub-btn-top-25076146").click(function () {
        let vall = $("#txt-huifu-top-25076146").val()
        let bool = vall.length
        let count = $("#count1").html()
        if (bool){
            let new_p = '<li class="items"><span class="folder" style="background: none;"><div class="comment-L comment-L-top"><div class="pp"><a class="name" href="#">游客 </a><span class="p3"><span class="text-comment-con">'+vall+'</span></span></div></div></span></li>'
            $("#comment-list-top-25076146").append(new_p)
            $("#count1").html(parseInt(count)+1)
            $("#txt-huifu-top-25076146").val("")
        }
        else{
            alert("评论内容不能为空")
        }
    })

    $("#pub-btn-top-25076147").click(function () {
        let vall = $("#txt-huifu-top-25076147").val()
        let bool = vall.length
        let count = $("#count2").html()
        if (bool){
            let new_p = '<li class="items"><span class="folder" style="background: none;"><div class="comment-L comment-L-top"><div class="pp"><a class="name" href="#">游客 </a><span class="p3"><span class="text-comment-con">'+vall+'</span></span></div></div></span></li>'
            $("#comment-list-top-25076147").append(new_p)
            $("#count2").html(parseInt(count)+1)
            $("#txt-huifu-top-25076147").val("")
        }
        else{
            alert("评论内容不能为空")
        }
    })

//    发布新文章
    $("#pub-btn1").click(function () {
        let countt = $(".content-list").children().length
        let num = parseInt(countt) + 1
        let vall2 = $("#txt-duanzi").val()
        let bool2 = vall2.length
        if (bool2){
            let new_i = '<div class="item" id="i'+num+'"><div class="new-content"><div class="part1"><a href="#" class="show-content color-chag">'+vall2+'</a><span class="content-source">-***.com</span><a href="#" class="n2"><span class="conten-kind">42区</span></a></div><div class="part2"><a href="javascript:;" title="推荐" class="digg-a"><span class="hand-icon icon-digg" id="rec"></span><b>0</b></a><a href="javascript:;" class="discus-a"  id="due'+ num + '"><span class="hand-icon icon-discus"></span><b id="count'+num+'">0</b></a><a href="javascript:;" class="collect-a" title="加入私藏"><span class="hand-icon icon-collect"></span><b>私藏</b></a><a href="javascript:;" class="user-a"><b>游客</b></a><span class="left time-into"><a href="#" class="time-a"><b>1分钟前</b></a><i>入热榜</i></span></div><div class="comment-box-area" id="coa'+num+'" style="display: none;"><div class="pinglun arrow" id="comt'+num+'" style="left: 62.75px;"></div><a class="pinglun close-comt" title="关闭" href="javascript:;" lang="25076146"></a><div class="corner comment-box" id="comm'+num+'"><ul class="filetree comment-list-top-2 treeview" id="comment-l'+num+'"style="background: none;"></ul><div class="huifu-top-box" id="huifu-tb'+num+'" style="display: block;"><div class="box-l txt-input-area-div-top corner no-corner-bottom"><div id="lab-c'+num+'" class="lab-comment-top" style="display: none;">回复 <spanid="nic'+num+'"></span>:</div><textarea maxlength="150" name="txt-huifu-top" id="txt-huifu'+num+'"class="txt-huifu txt-huifu-top"style="text-indent: 0px; height: 20px; resize: none;"></textarea></div><div class="box-r"><a id="pub-btn-top'+num+'" lang="25076146" href="javascript:;"class="pub-icons add-pub-btn add-pub-btn-unvalid">评论</a></div></div><div class="tip-3" id="hidden-comt'+num+'" style="display: block;"><a href="javascript:;" class="hiddenCom-Btn" lang="25076146"><emlass="pinglun em2"></em><span>收起</span></a></div><div class="write-error-box-top"><div class="write-error-desc" id="write-error-desc'+num+'" style="display: none;"></div></div></div></div></div></div>'
            $(".content-list").append(new_i)
            $("#digg-dialog-publish").hide()
            $(".module-pub-mask").hide()
            $("#txt-duanzi").val("")
        }
        else{
            alert("评论内容不能为空")
        }
    })

//    发布页面的清除键功能
    $(".pub-clear-btn").click(function () {
        $("#txt-duanzi").val("")
    })
});