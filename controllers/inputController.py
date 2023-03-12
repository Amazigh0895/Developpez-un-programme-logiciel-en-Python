from views import menuConstants as INPUT


class Input():
    """classe qui gere les erreurs"""

    def __init__(self):
        pass

    @staticmethod
    def makeRightChoiceInput(choice_input, user_input_choice,
                             isaNumber=True):
        """verifie si l'utilisateur a saisie
        le bon choix parmis ceux proposés"""

        user_input = ""
        if isaNumber:
            while user_input not in choice_input:
                try:
                    user_input = int(input(user_input_choice))
                except ValueError:
                    print(INPUT.ERROR_VALUE_INPUT)
            return user_input
        else:
            while user_input not in choice_input:
                try:
                    user_input = input(user_input_choice)
                except ValueError:
                    print(INPUT.ERROR_VALUE_INPUT)
            return user_input

    @staticmethod
    def makeValideChoiceInput(user_input, isaNumber=False):
        """verifie si l'utilisateur a saisie un choix valide"""
        value = ""
        if isaNumber:
            while INPUT.AVAILABLE_INPUT:
                try:
                    value = int(input(user_input))
                    INPUT.AVAILABLE_INPUT = False
                except ValueError:
                    print(INPUT.ERROR_VALUE_INPUT)
                    INPUT.AVAILABLE_INPUT = True
            INPUT.AVAILABLE_INPUT = True

        else:
            while INPUT.AVAILABLE_INPUT:
                try:
                    value = input(user_input)
                    INPUT.AVAILABLE_INPUT = False
                except ValueError:
                    print(INPUT.ERROR_VALUE_INPUT)
                    INPUT.AVAILABLE_INPUT = True
            INPUT.AVAILABLE_INPUT = True
        return value
