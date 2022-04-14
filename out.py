import requests #подключаем библиотеку

def i():
    global get_ip
    get_ip = input('[+] IP : ')  # Вводим IP
def info():
    response = requests.get( f'http://ipinfo.io/{ get_ip }/json' )
    print(response.json())

    user_ip = response.json()[ 'ip' ]
    user_city = response.json()[ 'city' ]
    user_region = response.json()[ 'region' ]
    user_country = response.json()[ 'country' ]
    user_location = response.json()[ 'loc' ]
    user_org = response.json()[ 'org' ]
    user_timezone = response.json()[ 'timezone' ]
    dom=response.json()["hostname"]

    global all_info
    all_info = f'\n<Информация>\nIP : { user_ip }\nСити : { user_city }\nРегион : { user_region }\nСтрана : { user_country }\nЛокация : { user_location }\nОгранизация : { user_org }\nЗона : { user_timezone }\nДомен : {dom}'# вся игфа

    print( all_info )

def record():
    user_record = input( '\n[?] Хотите информацию закинуть на текстовом документе? (д/н): ' )

    if user_record == 'д':
        file = open( 'ip_data.txt', 'a' ) #вся инфа в файле ip.txt
        file.write( f'{ all_info }\n' )
        file.close()

        print( '\nВся информация, находится в текстовом документе!"' ) #Если все получилось, то пайтон выводит нам сообшение

    if user_record == 'n':
        print( '\n<O.K>' )

def main():
    while True:
        i()
        info()


main()