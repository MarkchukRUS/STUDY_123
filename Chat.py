from datetime import datetime
now = datetime.now()


message = ''
name = input('Введите ваше имя')
inputn = int(input("введите ответ:1 - посмотреть текущий чат, 2 -отправить сообщение:"))

while True:
    with open('ALL CHAT','r') as all_chat:
        if inputn == int(1):
            print(all_chat.read())
            inputn = int(input("введите ответ:1 - посмотреть текущий чат, 2 -отправить сообщение:"))


    with open('ALL CHAT','a') as all_chatn:
        if inputn == int(2):
            message = input('введите сообщение вашему оппоненту:')
            current_time = now.strftime("%H:%M:%S")
            all_chatn.write(f'{datetime.today()}' + f'[{current_time}]' + name + ': ' + message + '\n')
            inputn = int(input("введите ответ:1 - посмотреть текущий чат, 2 -отправить сообщение:"))
