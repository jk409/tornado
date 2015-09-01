#coding=utf-8
__author__ = 'Administrator'
import time,sys
sys.path.append('./mod/')
import tornado.autoreload
#import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.template
import tornado.httpclient
import tornado.gen
import sql,tpp
from tornado.options import define, options
#------------------------------------------------------------------
userupdate_res=[]
hostupdate_res=[]
#------------------------------------------------------------------
define("port", default=80, help="run on the given port", type=int)
#实例化sql类
def mysqls():
    return  sql.Mysql('127.0.0.1','root','123456','kkk')

class myapp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/file",File_Handler),
            (r"/check", Check_Handler),
            (r"/users", Users_Handler),
            (r"/users/add", UsersAdd_Handler),
            (r"/users/update", UsersUpdate_Handler),
            (r"/hosts", Hosts_Handler),
            (r"/hosts/add", HostsAdd_Handler),
            (r"/hosts/update", HostsUpdate_Handler),
            (r"/hostinfo", hostinfo_Handler),
            (r"/ll", LL_Handler),
            (r"/delete/(.*)/(.*)", Delete_Handler),
            (r".*", MainHandler),

        ]
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            'template_path':'templates',
            'static_path' :'static',
            'debug':'False'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    #@tornado.gen.engine
    def get(self):
        ips=[]
        mysql = mysqls()
        res=mysql.cmd("select *,count(distinct ip) from hostinfo group by ip")
        mysql.close()
        for i in res:
            ips.append(list(i))
        print(ips)
        self.render('index.html',ips=ips)

    def post(self):
        tms=[]
        data=[]
        cpu_data=[]
        ip = self.get_argument('ip')
        mysql = mysqls()
        res=mysql.cmd("select * from hostinfo where ip='%s'"%ip)
        res=list(res)
        for i in res:
            i=list(i)
            #i=eval(list(i))
            ts=time.strftime("%d-%H:%M",time.localtime(i[3]))
            tms.append(ts)
            data.append([ts,i[4:]])
            cpu_data.append(i[4])
        print(data,cpu_data,tms)
        self.render('hostinfo.html',data=data,ips=ip,tms=tms,cpu_data=cpu_data)

class hostinfo_Handler(tornado.web.RequestHandler):
    def get(self):
        tms=[]
        data=[]
        cpu_data=[]
        ip = self.get_argument('ip')
        mysql = mysqls()
        res=mysql.cmd("select * from hostinfo where ip='%s'"%ip)
        res=list(res)
        for i in res:
            i=list(i)
            print(i)
            ts=time.strftime("%d-%H:%M",time.localtime(i[3]))
            tms.append(ts)
            data.append([ts,i[4:]])
            cpu_data.append(i[3])
        print(data,cpu_data)
        self.render('hostinfo.html',data=data,ips=ip,tms=tms,cpu_data=cpu_data)

class File_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('file.html')

class Check_Handler(tornado.web.RequestHandler):
    def get(self):
        res=[]
        self.render('check_index.html',res=res)

    def post(self):
        data=[]
        hostlist=[
            ['127.0.0.1',80],
            ['baidu.com',80],
            ['qq.com',8080]
        ]
        #ip = self.get_argument('ip')
        #port = self.get_argument('port')
        for i in hostlist:
            res=tpp.run(i[0],i[1])
            res=list(res)
            data.append(res)
        print(res,data)
        self.render('check_index.html',res=data)

class Users_Handler(tornado.web.RequestHandler):
    def get(self):
        data=[]
        mysql=mysqls()
        res=mysql.cmd("select id,name,email,phone,qx,zc from users")
        res=list(res)
        for i in res:
            i=list(i)
            data.append(i)
        self.render('users_index.html',data=data)

class UsersAdd_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('users_add.html')

    def post(self):
        name = self.get_argument('name')
        passwd = self.get_argument('passwd')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        qx = self.get_argument('qx')
        mysql = mysqls()
        res = mysql.cmd("select count(name) from users where email='%s' limit 1;"%name)
        res = list(res)
        if res[0][0] != 0:
            self.redirect('/users/add')
        else:
            try:
                sqls = "insert into  `users` (name,passwd,email,phone,qx) values('%s','%s','%s','%s','%s');"
                mysql.cmd(sqls%(name,passwd,email,phone,qx))
                mysql.commit()
            except:
                mysql.close()
                self.redirect('/users/add')
            mysql.close()
            self.redirect('/users')

class UsersUpdate_Handler(tornado.web.RequestHandler):
    def get(self):
        self.res=[]
        id = self.get_argument('id',None)
        #print(id,type(id))
        if id == None:
            self.redirect('/users')
        mysql=mysqls()
        res=mysql.cmd("select id,name,passwd,email,phone,qx,zc from users where id=%s"%int(id))
        res=list(res)
        userupdate_res.extend(res)
        self.res.extend(res)
        #print(res[0][0],res[0][1])
        self.render('users_update.html',data=res)

    def post(self):
        id = self.get_argument('id')
        cmd = self.get_argument('cmd')
        name = self.get_argument('name')
        passwd = self.get_argument('passwd')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        qx = self.get_argument('qx')
        #print(name,passwd,email,phone,qx)
        mysql=mysqls()
        try:
            if cmd == 'update':
                sqls="update  `users` set name='%s',passwd='%s',email='%s',phone='%s',qx='%s' where id=%s;"
                mysql.cmd(sqls%(name,passwd,email,phone,qx,id))
            if cmd == 'add':
                sqls="insert into  `users` (name,passwd,email,phone,qx) values('%s','%s','%s','%s','%s');"
                mysql.cmd(sqls%(name,passwd,email,phone,qx))
            mysql.commit()
            mysql.close()
            self.redirect('/users')
        except:
            mysql.close()
            self.render('users_update.html',data=userupdate_res)
            #self.render('users_update.html',data=self.res)

class Hosts_Handler(tornado.web.RequestHandler):
    def get(self):
        data=[]
        mysql=mysqls()
        res=mysql.cmd("select id,hip,hgroup,hport,huser,hstatus from hosts")
        res=list(res)
        for i in res:
            i=list(i)
            data.append(i)
        mysql.close()
        self.render('hosts_index.html',data=data)

class HostsAdd_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('hosts_add.html')

    def post(self):
        hip = self.get_argument('hip')
        hgroup = self.get_argument('hgroup')
        hport = self.get_argument('hport')
        huser = self.get_argument('huser')
        hpasswd = self.get_argument('hpasswd')
        hstatus = self.get_argument('hstatus')
        #print(hip,hgroup,hport,huser,hpasswd,hstatus)
        mysql=mysqls()
        res=mysql.cmd("select count(hip) from hosts where hip='%s' limit 1;"%hip)
        res =list(res)
        if res[0][0] == 0:
            try:
                sqls="insert into  `hosts` (hip,hgroup,hport,huser,hpasswd,hstatus) values('%s','%s',%s,'%s','%s',%s);"
                mysql.cmd(sqls%(hip,hgroup,hport,huser,hpasswd,hstatus))
                mysql.commit()
            finally:
                mysql.close()
        self.redirect('/hosts/add')

class HostsUpdate_Handler(tornado.web.RequestHandler):

    def get(self):
        global hostupdate_res
        hostupdate_res=[]
        id = self.get_argument('id',None)
        if id == None:
            self.redirect('/hosts')
        mysql=mysqls()
        res=mysql.cmd("select id,hip,hgroup,hport,huser,hpasswd,hstatus from hosts where id=%s"%int(id))
        res=list(res)
        hostupdate_res.extend(res)
        #print(res[0][0],res[0][1])
        self.render('hosts_update.html',data=res)

    def post(self):
        cmd = self.get_argument('cmd')
        id = self.get_argument('id')
        hip = self.get_argument('hip')
        hgroup = self.get_argument('hgroup')
        hport = self.get_argument('hport')
        huser = self.get_argument('huser')
        hpasswd = self.get_argument('hpasswd')
        hstatus = self.get_argument('hstatus')
        mysql=mysqls()
        try:
            if cmd == 'update':
                sqls="update  `hosts` set hip='%s',hgroup='%s',hport=%s,huser='%s',hpasswd='%s',hstatus=%s where id=%s;"
                mysql.cmd(sqls%(hip,hgroup,hport,huser,hpasswd,hstatus,id))
            if cmd == 'add':
                sqls="insert into  `hosts` (hip,hgroup,hport,huser,hpasswd,hstatus) values('%s','%s',%s,'%s','%s',%s);"
                mysql.cmd(sqls%(hip,hgroup,hport,huser,hpasswd,hstatus))
            mysql.commit()
            mysql.close()
            self.redirect('/hosts')
        except:
            mysql.close()
            self.render('hosts_update.html',data=hostupdate_res)

class Delete_Handler(tornado.web.RequestHandler):
    def get(self,arxg1,arxg2):
        #ip = self.get_argument('ip')
        mysql = mysqls()
        try:
            mysql.cmd("delete  from %s where id='%s'"%(arxg1,arxg2))
            mysql.commit()
        finally:
            mysql.close()
            self.redirect('/%s'%arxg1)
        pass

class UserDelete_Handler(tornado.web.RequestHandler):
    def get(self,id):
        mysql = mysqls()
        mysql.cmd("delete  from users where id='%s'"%id)
        mysql.close()
        self.redirect('/user')

class Bind_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('bind.html')

class LL_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('ll.html')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(myapp())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
