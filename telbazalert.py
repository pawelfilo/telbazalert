""" Program sends sms notification when new phone call comes in Telbaza """

import os
from twilio.rest import Client
from selenium import webdriver
from time import sleep
from datetime import datetime
from config import Config

# Login and password for Telbaza account
login_data = Config.login_data


def send_sms(number: str, message: str) -> None:
    # Function sends sms
    account_sid = Config.account_sid
    auth_token = Config.auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body = message,
                        from_= Config.from_number,
                        to = number
                    )

    print(message.sid)


def main_loop(call_counter: int) -> None:
    # main loop function
    while True:
        call_counter_refresh = len(driver.find_elements_by_xpath('//tr[@class="ng-star-inserted"]'))


        if call_counter_refresh != call_counter:
            if login_choice == '0':
                by_number = 'HL'
            elif login_choice == '1':
                by_number = 'Investa'
            
            new_calls = call_counter_refresh - call_counter
            phone_number = Config.to_number
            timestamp = datetime.now().strftime('%H:%M:%S')
            incoming_number = driver.find_elements_by_xpath('//div[@class="external-call"]')[-1].text.replace('\n', ' ')
            message = f'[{timestamp}] Zarejestrowano nowe połączenia na numer {by_number} w ilości: {new_calls}. \
                        Ostatnie połaczenie z numeru {incoming_number}'
            print(f'\n{message}\nWysyłanie wiadomości sms...')

            try:
                send_sms(phone_number, message)
                print('\nWiadomość wysłana.')
            except:
                print('\nBłąd podczas wysyłania wiadomości')
            
            call_counter = call_counter_refresh
        
        sleep(15)


if __name__ == '__main__':

    print(f'Wybierz opcję logowania:\n0 - HL\n1 - Investa\n')
    login_choice = input()

    # Open Web browser and go to telbaza webpage
    driver = webdriver.Chrome()
    driver.get('https://telbazanet.com/')
    driver.maximize_window()
    driver.find_element_by_xpath('//input[@id="username"]').send_keys(login_data[login_choice][0])
    driver.find_element_by_xpath('//input[@id="inputPassword3"]').send_keys(login_data[login_choice][1])
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    # Wait until user sets correct date and resfesh time on webpage
    print(f'\nUstaw odświeżanie i potwierdź przyciskiem enter.')
    input()
    print('Potwierdzenie przyjęte, oczekiwanie na nowe polaczenia...')

    # Set initial amount of calls
    call_counter = len(driver.find_elements_by_xpath('//tr[@class="ng-star-inserted"]'))

    # Start main loop
    main_loop(call_counter)