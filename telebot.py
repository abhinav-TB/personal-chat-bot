import requests as requests
import random
import webbrowser

url = "https://api.telegram.org/bot1087700191:AAHm7jvxWw9lJ3nnspCNDHn3nQEn6GiKlTg/"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), 'Hello Welcome to our bot. Type "Play" to roll the dice!')
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + ' and ' + str(_3) + ' !\n Your result is ' +
                             str(_1 + _2 + _3) + '!!!')
            elif get_message_text(update).lower() == "good morning":
                send_message(get_chat_id(update), 'good morning have a nice day')
            elif get_message_text(update).lower().split(' ', 1)[0]=="google":
                from selenium import webdriver
                driver = webdriver.Chrome()
                driver.get('https://www.google.com/')
                searchbox=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                searchbox.send_keys(get_message_text(update).lower().split(' ', 1)[1])
                searchbutton=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
                popblock=driver.find_element_by_xpath('//*[@id="hplogo"]')
                popblock.click()
                searchbutton.click()
                send_message(get_chat_id(update), 'good morning have a great day sir')
            elif get_message_text(update).lower() == "open google":
                send_message(get_chat_id(update), webbrowser.open('www.google.com'))
            elif get_message_text(update).lower() == "open safety":
                send_message(get_chat_id(update), webbrowser.open('https://abhinav-tb.github.io/safety-web/'))
            elif get_message_text(update).lower() == "open ml":
                send_message(get_chat_id(update), webbrowser.open('https://teachablemachine.withgoogle.com/models/lZBLyuB4/'))
            else:
                send_message(get_chat_id(update), "Sorry Not Understand what you inputed:")
            update_id += 1


# call the function to make it reply .
  
if __name__== "__main__":
  main()