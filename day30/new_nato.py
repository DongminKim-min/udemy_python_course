import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") #csv -> dataframe
alph_dict = {row.letter:row.code for (index, row) in data.iterrows()} # use iterrows() to iterate the rows and make new dictionary with corresponding row datas
# print(alph_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        code = [alph_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code)

generate_phonetic()