from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import speech_recognition as sr

# Speech Recognition

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        # print('You said: {}'.format(text))
    except:
        print('Sorry, couldn\'t recognize what you said.')
        
# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

# if('class how do you feel about' in text):
#     # collect the string after about
#     word = 'about'    
#     index = text.index(word)
#     conceptstr = text[index:]
    
#     numstr = input("How do you feel about {} on a scale of 0-10, 0 being bad and 10 being good? ".format(conceptstr))
#     num = int(numstr)
#     if(num < 5):
#         question = input('That is alright. What questions would you like to anonymously ask the teacher? ')
#         print('A student had this question: ' + question)
            
#     elif(num >= 5):
#         print('Good to hear, we can move on.')

# if('yes or no' in text):
# #     word = 'yes'
# #     index = text.index(word)
# #     conceptstr = text[index-2]
    
#     clarification = input("Do you understand? If so, please type Y or N.")
#     if(clarification == 'Y'):
#         print('Good to hear, we can move on.')
#     elif(clarification == 'N'):
#         question = input('That is alright. What questions would you like to anonymously ask the teacher? ')
#         print('A student had this question: ' + question)



@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )
  if('class how do you feel about' in text):
    # collect the string after about
    word = 'about'    
    index = text.index(word)
    conceptstr = text[index:]
    stri = "How do you feel about {} on a scale of 0-10, 0 being bad and 10 being good? ".format(conceptstr)
    
    socketio.emit( 'my response', {"message": stri, "user_name": "Bot"}, callback=messageRecived ) #send out poll

    rate = int(json['message'])
    if(rate < 5):
      socketio.emit( 'my response', {"message": "That is alright. What questions would you like to anonymously ask the teacher?", "user_name": "Bot"}, callback=messageRecived ) #questioning

if __name__ == '__main__':
  socketio.run( app, debug = True )