function clear() {
    localStorage.clear();
}

function $(id) {
    return document.getElementById(id);
}

window.onload = function () {
    let data = loaddata();
    console.log(data);
    console.log(data.length);
    if (data.length > 0) {

        add_todolist(data);
    }
};


//表单action触发的函数
/*先判断input值
    值为空：弹窗提示
    值不为空：
        1.加入事件到 "todolist" ul中 count_id +1
        2.保存数据到 Local Storage
*/
function postaction() {
    let title = $("title");
    if (title.value === "") {
        alert("内容不能为空！") ;   //因为input已经设置了required值，此处应该没有多大意义
    }else{
        let data = loaddata();
        let todo = { "title": title.value, "done": false };
        data.push(todo);
        savedata(data);
        let form = $("form");
        form.reset();
        update_data(todo, data);
    }
}

//加入事件到 "todolist" ul中
function add_todolist(data) {
    let todolist = document.getElementById("todolist");
    let donelist = document.getElementById("donelist");

    for (let i = 0; i < data.length; i++) {
        flag = data[i].done;
        todo_str = "<li draggable='true'>" +
            "<input type='checkbox' onchange='transfer(" + i + ",\"done\"," + flag + "'"+
            "<p id='p-" + i + "'>" + data[i].title + "</p>";
        if(flag === true) {
            todolist.innerHTML += todo_str;
            todolist_count("add");
        }else{
            donelist.innerHTML += todo_str;
            donelist_count("add")
        }
    }
}
// ul的计数器操作
function todolist_count(mod) {
    if (mod === 'add') {
        let count = parseInt($("todocount").innerText) + 1;     //先把span的字符串值改成int类型
        $("todocount").innerHTML = count;
    }
}

function donelist_count(mod) {
    if (mod === 'add') {
        let count = parseInt($("donecount").innerText) + 1;     //先把span的字符串值改成int类型
        $("donecount").innerHTML = count;
    }
}

//获取Local Storage的数据
function loaddata() {
    let mod_data = localStorage.getItem("todo");
    if (mod_data != null) {
        return JSON.parse(mod_data)
    } else return [];
}
//保存数据到 Local Storage
function savedata(data) {
    localStorage.setItem("todo", JSON.stringify(data));
}

function update_data(mode, data) {
    let todolist = document.getElementById("todolist");

    let i = data.length;


    todo_str = "<li draggable='true'>" +
        "<input type='checkbox' onchange='transfer(" + i + ",\"done\",true)'/>"+
        "<p id='p-" + i + "'>" + mode.title + "</p>";

    todolist.innerHTML += todo_str;
    todolist_count("add");
    // savedata(data);

}

//点击li里面的input框之后， todolist的li转移到donelist



function transfer(i, field, value) {
    let data = loaddata();
    let todo = data.splice(i, 1)[0];
    todo[field] = value;
    data.splice(i, 0, todo);
    savedata(data);
}