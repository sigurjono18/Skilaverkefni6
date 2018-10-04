import csv

def return_x(the_row,number):   #fall sem fer í gegnum línurnar og ef fallið er sama og talan sem leitað er að kemur fylkið fram
    with open('riskFactors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if row[the_row] == number:
                    x = row[0]
                line_count += 1
            else:
                line_count += 1
    return x

def return_percentage2(the_row,number):  #fall sem vinnur úr því ef tala er með prósentu, þar sem búið er að fjarlægja prósentumerkið þá þarf að bæta því við aftur til að fá fylki
    with open('riskFactors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        w = 0
        for row2 in csv_reader:
            number2 = str(number)+"0%"
            if line_count > 0:
                if row2[the_row] == number2:
                    #print(row2[11])
                    w = row2[0]
                line_count += 1
            else:
                line_count += 1
    return w

def return_float(input_x):  #fall sem tekur út prósenturmerki og skila öllum tölum sem float
    new_list = []
    for i in range(len(input_x)):
        x = input_x[i]
        x.split()
        return_number = x.replace("%","")
        z = float(return_number)
        new_list.append(z)
    return new_list

def main():   #fall sem safnar saman tölum, finnur lægstu, hæstu og prentar þær út
    with open('riskFactors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        Heart = []
        Motor = []
        Teen = []
        Smoking = []
        Obisity = []
        line_count = 0
        
        for row in csv_reader:
            if line_count > 0:
                Heart.append(row[1])
                Motor.append(row[5])
                Teen.append(row[7])
                Smoking.append(row[11])
                Obisity.append(row[13])
                line_count += 1
            else:
                line_count += 1
        
        Heart1 = []
        Heart1 = return_float(Heart)
        Motor1 = []
        Motor1 = return_float(Motor)
        Teen1 = []
        Teen1 = return_float(Teen)
        Smoking1 = []
        Smoking1 = return_float(Smoking)
        Obisity1 = []
        Obisity1 = return_float(Obisity)

        print('{:<33}{:<21}{:>15}'.format('Indicator','Min','Max'))
        print('-'*87)        
        print('{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}'.format('Heart Disease Death Rate (2007):',return_x(1,str(min(Heart1))),float(min(Heart1)),'',return_x(1,str(max(Heart1))),float(max(Heart1))))
        print('{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}'.format('Motor Vehicle Death Rate (2009):',return_x(5,str(min(Motor1))),float(min(Motor1)),'',return_x(5,str(max(Motor1))),float(max(Motor1))))
        print('{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}'.format('Teen Birth Rate (2009):',return_x(7,str(min(Teen1))),float(min(Teen1)),'',return_x(7,str(max(Teen1))),float(max(Teen1))))
        print('{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}'.format('Adult Smoking (2010):',return_percentage2(11,str(min(Smoking1))),float(min(Smoking1)),'',return_percentage2(11,str(max(Smoking1))),float(max(Smoking1))))
        print('{:<33s}{:<21s}{:>6.1f}{:^6}{:<15s}{:>6.1f}'.format('Adult Obesity (2010):',return_percentage2(13,str(min(Obisity1))),float(min(Obisity1)),'',return_percentage2(13,str(max(Obisity1))),float(max(Obisity1))))

main()