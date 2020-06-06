
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

def rotStringRect(string: str):
    a = string.split("\n")
    b = []

    for j in range(len(a[0])):
        b.append("")
        for i in a:
            b[j] += i[j]     
    b.reverse()
    c = ""
    for i in b:
        c = c + i + "\n"
    c = c[:-1]
    return c



def getcolorInt(fg, bg):
    return "\33[38;5;" + str(fg) + "m" + "\33[48;5;" + str(bg) + "m"

def colored(text, fg, bg=colors.bg.BLACK):
    return fg + bg + str(text) + colors.RESET 

def table(array: list, cellsize: int, style=1, direction=-1):

    if type(array) != list:
        raise ValueError("array has to be a list!")
    if type(cellsize) != int:
        raise ValueError("cellsize has to be a int!")

    if len(array) <= 0:
        if style == 1:
            return "┌┐\n└┘\n"
        elif style == 2:
            return "┌┐\n└┘\n"
        elif style == 0:
            return "┌┐\n└┘\n"
        else:
            return ""
    
    if type(array[0]) != list:
        if direction <= 0:
            array = [array]
        else:
            array = [[i] for i in array]


    if style == 1:
        table = "┌" + "─"*len(array[0])*cellsize + (len(array[0])-1)*"─" + "┐\n"
    elif style == 2:
        table = "┌" + ("─"*cellsize + "┬")*len(array[0])
        table = table[:-1] + "┐\n"
    elif style == 0:
        table = "┌" + "─"*len(array[0])*cellsize + "┐\n"
    else:
        table = ""
 

    for x in range(len(array)):
        if style >= 0:
            table = table + "│"
        
        for y in range(len(array[x])):
            table = table + str(array[x][y]).ljust(cellsize)[:cellsize]
            if style == 1:
                table = table + " "
            elif style == 2:
                table = table + "│"

        if style == 1:
            table = table[:-1] + "│\n"
        elif style >= 0 and style != 2:
            table = table + "│\n"
        else:
            table = table + "\n"
            
        if style == 2 and x+1 != len(array):
            table = table + "├" + (len(array[0]))*("─"*cellsize + "┼")
            table = table[:-1] + "┤\n"

    if style == 1:
        table = table + "└" + "─"*len(array[0])*cellsize + (len(array[0])-1)*"─" + "┘"
    elif style == 2:
        table = table + "└" + ("─"*cellsize + "┴")*len(array[0])
        table = table[:-1] + "┘\n"
    elif style == 0:
        table = table + "└" + "─"*len(array[0])*cellsize + "┘"
    
    return table

def colortable(array: list, cellsize: int, selected: dict, style=1, direction=-1):
    pass

    if type(array) != list:
        raise ValueError("array has to be a list!")
    if type(cellsize) != int:
        raise ValueError("cellsize has to be a int!")
    if type(selected) != dict:
        raise ValueError("selected has to be a dict!")

    if len(array) <= 0:
        if style == 1:
            return "┌┐\n└┘\n"
        elif style == 2:
            return "┌┐\n└┘\n"
        elif style == 0:
            return "┌┐\n└┘\n"
        else:
            return ""
    
    if type(array[0]) != list:
        if direction <= 0:
            array = [array]
        else:
            array = [[i] for i in array]


    if style == 1:
        table = "┌" + "─"*len(array[0])*cellsize + (len(array[0])-1)*"─" + "┐\n"
    elif style == 2:
        table = "┌" + ("─"*cellsize + "┬")*len(array[0])
        table = table[:-1] + "┐\n"
    elif style == 0:
        table = "┌" + "─"*len(array[0])*cellsize + "┐\n"
    else:
        table = ""


    for x in range(len(array)):
        if style >= 0:
            table = table + "│"
        
        for y in range(len(array[x])):
            if (x, y) in selected.keys():
                table = table + selected.get((x, y))
            table = table + str(array[x][y]).ljust(cellsize)[:cellsize] + colors.RESET
            if style == 1:
                table = table + " "
            elif style == 2:
                table = table + "│"

        if style == 1:
            table = table[:-1] + "│\n"
        elif style >= 0 and style != 2:
            table = table + "│\n"
        else:
            table = table + "\n"
            
        if style == 2 and x+1 != len(array):
            table = table + "├" + (len(array[0]))*("─"*cellsize + "┼")
            table = table[:-1] + "┤\n"

    if style == 1:
        table = table + "└" + "─"*len(array[0])*cellsize + (len(array[0])-1)*"─" + "┘"
    elif style == 2:
        table = table + "└" + ("─"*cellsize + "┴")*len(array[0])
        table = table[:-1] + "┘\n"
    elif style == 0:
        table = table + "└" + "─"*len(array[0])*cellsize + "┘"
    
    return table

def progressbar(summ, iteration, suffix="", prefix=""):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / summ))
    filledLength = int(50 * iteration // summ)
    bar = "█" * filledLength + '-' * (50 - filledLength)
    color = "\33[33m"
    print('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix), end = "\r")
    
def chartpillers(array: list, valueRange:list, hight: int, labelX="", lableY="", symbole="█"):
    chart = ""
    valueRangeprop = abs(valueRange[1]-valueRange[0]) / hight
    print(valueRangeprop)
    values = array.copy()

    for i in range(len(values)):
        values[i] = round(values[i] / valueRangeprop)

    for i in range(len(values)):
        if values[i] >= hight:
            chart += symbole*hight + "\n"
        elif values[i] <= 0:
            chart += " "*hight + "\n"
        else:
            chart += symbole*values[i] + " "*(hight-values[i]) + "\n"
    chart = chart[:-1]

    return rotStringRect(chart)

