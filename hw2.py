# David Gonzalez
# 1630338


mon_l = {"January": '1', "February": '2', "March": '3', "April": '4', "May": '5', "June": '6', "July": '7',
         "August": '8', "September": '9', "October": '10', "November": '11', "December": '12'}
f1 = open('inputDates.txt', 'r')
f2 = open('parsedDates.txt', 'w')

for each in f1:
    if each != '-1':
        li = each.split()
        if len(li) > 3:
            m = li[0]
            d = li[1]
            y = li[2]

            if m.lower() in mon_l:
                com = d[-1]
                if com == ',':
                    d = d[:len(d)-1]
                    m_num = mon_l[m.lower()]
                    sol = m_num + '/' + d + '/' + y
                    print(sol)
                    f2.write(sol)
                    f2.write('\n')


f2.close()
f1.close()
