# name = input("Please enter your name: ")
# x = name.capitalize()

# print(x)

# name1 = input("Please enter your name: ")
# y = name.upper()

# print(y)

#capitalize aris methodi romelic shemotanil stringis pirvel asos did asot aqcevs da mase printavs
#upper aris methodi romelic shemotanil strings mtlianad did asoebad anacvlebs da mase printavs
#methodi aris iseti funqcia romelic konktretuli monacemis shecvlas uwyobs xels (ar maxsovs kargad)

# sentence = "this is a senctence"
# xy = sentence.count("s")

# print(xy)

# sentence1 = "THIS IS SENTENCE1"
# xyz = sentence1.lower()

# print(xyz)

#count methodi itvis shen archeul asos dawer da gichvenebs ramdenjer aris stringshi es aso
#lower methodi shemotanis strings tu aris uppercaseshi dawerili ower caseshi dawers
#stringi aris "" chawerili ram


# text = "My name is giorgi"
# index = text.index("name")
# find = text.find("Name")
# print(index)
# print(find)

#index abrunebs romel ricxvzea chveni shetanili stringi romeli ricxvidan iwyeba
#find aris igive rac index magram roca ar iqneba monacemi -1 abrunebs
#gansxvaveba is ari rom find -1 abrunebs roca chveni monacemi ar aris saertod stingshi



sentence = 'My name is Giorgi'

print(sentence.startswith('My name is'))
print(sentence.endswith('rgi'))

email_number = int(input("How many emails do you want to input? : "))

for i in range(email_number):
    email = input("Please enter your email: ")
    if email.endswith("@gmail.com"):
        print("Your email is valid")
    else:
        print("Your email is invalid")


#startwith rom gavigot stringi riti iwyeba
#endwith rom gavigot stringi riti mtavrdeba