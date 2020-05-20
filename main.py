from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def main():
    '''
    Login and Signup
    '''
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')



if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask
# from flask_socketio import SocketIO, send

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app)

# @socketio.on('message')
# def handleMessage(msg):
#     print('Message: ' + msg)
#     send(msg, broadcast = True)

# if (__name__ == '__main__'):
#     socketio.run(app)
