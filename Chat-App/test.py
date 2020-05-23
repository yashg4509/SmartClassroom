import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry, couldn\'t recognize what you said.')
#   print( 'recived my event: ' + str( json ) )
#   print(json['message'])
#   socketio.emit( 'my response', json, callback=messageRecived )
if('class how do you feel about' in text):
    # collect the string after about
    word = 'about'    
    index = text.index(word)
    conceptstr = text[index:]
    stri = "How do you feel about {} on a scale of 0-10, 0 being bad and 10 being good? ".format(conceptstr)

    # socketio.emit( 'my response', {"message": stri, "user_name": "Bot"}, callback=messageRecived ) #send out poll

    # rate = int(json['message'])
    # if(rate < 5):
    #     socketio.emit( 'my response', {"message": "That is alright. What questions would you like to anonymously ask the teacher?", "user_name": "Bot"}, callback=messageRecived ) #questioning
