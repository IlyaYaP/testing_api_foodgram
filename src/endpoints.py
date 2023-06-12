class UsersEndPoints():
    LIST_USERS = 'http://localhost/api/users/'
    USER_REGISTRATION = 'http://localhost/api/users/'
    USER_PROFILE = 'http://localhost/api/users/1/'
    INVALIDE_USER_PROFILE = 'http://localhost/api/users/99/'
    USER_TOKEN = 'http://localhost/api/auth/token/login/'
    CURRENT_USER = 'http://localhost/api/users/me/'
    CHANGING_PASSWORD = 'http://localhost/api/users/set_password/'
    DELETE_TOKEN = 'http://localhost/api/auth/token/logout/'


class TagsEndPoints():
    LIST_TAGS = 'http://localhost/api/tags/'
    TAGS_NOT_FOUND = 'http://localhost/api/tags/99/'


class RecipesEndPoints():
    RECIPES_LIST = 'http://localhost/api/recipes/'