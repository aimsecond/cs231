import os
import csv
import string
from string import maketrans

class Parse:
dir_path = os.path.dirname(os.path.realpath(__file__))
word_id = 0

def add_to_word_dict(_list, _dict, label):
    for word in _list:
        word = word.lower()
        if word not in _dict:
            word_id += 1
            _dict[word] = {"word_id":word_id,"true":0,"mostly-true":0,"half-true":0,"barely-true":0,"false":0,"pants-fire":0,"total_counts":0,"true_counts":0,"false_counts":0}
        _dict[word][label] += 1
        if label in ["true","mostly-true"]:
            _dict[word]["true_counts"] += 1
        elif label in ["barely-true","false","pants-fire"]:
            _dict[word]["false_counts"] += 1
        _dict[word]["total_counts"] += 1


# remove all punctuations in the srting except hyphen and underscore. e.g "semi-colon&(user_id)+32." => "semi-colon user_id 32"
def remove_punctuations(_string):
    puncts = string.punctuation.translate(None, "-_")
    replacement = " " * len(puncts)
    trantab = maketrans(puncts, replacement)
    return _string.translate(trantab)


# construct the word_dict dictionary
def construct_word_dict(filename):
    word_dict = {}
    vocabfile_path = os.path.join(dir_path,filename)
    
    with open(vocabfile_path) as f:
        for line in f:
            word = line[:-1].lower()
            if not word in word_dict:
                word_id += 1
                word_dict[word] = {"word_id":word_id,"true":0,"mostly-true":0,"half-true":0,"barely-true":0,"false":0,"pants-fire":0,"total_counts":0,"true_counts":0,"false_counts":0}
    return word_dict

# count words in the file, categorize them into word_dict
def count_words(filename, word_dict):
    file_path = os.path.join(dir_path, filename)
    with open(file_path) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            statement = remove_punctuations(row['statement'])
            statement_id = row['ID']
            statement_list = statement.split(" ")
            add_to_word_dict(statement_list, word_dict, row['label'])

def calculate

def main():
    word_dict = construct_word_dict('vocab.txt')
    count_words("test.tsv", word_dict)
    count_words("train.tsv", word_dict)
    count_words("valid.tsv", word_dict)
    count = 0
    for key,val in word_dict.items():
        
        if val['total_counts'] > 0:
            count += 1
        #     print key, val
    print count,"==================="

main()










#         if line[0] == '#':
#             program_type = line[1:-1]
#         elif not line[:-1] in prog_dict:
#             prog_dict[line[:-1]] = [program_type]
#         else:
#             prog_dict[line[:-1]].append(program_type)

# csvfile = os.path.join(dir_path,'output.csv')
# with open(csvfile,'a') as file:
#     for key,value in prog_dict.items():
#         file.write(key)
#         file.write('\n')
#         for i in value:
#             file.write(i+',')
#             f_read =  open(os.path.join(dir_path,'windows_measurement',i,key),'r')
#             data = f_read.readlines()
#             elapsed_time = data[-4].split()[2]
#             CPU_time = data[-3].split()[2]
#             memory_usage = data[-2].split()[2]
#             if data[-2].split()[3] == 'MB':
#                 memory_usage = float(memory_usage)*1024
#                 memory_usage = str(memory_usage)
#             CPU_load = data[-1][12:-2].split()
#             f_read.close()
#             file.write(elapsed_time+','+CPU_time+','+memory_usage+','+''.join(CPU_load)+'\n')
#             print("finish: "+key+'/'+i)