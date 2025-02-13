
def user_is_autorezed():
    return False

def test_abs1():
    assert abs(-50) == -50, "Должно быть положительное"
    
def test_abs2():
    assert abs(-50) == 50, "Должно быть положительное"

def test_user_is_autorezid():
    assert user_is_autorezed(), "Пользователь не авторизирован"