#coding=utf-8
from flask import Flask
from pymongo import MongoClient
import redis,MySQLdb,os

app = Flask(__name__)
@app.route('/')
def hello():
    	client=MongoClient('mongo',27017)
	db=client.EnInternalChatTest
	collection=db.test
	collection.insert({'name':'fog'})
	print collection
	
	r=redis.Redis(host='redis',port=6379,db=0)
	r.set('name','fog')
	print r.get('name')
		
	mysql=MySQLdb.connect(host='mysql',passwd=os.getenv('MYSQL_ROOT_PASSWORD'),charset='utf8')
	cur=mysql.cursor()

	cur.execute('USE CSharp')

	result=cur.execute("INSERT INTO CS1(id,name) VALUES(1,'fog');")
	print result
	return 'hello fog'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)