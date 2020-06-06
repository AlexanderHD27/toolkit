
class colors:
    RESET = "\33[0m"

    BLACK = "\33[30m"
    RED = "\33[31m"
    GREEN = "\33[32m"
    YELLOW = "\33[33m"
    BLUE = "\33[34m"
    PURPLE = "\33[35m" 
    LIGHTBLUE = "\33[36m"
    WHITE = "\33[37m"

    class style:
            BOLD = "\33[1m"    
            UNDERLINE = "\33[4m"
            INVERTED = "\33[7m"

    class bg:
        BLACK = "\33[40m"
        RED = "\33[41m"
        GREEN = "\33[42m"
        YELLOW = "\33[43m"
        BLUE = "\33[44m"
        PURPLE = "\33[45m" 
        LIGHTBLUE = "\33[46m"
        WHITE = "\33[47m"

def getcolorInt(fg, bg):
    return "\33[38;5;" + str(fg) + "m" + "\33[48;5;" + str(bg) + "m"

def colored(text, fg, bg=colors.bg.BLACK):
    return fg + bg + str(text) + colors.RESET 
