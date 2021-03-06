from flask import Flask, render_template,request,flash, redirect, render_template, \
     request, url_for,Response, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
import smtplib


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def index():

  return render_template( 'chatapp.html' )

@app.route( '/email', methods =['GET', 'POST'] )
def email():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['message']
        content="email from "+ name +" and message is "+ email
        to="beherakhirod015@gmail.com"
        server = smtplib.SMTP('smtp.sendgrid.net', 587)
        server.ehlo()
        server.starttls()
        server.login('khirodbehera.bdk@gmail.com', 'Khirod@123')
        server.sendmail('khirodbehera.bdk@gmail.com', to, content)
        server.close()

    return render_template( 'email.html' )


def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )