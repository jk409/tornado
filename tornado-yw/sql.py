#conding:utf8
__author__ = 'Administrator'
#jk409 update 2015-5-23
import pymysql
#import pymongo
import sqlite3
#import redis
class Mysql:
    def __init__(self,host,user,password,db):
        self.cnn = pymysql.connect(host=host,user=user, passwd=password, db=db, charset='utf8')
        #self.cnn.autocommit(True)
        self.cur= self.cnn.cursor()

    def run(self,sql):
        self.cur.execute(sql)

    def cmd(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def commit(self):
        self.cnn.commit()

    def curlclose(self):
        self.cur.close()

    def close(self):
        self.cnn.close()

class Mongodb():
    def __init__(self, ip, port, db):
        self.conn = pymongo.Connection(ip, port)
        self.db = self.conn[db]

    def find(self,table):
        return self.db[table].find({}).limit(1500)

    def find_one(self,table,xarg):
        return self.db[table].find_one(xarg)

    def insert(self,table, xarg):
        try:
            data = self.db[table]
            data.insert(xarg)
        finally:
            self.conn.close()

    def remove(self,table ,xarg):
        try:
            data = self.db[table]
            data.remove(xarg)
        finally:
            self.conn.close()

    def save(self,table, xarg):
        try:
            data = self.db[table]
            data.save(xarg)
        finally:
            self.conn.close()

    def update(self,table ,*xarg):
        try:
            data = self.db[table]
            data.update(*xarg)
        finally:
            self.conn.close()

class redis():
    def __init__(self,host,port,db,passwd):
        #self.cnn=redis.Connection(host='localhost',port=6379,db=0,password='',encoding='utf-8')
        self.cnn=redis.Redis(host=host,port=port,db=db,password=passwd,encoding='utf-8')

    def get(self,name):
        data = self.cnn
        data.get(name)

    def append(self,key,value):
        data = self.cnn
        data.append(key,value)


class Sqlite3():
    def __init__(self,db):
        self.cnn = sqlite3.connect(database=db)
        self.cur = self.cnn.cursor()

    def run(self,args):
        self.cur.execute(args)

    def cmd(self,args):
        return self.cur.execute(args)

    def commit(self):
        self.cnn.commit()

    def close(self):
        self.cnn.close()

    def INIT(self):
        sql = '''create table blog(
            id int,
            name varchar(32),
            email varchar(32),
            title varchar(32),
            fl varchar(32),
            tag varchar(32),
            date varchar(32),
            content varchar
        ) '''
        #sql2='alter table blog add column content  varchar;'
        self.cmd(sql)

if __name__ == '__main__':
    pass
	

