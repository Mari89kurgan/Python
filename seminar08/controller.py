from view import action
import action_func
from logger import logger


def controller():
    choice_action = action()
    if choice_action == 1:
        action_func.search_contact()
    elif choice_action == 2:
        action_func.add_contact()
    elif choice_action == 3:
        action_func.delete_contact()
    else:
        action_func.edit_contact()
    logger(choice_action)

