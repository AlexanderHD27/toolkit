import os
import sys

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


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


# - Clear the screen, move to (0,0):
# \033[2J
# - Erase to end of line:
# \033[K

# - Save cursor position:
# \033[s
# - Restore cursor position:
# \033[u

def moveCursor(x, y):
    sys.stdout.write("\33[{};{}H".format(y, x))
    sys.stdout.flush()

def moveCursorUp(n=1):
    sys.stdout.write("\33[{}A".format(n))
    sys.stdout.flush()

def moveCursorDown(n=1):
    sys.stdout.write("\33[{}B".format(n))
    sys.stdout.flush()  

def moveCursorFor(n=1):
    sys.stdout.write("\33[{}C".format(n))
    sys.stdout.flush()  

def moveCursorBack(n=1):
    sys.stdout.write("\33[{}D".format(n))
    sys.stdout.flush()  

def cleanAll():
    sys.stdout.write("\33[2J")
    sys.stdout.flush()  

def cleanLine():
    sys.stdout.write("\033[K")
    sys.stdout.flush()  

def print_location(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


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


def progressbar(summ, iteration, suffix="", prefix="", leaght=50):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / summ))
    filledLength = int(leaght * iteration // summ)
    bar = "█" * filledLength + '-' * (leaght - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix))
    sys.stdout.flush()

def statebar(summ, stat, suffix="", prefix="", leaght=50):
    filledLength = int(leaght * stat // summ)
    if filledLength == 0:
        bar = "|" + '-' * (leaght - filledLength)
    elif filledLength > leaght:
        bar = "-"*leaght
    else:
        bar = "="*(filledLength-1) + "|" + '-' * (leaght - filledLength)

    sys.stdout.write('\r%s |%s| %s' % (suffix, bar, prefix))
    sys.stdout.flush()

def percent(summ, iteration, suffix="", prefix=""):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / summ))
    sys.stdout.write('\r%s %s%% %s' % (suffix, percent, prefix))
    sys.stdout.flush()


def chartpiller(array: list, hight: int, valuerange: (int, int), leaght=-1, styleGraph=0, styleBoarder=0, rotated=True, colorPos=colors.WHITE, colorMin=colors.WHITE, colorZero=colors.WHITE):

    if leaght <= 0:
        values = array.copy()
    else:
        values = array[:leaght].copy()

    highest = valuerange[1]
    lowest = valuerange[0]

    valueMap = []
    step = (highest-lowest) / hight
    n = lowest + step

    negative = 0
    positive = 0
    zero = 0

    for i in range(hight):
        valueMap.append(n)
        if n > 0:
            positive += 1
        elif n == 0:
            zero += 1
        elif n < 0:
            negative += 1

        n += step

    chartValues = []

    for i in values:
        chartValues.append(int(i/step))
    
    chart = []

    if styleGraph == 0:
        for i in chartValues:
            if not rotated:
                if i > 0:
                    if i > positive:
                        chart.append(colorPos + " "*negative + " "*zero + "█"*positive + colors.RESET)
                    else:
                        chart.append(colorPos + " "*negative + " "*zero + "█"*i + " "*(positive-i) + colors.RESET)
                elif i == 0:
                    chart.append(colorZero + " "*negative + "█"*zero + " "*positive + colors.RESET)
                elif i < 0: 
                    if i < negative*-1:
                        chart.append(colorMin + "█"*negative + " "*zero + " "*positive + colors.RESET)
                    else: 
                        chart.append(colorMin + " "*(negative-abs(i)) + "█"*abs(i) + " "*zero + " "*positive + colors.RESET)

            else:
                if i > 0:
                    if i > positive:
                        chart.append(" "*negative + " "*zero + "█"*positive)
                    else:
                        chart.append(" "*negative + " "*zero + "█"*i + " "*(positive-i))
                elif i == 0:
                    chart.append(" "*negative + "█"*zero + " "*positive)
                elif i < 0: 
                    if i < negative*-1:
                        chart.append("█"*negative + " "*zero + " "*positive)
                    else: 
                        chart.append(" "*(negative-abs(i)) + "█"*abs(i) + " "*zero + " "*positive)
    
    chartString = ""
    valueMap.reverse()

    for i in chart:
        chartString += i + "\n"

    chartString = chartString[:-1]

    if rotated:
        chartString = rotStringRect(chartString)
        chart = chartString.split("\n")

        for i in range(len(chart)):
            if valueMap[i] > 0:
                chart[i] = colorPos + chart[i] + colors.RESET
            elif valueMap[i] == 0:
                chart[i] = colorZero + chart[i] + colors.RESET
            elif valueMap[i] < 0:
                chart[i] = colorMin + chart[i] + colors.RESET
        
        if styleBoarder == 0:
            numberleaght = 0
            for i in valueMap:
                if len("{: .1f}".format(i)) > numberleaght:
                    numberleaght = len("{: .1f}".format(i))

            for i in range(len(chart)):
                chart[i] = "{: .1f}".format(valueMap[i]).ljust(numberleaght) + " ┤" + chart[i] + "│"

            chart = [" "*(numberleaght+1) + "┌" + "─"*len(values) + "┐"] + chart
            chart.append(" "*(numberleaght+1) + "└" + "─"*len(values) + "┘")

        chartString = ""
        for i in chart:
            chartString += i + "\n"

    else:
        chart = chartString.split("\n")
        
        if styleBoarder == 0:
            for i in range(len(chart)):
                chart[i] = "│" + chart[i] + "│"

            chart = [" "*(negative+1) + "0"*zero + "\n┌" + "─"*negative + "┬"*zero + "─"*positive + "┐"] + chart
            chart.append("└" + "─"*negative + "┴"*zero + "─"*positive + "┘")

        chartString = ""
        for i in chart:
            chartString += i + "\n"

    return chartString