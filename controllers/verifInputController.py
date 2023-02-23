from views import menuConstants as INPUT
class Input():
    """classe qui gere les erreurs"""

    def __init__(self):
        pass

    def makeRightChoiceInput(choice_input,user_input ):
        """verifie si l'utilisateur a saisie le bon choix"""

        default_user_choice_input = ""
        while default_user_choice_input not in choice_input:
            try :
                default_user_choice_input = user_input 
            except:
                print(INPUT.ERROR_VALUE_INPUT)
    def makeValideChoiceInput(user_input):
        """verifie si l'utilisateur a saisie un choix valide"""

        while INPUT.AVAILABLE_INPUT:
            try:
                user_input   
                INPUT.AVAILABLE_INPUT = False

            except:
                print(INPUT.ERROR_VALUE_INPUT)
                INPUT.AVAILABLE_INPUT = True
    def ifNotZero(user_input):
         pass

        
