class UsersData():
    USER_REGISTRATION_DATA = {
                                "email": "vpupki@nyandex.ru",
                                "username": "vasya.pupkin",
                                "first_name": "Вася",
                                "last_name": "Пупкин",
                                "password": "Qwerty12asd3"
                                }

    INVALID_USER_REGISTRATION_DATA = {
                                "email": "vpupkiyandex.ru",
                                "username": "vasya. pupkin",
                                "first_name": "Вася!)(*(№;))",
                                "last_name": "Пупкин",
                                "password": "Qwerty12asd3"
                                }

    LOGIN_USER_TOKEN_DATA = {

                            "password": "Qwerty12asd3",
                            "email": "vpupki@nyandex.ru"

                            }
    INVALID_LOGIN_USER_TOKEN_DATA = {

                            "password": "Qwerty2asd3",
                            "email": "vpupki@nyandex.ru"

                            }