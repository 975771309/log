#!/usr/bin/env python
#encoding: utf-8
import logging
import logging.config
def log():
#手动配置
	# logging.basicConfig(
	# 	filename='app.log',
	# 	level=logging.ERROR
	# 	)
#读取配置方式
	logging.config.fileConfig('logconfig.ini')
	hostname='www.python.org'
	item='spam'
	filename='date.csv'
	mode='r'
#best
	logging.critical('critical %s',hostname)
	logging.error('error %s',item)
	logging.warning('warning %s',filename)
	logging.info('info %s',mode)
	logging.debug('debug %s',1)



if __name__=='__main__':
	log()
