
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
    print('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix), end = "\r")

def chartpillers(array: list, valueRange:list, hight: int, symbole="█"):
    chart = ""
    valueRangeprop = abs(valueRange[1]-valueRange[0]) / hight
    values = array.copy()

    for i in range(len(values)):
        values[i] = abs(int(values[i] / valueRangeprop))

    for i in range(len(values)):

        if values[i] >= hight:
            chart += symbole*(hight) + "\n"
        elif values[i] <= 0:
            chart += " "*(hight) + "\n"
        else:
            chart += symbole*values[i] + " "*(hight-values[i]) + "\n"
        
        
    chart = chart[:-1]

    prefix = "┌" + "─"*len(values) + "┐\n│"
    sufix = "│\n└" + "─"*len(values) + "┘"
    chart = (prefix + rotStringRect(chart).replace("\n", "│\n│") + sufix).split("\n")
    
    leaghtnumber = len(str((len(chart)-1)*valueRangeprop)) + 2

    chart[0] = leaghtnumber*" " + chart[0]
    chart[-1] = leaghtnumber*" " + chart[-1]

    n = valueRange[1]
    for i in range(1, hight+1):
        chart[i] = "{:.1f}".format(n).ljust(leaghtnumber) + "┤" +chart[i][1:]
        n -= valueRangeprop

    chartString = ""
    for i in chart:
        chartString += i + "\n"

    return  chartString

def chart(array: list, hight: int, valuerange: (int, int), leaght=-1, styleGraph=0, styleBoarder=0, rotated=True, colorPos=colors.WHITE, colorMin=colors.WHITE, colorZero=colors.WHITE):

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