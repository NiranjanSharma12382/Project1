str='''hello DarkNess my old friend
i come to see You again'''


#Length of string
def length(str):
    count=0
    for i in str:
        count+=1
    return count
#TASK 1 - No. of words
def no_of_words(str):
    count=0
    list=str.split()
    for i in list:
        count+=1
    return count
#TASK 2 - No. of digits
def no_of_digits(str):
    count=0
    for i in str:
        if i.isdigit()==True:
            count+=1
    return count
#TASK 3 - No. of alphabets
def no_of_alphabets(str):
    count=0
    for i in str:
        if i.isalpha()==True:
            count+=1
    return count
#TASK 4 - Checking if a word if present in the string
def check_if_present(str,check_word):
    if check_word in str:
        return "YES"
    else:
        return "NO"
#print(check_if_present('hello guys',input("Enter phrase to check:")))     

#Task 5-converting whole paragraph to uppercase
def capital(str):
    upper_str=''
    for i in str:
        if ord(i)<=122 and ord(i)>=97:
            upper_str+=chr(ord(i)-32)
        else:
            upper_str+=i
    return upper_str


#Task 5-converting whole paragraph to lowercase
def lower(str):
    lower_str=''
    for i in str:
        if ord(i)<=90 and ord(i)>=65:
            lower_str+=chr(ord(i)+32)
        else:
            lower_str+=i
    return lower_str

#Reversing the paragraph
def reverse(str):
    rev_str=''
    for i in range (length(str),0,-1):
        rev_str+=str[i-1]
    return rev_str

#Finding and replacing a word from paragraph
def find_replace(paragraph:str,word_to_be_replaced:str,new_word:str):
    l=paragraph.split()
    new_str=''
    for i in range(length(l)):
        if l[i]==word_to_be_replaced:
            new_str+=new_word+' '
        else:
            new_str+=l[i]+' '
    return new_str
#print(find_replace(str,'hello','yellow'))

#Checking if a word is present in the Paragraph
def find(paragraph:str,word_to_find):
    l=paragraph.split()
    if word_to_find in paragraph:
        return True
    else:
        return False

#Calculating frequency of each word in the paragraph
def frequency(paragraph:str):
    l=paragraph.split()
    unique=[]
    for i in l:
        if i not in unique:
            unique.append(i)
    count_list=[]
    for j in unique:
        count=0
        for k in l:
            if j==k: 
                count+=1
        count_list.append(count)
    freq_dict={}
    for m in range(len(unique)):
        freq_dict[unique[m]]=count_list[m]
    return freq_dict
   
#Checking if 'a' and 'an' are in right place
def vowel_correct_checker(paragraph:str):
    list1=paragraph.split()
    vowels=['a','e','i','o','u']
    for i in range (len(list1)):
        if list1[i]=='a':
            if (list1[i+1])[0] in vowels:
                print("Wrong! 'a' before a vowel starting word",'\"'+list1[i+1]+'\"')  
        elif list1[i]=='an':
            if (list1[i+1])[0] not in vowels:
                print("Wrong! 'an' before a consonant starting word",'\"'+list1[i+1]+"\"")
#vowel_correct_checker('i am niranjan . i have a apple , i go to an school an')

#vowel counter:
def vowel_counter(paragraph:str):
    vowels=['a','e','i','o','u']
    count_list=[]
    for i in vowels:
        count=0
        for j in paragraph:
            if i==j:    
                count+=1
        count_list.append(count)    
    new_dict={}
    sum=0
    for l in count_list:
        sum+=l
    for k in range(5):
        new_dict[vowels[k]]=count_list[k]
    print(new_dict)
    print(sum)
#vowel_counter(lower(str))
####print(vowel_counter(str))
#consonant counter:
def consonant_counter(paragraph:str):
    vowels=['a','e','i','o','u',' ']
    count=0
    for i in paragraph:
        if i not in vowels:
            count+=1    
    return count
####print(consonant_counter(str))

#Adding a word at an index
def word_adder(paragraph:str,index:int,word_to_add:str):
    list1=paragraph.split()
    new_str=list1[0:index]
    new_str.append(word_to_add)
    new_str+=list1[index:length(paragraph)]
    return new_str
#print(*word_adder(str,3,'lololo'))

#Calculating total special characters
def special_word_character(paragraph:str):
    count=0
    for i in paragraph:
        if ord(i) in range (32,48) or ord(i) in range (58,65) or ord(i) in range (91,97) or ord(i) in range(123,127):
            if i!=' ':
                count+=1 
    return count
#print(special_word_character(str))
#calculating Number of spaces:
def no_of_spaces(paragraph:str):
    count=0
    for i in paragraph:
        if i==' ':
            count+=1
    return count
#print(no_of_spaces(str))

#Changing uppercase characters to lowercase and lowercase to uppercase
def up_low_reverse(paragraph:str):
    new_str=''
    for i in paragraph:
        if ord(i)<=122 and ord(i)>=97:
            new_str+=chr(ord(i)-32)
        elif ord(i)<=90 and ord(i)>=65:
            new_str+=chr(ord(i)+32)
        else:
            new_str+=i 
    return new_str
#print (up_low_reverse(str))

#Removing all the occurance of a word from the string
def remove(paragraph:str,target:str):
    list1=paragraph.split()
    new_str=''
    for i in list1:
        if i==target:
            new_str+=' '
        else:
            new_str+=i+' '
    print(new_str)
#remove(str,'hello')


#Return the position of first occurance of a word in a string
def position(paragraph:str,target:str):
    list1=paragraph.split()
    for i in range(len(list1)):
        if list1[i]==target:
            print(i)
            break
#position(str,'old')

#Make a new string which contain only those words which are present at even position from the given input string.
def even_string(paragraph:str):
    list1=paragraph.split()
    new_str=''
    for i in range(0,len(list1),2):
            new_str+=list1[i]+' '
    print(new_str)
#even_string(str)


#Make a new string which contain only those words which are present at odd position from the given input string.
def odd_string(paragraph:str):
    list1=paragraph.split()
    new_str=''
    for i in range(1,len(list1),2):
            new_str+=list1[i]+' '
    print(new_str)
#odd_string(str)

#Reversing the content of each word
def rev_word(paragraph:str):
    list1=paragraph.split()
    new_str=''
    for i in list1:
        new_i=i[::-1]
        new_str+=new_i+' '
    print(new_str)
#rev_word(str)
#Reverse only the content of those words which are present at even index
def rev_even_word(paragraph:str):
    list1=paragraph.split()
    new_str=''
    count=0
    for i in list1:
        count+=1
        if count%2==0:
            new_i=i[::-1]
            new_str+=new_i+' '
        else:
            new_str+=i+' '
    print(new_str)
#rev_even_word(str)
#Reverse only the content of those words which are present at odd index
def rev_odd_word(paragraph:str):
    list1=paragraph.split()
    new_str=''
    count=0
    for i in list1:
        count+=1
        if count%2==1:
            new_i=i[::-1]
            new_str+=new_i+' '
        else:
            new_str+=i+' '
    print(new_str)
#rev_odd_word(str)

#Remove all space from the input string
def remove_whitespace(paragraph:str):
    new_str=''
    for i in paragraph:
        if i!=' ' and i!='\n':
            new_str+=i
    print(new_str)
remove_whitespace(str)

            





