#!/usr/bin/env python

import MySQLdb
conn = MySQLdb.connect('user=root dbname=test')
curs = conn.cursor()

reply_to = raw_input('Reply to: ')
