def find_short(s): #vqmnit funqcias
    list1 = s.split(" ") # s values vyopt sityvebad da vsvamt listshi


    word_len = len(list1[0]) #word_len = pirveli sityvis sigrdzes
    for i in list1: #vuvlit list1-s
        if len(i) < word_len: #aq chven gvaq word_len rogor yvelaze patara sityva da TU i-s len iqneba am sityvaze ufro naklebi mashin word_len gaxdeba len(i)
            word_len = len(i)
    
    # word_len = 3
    return word_len #vareturnebt i-s

su = "welcome I love cake"
list = su.split(" ")
print(list)

sut = "very good very nice"
list2 = sut.split(" ")
print(list2)

suy = "Kono Giorno Giovanna Niwa Yume Ga Aru"
list3 = suy.split(" ")
print(list3)

suu = "who will be gru tonight"
list4 = suu.split(" ")
print(list4)

sug = "that's the question"
list5 = sug.split(" ")
print(list5)

suh = "i keep on changing the heights"
list6 = suh.split(" ")
print(list6)

sud = "and i got eyes on the back of my head"
list7 = sud.split(" ")
print(list7)

sus = "i got eyes everywhere and i know where you go(uhh)"
list8 = sus.split(" ")
print(list8)

sua = "breath i was brought bought a jet made a billion"
list9 = sua.split(" ")
print(list9)
