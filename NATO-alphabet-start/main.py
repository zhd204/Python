import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# word_dict = {df.loc[index, "letter"]: df.loc[index, "code"] for index in range(len(df))}
word_dict = {row.letter: row.code for index, row in df.iterrows()}
print(word_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    input_word = input("Enter a word: ").upper()
    if input_word != "QUIT":
        word_list = [word_dict[letter] for letter in list(input_word)]
        print(word_list)
        print("\nEnter 'quit' to end the game.")
    else:
        break
