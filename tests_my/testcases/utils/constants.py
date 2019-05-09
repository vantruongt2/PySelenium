from enum import Enum


REPOSITORY_DEFAULT = 'SampleRepository'

# user_info
USER_NAME = 'administrator'
PASSWORD = ''

# time_out
WAIT_CONDITION_TIME = 10

# messages
LOGIN_ERROR_MESSAGE = 'Username or password is invalid'

# enum setting
class Settings(Enum):
    ADD_PAGE = 'Add Page'
    CREATE_PROFILE = 'Create Profile'
    GREATE_PANEL = 'Greate Panel'
    DELETE = 'Delete'
    EDIT = 'Edit'

