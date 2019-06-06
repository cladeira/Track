from flask import Flask
import socketio
#import eventlet
#from gevent.pywsgi import WSGIServer



sio = socketio.Server()

app = Flask(__name__) #'__main__'

#@app.route('/home')
#def greeting():
#	return 'Welcome!'

@sio.on('connect') #message, disconnect

def connect(sid, environ):
	print('Conneced')
	send_control(0, 1)

def send_control(steering_angle, throttle):
	sio.emit('steer', data = {
		'steering_angle': steering_angle.__str__(),
		'throttle': throttle.__str__()
	})

if __name__ == '__main__':
	app = socketio.Middleware(sio, app)
    #WSGIServer(('', 4567), app).serve_forever()
    #eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
    #print('Serving on 8088...')
    #WSGIServer(('127.0.0.1', 8088), app).serve_forever()
