from utils import screen

def main():
    print("Выберите область скриншота (1 - Главная страница, 2 - Баннер на главной странице, 3 - Весь сайт)")
    answer = input()
    match int(answer):
        case 1: 
            screen.screen_main_page()
        case 2:
            screen.screen_banner()
        case 3:
            screen.screen_full_website()
    
    

if __name__ == '__main__':
    main()