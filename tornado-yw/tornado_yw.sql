-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        10.0.18-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出  表 kkk.hostinfo 结构
DROP TABLE IF EXISTS `hostinfo`;
CREATE TABLE IF NOT EXISTS `hostinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(16) NOT NULL DEFAULT '127.0.0.1',
  `time` int(16) NOT NULL,
  `cpuPercent` int(6) NOT NULL,
  `memTotal` int(8) NOT NULL,
  `memFree` int(8) NOT NULL,
  `diskTotal` int(32) NOT NULL,
  `diskFree` int(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 正在导出表  kkk.hostinfo 的数据：4 rows
DELETE FROM `hostinfo`;
/*!40000 ALTER TABLE `hostinfo` DISABLE KEYS */;
INSERT INTO `hostinfo` (`id`, `ip`, `time`, `cpuPercent`, `memTotal`, `memFree`, `diskTotal`, `diskFree`) VALUES
	(2, '127.0.0.1', 1440942546, 35, 4089, 1024, 1024000, 504800),
	(3, '127.0.0.1', 1440942586, 20, 4089, 103, 1024000, 154800),
	(4, '127.0.0.1', 1440942686, 45, 4089, 500, 1024000, 254800);
/*!40000 ALTER TABLE `hostinfo` ENABLE KEYS */;


-- 导出  表 kkk.hosts 结构
DROP TABLE IF EXISTS `hosts`;
CREATE TABLE IF NOT EXISTS `hosts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `hip` varchar(16) NOT NULL DEFAULT '127.0.0.1',
  `hgroup` varchar(16) NOT NULL DEFAULT 'localhost' COMMENT '主机组',
  `hport` int(6) NOT NULL DEFAULT '22',
  `huser` varchar(12) NOT NULL DEFAULT 'root',
  `hpasswd` varchar(32) NOT NULL DEFAULT '123456',
  `hstatus` int(1) NOT NULL DEFAULT '0' COMMENT '监控状态：0关闭,1开启',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ipaddr` (`hip`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1015 DEFAULT CHARSET=utf8 COMMENT='主机信息表';

-- 正在导出表  kkk.hosts 的数据：~10 rows (大约)
DELETE FROM `hosts`;
/*!40000 ALTER TABLE `hosts` DISABLE KEYS */;
INSERT INTO `hosts` (`id`, `hip`, `hgroup`, `hport`, `huser`, `hpasswd`, `hstatus`) VALUES
	(1002, '198.71.86.83', 'ftp', 22, 'root', 'kkkkkkkk', 1),
	(1003, '127.0.0.1', 'localhost', 22, 'root', '123456', 0),
	(1005, '198.71.86.84', 'www', 22, 'root', '123456', 0),
	(1006, '192.168.1.1', 'localhost', 22, 'root', '', 0),
	(1007, '192.168.1.2', 'localhost', 22, 'root', '', 0),
	(1008, '192.168.1.3', 'localhost', 22, 'root', '', 0),
	(1009, '192.168.1.4', 'localhost', 22, 'root', '', 0),
	(1010, '192.168.1.5', 'localhost', 22, 'root', '', 0),
	(1011, '192.168.1.6', 'localhost', 22, 'root', '', 0),
	(1012, '192.168.1.7', 'localhost', 22, 'root', '', 0),
	(1013, '192.168.1.8', 'localhost', 22, 'root', '', 0),
	(1014, '192.168.1.9', 'localhost', 22, 'root', '', 0);
/*!40000 ALTER TABLE `hosts` ENABLE KEYS */;


-- 导出  表 kkk.hosts_group 结构
DROP TABLE IF EXISTS `hosts_group`;
CREATE TABLE IF NOT EXISTS `hosts_group` (
  `groupid` int(2) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(16) NOT NULL DEFAULT 'localhost' COMMENT '主机组名称',
  PRIMARY KEY (`groupid`),
  KEY `id` (`groupid`,`groupname`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='主机组信息表';

-- 正在导出表  kkk.hosts_group 的数据：~9 rows (大约)
DELETE FROM `hosts_group`;
/*!40000 ALTER TABLE `hosts_group` DISABLE KEYS */;
INSERT INTO `hosts_group` (`groupid`, `groupname`) VALUES
	(1, 'localhost'),
	(2, 'www'),
	(3, 'ftp'),
	(4, 'mysql'),
	(5, 'mssql'),
	(7, 'sql'),
	(8, 'apache'),
	(9, 'nginx'),
	(10, 'other'),
	(12, 'all');
/*!40000 ALTER TABLE `hosts_group` ENABLE KEYS */;


-- 导出  表 kkk.users 结构
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL DEFAULT 'guest' COMMENT '姓名',
  `email` varchar(50) NOT NULL COMMENT '邮箱',
  `passwd` varchar(32) NOT NULL COMMENT '密码',
  `phone` varchar(18) NOT NULL DEFAULT '88888888' COMMENT '电话',
  `qx` varchar(16) NOT NULL DEFAULT 'guest' COMMENT '权限：admin,user,guest',
  `zc` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '注册日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COMMENT='用户信息表';

-- 正在导出表  kkk.users 的数据：~11 rows (大约)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `name`, `email`, `passwd`, `phone`, `qx`, `zc`) VALUES
	(1, 'admin', 'jk409@qq.com', '', '88888888', 'admin', '2015-08-30 13:09:41'),
	(2, 'guest', 'kkk@kkk.com', '', '88888888', 'user', '2015-08-30 13:09:41'),
	(6, 'kkk6666', 'kkk@s.com', 'dddd', '2223', 'admin', '2015-08-30 16:37:13'),
	(9, 'admin3', 'jk409@qq2.com', '', '88888888', 'admin3', '2015-08-30 16:49:27'),
	(18, 'flyhu', 'flyhu@126.com', '123456', '88888888', '高级', '2015-08-31 23:46:56'),
	(19, 'flyhu2', 'flyhu2@qq.com', 'flyhu2', '', '', '2015-08-31 23:47:19'),
	(21, 'user1', 'user1@qq.com', 'user1', '', '', '2015-08-31 23:47:53'),
	(22, 'user2', 'user2@qq.com', 'user2', '', '', '2015-08-31 23:48:09'),
	(23, 'user3', 'user3@qq.com', 'user3', '', '', '2015-08-31 23:48:34'),
	(24, 'user4', 'user4@qq.com', 'user4', '', '', '2015-08-31 23:48:48'),
	(25, 'user5', 'user5@qq.com', 'user5', '', '', '2015-08-31 23:56:05');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;


-- 导出  表 kkk.users_group 结构
DROP TABLE IF EXISTS `users_group`;
CREATE TABLE IF NOT EXISTS `users_group` (
  `userid` int(2) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(16) NOT NULL DEFAULT 'guest' COMMENT '用户组名称',
  PRIMARY KEY (`userid`),
  KEY `userid` (`userid`,`groupname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='用户组信息表';

-- 正在导出表  kkk.users_group 的数据：~2 rows (大约)
DELETE FROM `users_group`;
/*!40000 ALTER TABLE `users_group` DISABLE KEYS */;
INSERT INTO `users_group` (`userid`, `groupname`) VALUES
	(1, 'admin'),
	(2, 'user'),
	(3, 'backup'),
	(4, 'guest');
/*!40000 ALTER TABLE `users_group` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
