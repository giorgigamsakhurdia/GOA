age = int(input("Please enter you age: "))
if age >= 5 and age < 13:
    print("You are a child")
elif age >= 13 and age < 18:
    print("You are a teenager")
else:
    print("you are an adult")


#part 2
# sia aris kvadratul frchxilebshi(indexebshi) chawerili ragaceebi 

# index aris [ ]

# len funqcii vxedavt ramdeni monacemi gvaq cvladshi

filmis_saxelebi = ["Harry Potter", "Fury", "Jarhead"]
musics =  ["if we being real", "godzilla", "heartless "]
sum = filmis_saxelebi + musics
print(len(sum))
print(sum[2] , sum[4])