# it reduces complexity by hiding unnecessary details

class EmailService:

    def _conncet(self):
        print('Connecting to email server...')
    
    def _authenticate(self):
        print('Authenticating...')
    
    def send_email(self):
        self._conncet()
        self._authenticate()
        print('Sending email...')
        print('Sent!')
        self._disconnect()


    def _disconnect(self):
        print('Disconnecting from the email server')

gmail = EmailService()
gmail.send_email()