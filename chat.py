from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
app.config['MYSQL_HOST']='sql12.freemysqlhosting.net'
app.config['MYSQL_USER']='sql12305446'
app.config['MYSQL_PASSWORD']='BWuf3uLXmY'
app.config['MYSQL_DB']='sql12305446'
mysql=MySQL(app)
@app.route('/', methods=['GET','POST'])
def chat():
	if request.method=="POST":
		d=request.form
		chat=d["send"]
		conn = MySQLdb.connect(host="sql12.freemysqlhosting.net", user = "sql12305446", passwd = "BWuf3uLXmY", db = "sql12305446")
		cur = conn.cursor()
		cur.execute("insert into chat (chat) values(%s)",([chat]))
		conn.commit()
		cur.execute("select * from chat")
		s=cur.fetchall()
		k=list(s)
		msg1=k[len(k)-5]
		msg2=k[len(k)-4]
		msg3=k[len(k)-3]
		msg4=k[len(k)-2]
		msg5=k[len(k)-1]
		return render_template("chat.html",msg1=msg1,msg2=msg2,msg3=msg3,msg4=msg4,msg5=msg5)

	return render_template("chat.html")
	#return render_template("")
if __name__ == '__main__':
	app.run(debug=True)
