import color
import sys

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
            table = table + str(array[x][y]).ljust(cellsize)[:cellsize] + color.RESET
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


def chartpiller(array: list, hight: int, valuerange: (int, int), leaght=-1, styleGraph=0, styleBoarder=0, rotated=True, colorPos=color.WHITE, colorMin=color.WHITE, colorZero=color.WHITE):

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
                        chart.append(colorPos + " "*negative + " "*zero + "█"*positive + color.RESET)
                    else:
                        chart.append(colorPos + " "*negative + " "*zero + "█"*i + " "*(positive-i) + color.RESET)
                elif i == 0:
                    chart.append(colorZero + " "*negative + "█"*zero + " "*positive + color.RESET)
                elif i < 0: 
                    if i < negative*-1:
                        chart.append(colorMin + "█"*negative + " "*zero + " "*positive + color.RESET)
                    else: 
                        chart.append(colorMin + " "*(negative-abs(i)) + "█"*abs(i) + " "*zero + " "*positive + color.RESET)

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
                chart[i] = colorPos + chart[i] + color.RESET
            elif valueMap[i] == 0:
                chart[i] = colorZero + chart[i] + color.RESET
            elif valueMap[i] < 0:
                chart[i] = colorMin + chart[i] + color.RESET
        
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