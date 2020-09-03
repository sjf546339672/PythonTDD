# coding: utf-8
"""
TODO: 1、PATCH和PUT方法的区别?
PUT实现的是全部的更新 PATCH是局部更新

假设我们有一个UserInfo，里面有userId， userName， userGender等10个字段
如果你用了put，但却没有提供完整的UserInfo，那么缺了的那些字段应该被清空
patch只传一个userName到指定资源去，表示该请求是一个局部更新, 后端仅更新接收到的字段

TODO: 2、RESTful API接口设计标准及规范

URI表示资源的两种方式：资源集合、单个资源
资源集合：
/zoos //所有动物园
/zoos/1/animals //id为1的动物园中的所有动物

单个资源：
/zoos/1 //id为1的动物园
/zoos/1;2;3 //id为1，2，3的动物园

GET：查询
GET /zoos
GET /zoos/1
GET /zoos/1/employees

POST：创建单个资源。POST一般向“资源集合”型uri发起
POST /animals  //新增动物
POST /zoos/1/employees //为id为1的动物园雇佣员工

PUT：更新单个资源（全量），客户端提供完整的更新后的资源。与之对应的是 PATCH，PATCH 负责部分更新，客户端提供要更新的那些字段。PUT/PATCH一般向“单个资源”型uri发起
PUT /animals/1
PUT /zoos/1

DELETE：删除
DELETE /zoos/1/employees/2
DELETE /zoos/1/employees/2;4;5
DELETE /zoos/1/animals  //删除id为1的动物园内的所有动物


TODO: 3、a = [1,2,3] 和 b = [(1),(2),(3) ] c = [(1,),(2,),(3,) ], a和b,b和c 的区别？

print(f'他们分别都是列表：{a},{b},{c}')
print(f'他们的类型都是：{type(a)},{type(b)},{type(c)}')
print(f'其中元素类型为：{[type(x) for x in a]},{[type(x) for x in b]},{[type(x) for x in c]}')
他们分别都是列表：[1, 2, 3],[1, 2, 3],[(1,), (2,), (3,)]
他们的类型都是：<class 'list'>,<class 'list'>,<class 'list'>
其中元素类型为：[<class 'int'>, <class 'int'>, <class 'int'>],
                [<class 'int'>, <class 'int'>, <class 'int'>],
                [<class 'tuple'>, <class 'tuple'>, <class 'tuple'>]

问题链接：https://blog.csdn.net/weixin_44266137/article/details/89318460

TODO: 4、用class来表示类的封装继承以及多态
class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass

f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

新式类继承顺序:F->D->B->E->C->A
经典类继承顺序:F->D->B->A->E->C
python3中统一都是新式类
pyhon2中才分新式类与经典类

问题链接：https://www.cnblogs.com/ajaxa/p/9049518.html

5、可以做字典key的类型有哪些？
不可变类型是可hash # tuple str freezeset
可变类型是不可hash # list set
可hash的类型可以作为字典的key
"""






"""
Mysql
第一张表 person 人员信息表：
create table person(
  id int not null auto_increment primary key,
  name varchar(50) not null,
  age int not null,
  sex char(2) not null,
  salary int not null,
  hire_date datetime default null,    # insert 数据时 可以手动输入员工入职时间
  create_time timestamp not null default current_timestamp,  # 可以记录创建数据的时间（insert数据时可以不用自己添加，会自动生成）   
  update_time timestamp not null default current_timestamp on update current_timestamp,  # 每次修改数据项，会自动记录 update时间
  dept_id int null)

insert into person(id,name,age,sex,salary,hire_date,dept_id) values(1,"璇璇",22,"女",20000,"2017-09-01",1);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(2,"西西",22,"女",16000,"2017-09-01",1);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(3,"楠楠",24,"男",18000,"2017-09-01",1);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(4,"东东",24,"男",22000,"2017-09-01",2);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(5,"哈哈",23,"男",21000,"2017-09-01",2);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(6,"呵呵",24,"女",16000,"2017-09-01",3);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(7,"梅梅",26,"女",15000,"2016-09-01",3);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(8,"浩浩",24,"男",18000,"2018-09-01",4);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(9,"夏夏",27,"女",19000,"2015-09-01",4);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(10,"星星",29,"女",12000,"2016-09-01",5);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(11,"alex",26,"男",30000,"2011-09-01",5);
insert into person(id,name,age,sex,salary,hire_date,dept_id) values(12,"Eva-J",29,"女",29000,"2012-09-01",6);
select * from person;

第二张表: dept----记录部门id以及对应的部门名称
create table dept(
  did int not null,
  name varchar(50) not null,
  create_time timestamp not null default current_timestamp,
  update_time timestamp not null default current_timestamp on update current_timestamp 
  )
insert into dept(did,name) values(1,"研发部");
insert into dept(did,name) values(2,"事业部");
insert into dept(did,name) values(3,"销售部");
insert into dept(did,name) values(4,"运营部");
insert into dept(did,name) values(5,"美工部");
insert into dept(did,name) values(6,"产品部");
select * from dept;

哦对了，为了后续讲多表联合查询，连接查询的区别，这里我再往person表 和 dept表各自增加一条信息：
insert into person(id,name,age,sex,salary,hire_date) values(13,"萌萌",25,"女",18000, "2015-02-01");  # 新增加的员工没有部门
insert into dept(did,name) values(7,"国际部")  # dept表有个部门7 person表没有员工在这个部门

问题链接: https://www.cnblogs.com/xuanxuanlove/p/9871859.html



# 如果是想查询person表的全部人员信息，而且需要显示各自的部门：需要用到联合查询
#select * from person, dept where person.dept_id=dept.did

#如果是想显示person表的全部员工信息，有dept_id的就显示部门名称，没有的也显示该条员工信息，只不过部门名称为null即可 这时候就需要用到左连接 
-- select * from person left join dept on person.dept_id=dept.did

#3. 作业
#3.1 查询出产品部年龄大于22岁工资小于30000的员工，并且按照薪资倒序排列；
# select * from person where age>22 and salary<30000 and dept_id=(select did from dept where `name`="产品部") order by salary desc

# 3.2 查询每个部门中最高工资与最低工资是多少，并且显示部门名称；
#select max(salary), min(salary), dept.name from person left join dept on person.dept_id=dept.did group by dept_id 

#查询美工部员工的名字
#select * from person where dept_id=(select did from dept where `name`="美工部")

#查询平均年龄在25岁以上的部门名
#select name from dept where did in (select dept_id from person group by dept_id having avg(age)>25)

# 查询大于所有人平均年龄的员工名与年龄
# select name, age from person where age>(select avg(age) from person)

# 查询每个部门的平均年龄
#select dept_id, avg(age) from person group by dept_id


# 查询大于部门内平均年龄的员工名、年龄
#select t1.name,t1.age from person t1 inner join (select dept_id, avg(age) avg_age from person group by dept_id) t2 on 
#t1.dept_id=t2.dept_id where t1.age>t2.avg_age


# 查询姓“李”的个数











"""




