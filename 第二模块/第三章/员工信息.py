#!-*- coding:utf-8 -*-
#__author__:"irving"

def load_db():
    '''
    当作读取数据库函数
    这里只有一个文件放用户数据，所以不加参数做文件判断了，操作全在此文件进行。
    :return:
    '''
    with open('staff_table', 'r', encoding='utf-8') as f:
        for i in f:
            tmp_list = i.split(',')
            tmp_list[-1] = tmp_list[-1].strip()
            STAFF_INFO.append(tmp_list)

def save_db():
    '''
    当作写入数据库函数
    :return:
    '''
    with open('staff_table', 'w', encoding='utf-8') as f:
        for i in STAFF_INFO:
            line = ','.join(i)
            f.write(line + '\n')
        f.flush()

# find name,age from staff_table where age > 22
# find * from staff_table where dept = "IT"
# find * from staff_table where enroll_date like "2013"
def _find():
    find_info = syntax_list[1].split(' ')
    print(syntax_list)
    find_index = find_info.index('find')      #找出find字符的索引，后面用来切片用
    from_index = find_info.index('from')      #找出from字符的索引，后面用来切片用
    where_index = find_info.index('where')    #找出where字符的索引，后面用来切片用
    tmp_return_keys = find_info[find_index+1: from_index]
    return_keys = tmp_return_keys[0].split(',')
    codition_keys = find_info[where_index+1:]
    print(codition_keys)
    if codition_keys[1] is '>':
        for i in STAFF_INFO:
            if i[COLUMN_NAME.index(codition_keys[0])] > codition_keys[2]:
                print(i[COLUMN_NAME.index(return_keys[0])], i[COLUMN_NAME.index(return_keys[1])])
    elif codition_keys[1] is '=':
        for i in STAFF_INFO:
            if i[COLUMN_NAME.index(codition_keys[0])] == codition_keys[2].strip('"'):
                print(i)
    elif codition_keys[1] == 'like':
        for i in STAFF_INFO:
            # print(i[COLUMN_NAME.index(codition_keys[0])], codition_keys[2].strip('"'))
            if codition_keys[2].strip('"') in i[COLUMN_NAME.index(codition_keys[0])]:
                print(i)



# add staff_table Alex Li,25,134435344,IT,2015-10-29
def _add():
    filename = syntax_list[0]
    add_list = syntax_list[1].split(' ', 1)
    # print(add_list)
    add_info = add_list[1]
    # print(add_info)
    new_user_info = add_info.split(',')
    new_user_info.insert(0, str(len(STAFF_INFO) + 1))
    print(new_user_info)
    exist_flag = True
    for i in STAFF_INFO:
        if new_user_info[-3] == i[COLUMN_NAME.index('phone')]:
            exist_flag = False
    if exist_flag == True:
        STAFF_INFO.append(new_user_info)
        print('\033[33;1m Add successfully! \033[0m')
        save_db()
    else:
        print('\033[31;1m phone number is already exist! \033[0m')





# del from staff where  id=3
def _del():
    del_info = syntax_list[1].split(' ')
    print(del_info)
    file_name = del_info[0]
    id_index = del_info[-1].split('=')[-1]
    print(id_index)
    for i in STAFF_INFO:
        if id_index == i[COLUMN_NAME.index('staff_id')]:
            STAFF_INFO.remove(i)
            print('\033[33;1m Delete successfully! \033[0m')
            save_db()



# UPDATE staff_table SET dept="Market" WHERE  dept = "IT"
# UPDATE staff_table SET age=25 WHERE  name = "Alex Li"
def _update():
    update_info = syntax_list[1].split(' ', 5)
    print(update_info)
    filename = update_info[0]
    after_value = update_info[2].split('=')
    before_value = update_info[-1].split('=')
    print(after_value, before_value)   # 带 ""
    print(before_value[1].strip(' ').strip('"'))
    for i in STAFF_INFO:
        if i[COLUMN_NAME.index(before_value[0].strip())] == before_value[1].strip(' ').strip('"'):
            i[COLUMN_NAME.index(after_value[0])] = after_value[1].strip('"')
    print('修改成功！')
    save_db()



if __name__ == '__main__':
    COLUMN_NAME = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    STAFF_INFO = []
    load_db()
    while True:
        syntax = input('>>:')
        syntax_list = syntax.split(' ', 1)
        keys = syntax_list[0]
        print(keys)
        if keys == 'find':
            _find()
        elif keys == 'del':
            _del()
        elif keys == 'UPDATE':
            _update()
        elif keys == 'add':
            _add()
        for i in STAFF_INFO:
            print(i)
