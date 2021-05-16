# telbazalert
Tolbaza is web aplication for phone calls tracking. Program telbazalert use Twilio API to send sms notification when new phone call comes in Telbaza.
To Run telbazalert You need to create first config.py file, which should look like this:


    """ Config file for telbazalert.py """

    class Config:
        # Login data for Telbaza webpage
        login_data = {'0': (login1, password1),
                      '1': (login2, password2)}

        # Twilio account data
        account_sid = 'example'
        auth_token = 'example'
        from_number = 'example'
        to_number = 'example'
