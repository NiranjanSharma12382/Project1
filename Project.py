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
        elif l[i]=='\n':
            new_str+=new_word+'\n'
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
    count=0
    for i in range (len(list1)):
        if list1[i]=='a':
            if (list1[i+1])[0] in vowels:
                print("Wrong! 'a' before a vowel starting word",'\"'+list1[i+1]+'\"')
                count+=1  
        elif list1[i]=='an':
            if (list1[i+1])[0] not in vowels:
                print("Wrong! 'an' before a consonant starting word",'\"'+list1[i+1]+"\"")
                count+=1 
    if count==0:    
        print("There is no problem with 'a' and 'an' in your paragraph")        
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
    print("Total vowels in the string:"+str(sum))
#vowel_counter(lower(str))
####print(vowel_counter(str))
#consonant counter:
def consonant_counter(paragraph:str):
    consonant='bcdfghjklmnpqrstvwxyz'
    consonant_list=[]
    for l in consonant:
        consonant_list.append(l)
    count_list=[]
    for i in consonant_list:
        count=0
        for j in paragraph:
            if capital(i)==capital(j) or lower(i)==lower(j):
                count+=1
        count_list.append(count)
    new_dict={}
    for k in range (len(consonant_list)):
        new_dict[capital(consonant_list[k])]=count_list[k]
    return new_dict

####print(consonant_counter(str))

#Adding a word at an index
def word_adder(paragraph:str,index:int,word_to_add:str):
    list1=paragraph.split()
    list2=list1[0:index]
    list2.append(word_to_add)
    list2+=list1[index:length(paragraph)]
    new_str=''
    for i in list2:
        new_str+=i+' '
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
            new_str+=''
        else:
            new_str+=i+' '
    print(new_str)
#remove(str,'hello')


#Return the position of first occurance of a word in a string
def position(paragraph:str,target:str):
    list1=paragraph.split()
    if target in list1:
        for i in range(len(list1)):
            if list1[i]==target:
                print("Entered word is present at index",i,"from beginning")
                break
    else:
        print("Entered word is not present in the string")
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
#remove_whitespace(str)

#Find duplicate characters in a given string
def duplicate_characters(paragraph:str):
    list1=paragraph.split()
    duplicate_list=[]
    for i in list1:
        count=0
        for j in list1:
            if i==j:
                count+=1
        if count!=1 and i not in duplicate_list:
                duplicate_list.append(i)
    print(duplicate_list)
#Find unique characters in a given string
def unique_characters(paragraph:str):
    list1=paragraph.split()
    unique_list=[]
    for i in list1:
        count=0
        for j in list1:
            if i==j:
                count+=1
        if count==1 and i not in unique_list:
                unique_list.append(i)
    print(unique_list)
#Maximum occurring character in given String
def max_frequency(paragraph:str):
    dict1=frequency(paragraph)
    words=list(dict1.keys())
    values=list((dict1).values())
    max_len=max(values)
    max_index=values.index(max_len)
    print("The maximum frequency is of","'"+words[max_index]+"'","and is equal to",max_len)


#Frequency of the specified word in the string:
def freq_word(paragraph:str,target:str):
    dict1=frequency(paragraph)
    if target in dict1.keys():
        print("The frequency of","'"+target+"'","is equal to",dict1[target])
    else:
        print("'"+target+"'","is not present in specifed paragraphs")

#Print the first non-repeated character from a string
def first_non_repeated(paragraph:str):
    dict1=frequency(paragraph)
    print((list(dict1.keys())[0]))


 

#MAIN CODE
paragraph=''
print('=================================================================')
print("ENTER STRING TO MANIPULATE")
print('=================================================================')

while True:
    line=input()
    if line=='':
        break
    paragraph+=line+'\n'
#correct

#Application Menu
menu1='''Press 1:To print total characters in the entered string
Press 2:For counting related facilities
Press 3:For changing case of provided string
Press 4:For frequency related facilities
Press 5:For finding related facilities
Press 6:For reverse related facilities
Press 7:To check if vowels 'a' and 'an' are at correct places.
Press 8:For remove related facilities
Press 9:To add a word at a particular index
Press 10:For miscellaneous fascilities       
Press -1:To exit Menu'''
menu2='''1:To count the total words in the entered string
2:To count the total alphabets in the entered string
3:To count the total numbers in the entered string
4:To count the total special characters in the string
5:To count the total number of whitespaces
-1:To Exit program'''
menu3='''1:To convert the Entered string into Uppercase
2:To convert the Entered string into Lowercase
3:To change uppercase characters to lowercase and lowercase to uppercase
-1:To Exit program'''
menu4='''1:To display the frequency of each word in the string
2:To display the frequency of each vowel in the string
3:To display the frequency of each consonant in the string
4:To find the frequency of entered word 
5:To display the word with maximum frequency
-1:To Exit program          '''
menu5='''1:To check if a word is present in the string
2:To find and replace a word in the string
-1:To Exit program'''

menu6='''1:To reverse the string
2:To reverse the content of each word
3:To reverse only the content of those words which are present at even index
4:To reverse only the content of those words which are present at odd index
-1:To Exit program'''
menu8='''1:To remove all the occurance of a word from the string
2:To remove whitespaces from the given string
-1:To Exit program'''
menu10='''1:To return the position of first occurance of a word in a string
2:To display only those words which are present at even position
3:To display only those words which are present at odd position
4:To find duplicate characters in a given string
5:To find unique characters in a given string
-1:To Exit program         '''


while True:
    print('=================================================================')
    print("SELECT YOUR CHOICE FROM THE MENU")
    print('=================================================================')
    print(menu1)
    print('=================================================================')
    
    choice=int((input("Enter Choice:")))
    if choice==1:
        print("The length of the entered string is:"+str(length(paragraph)))
    
    elif choice==2:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE SUB-MENU")
        print('=================================================================')
        print(menu2)
        print('=================================================================')

        choice2=int(input("Enter Choice:"))
        if choice2==1:
            print("Total characters in the entered string:",no_of_words(paragraph))
        elif choice2==2:
            print("Total alphabets in the entered string are:",no_of_alphabets(paragraph))
        elif choice2==3:
            print("Total numbers/digits in the entered string are:",no_of_digits(paragraph))
        elif choice2==4:
            print("Total whitespaces in the entered string are:",special_word_character(paragraph))
        elif choice2==5:
            print("Total whitespaces in the entered string are:",no_of_spaces(paragraph))
        elif choice2==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")
    
    elif choice==3:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE SUB-MENU")
        print('=================================================================')
        print(menu3)
        print('=================================================================')
        choice3=int(input("Enter Choice:"))
        if choice3==1:
            print(capital(paragraph))
        elif choice3==2:
            print(lower(paragraph))
        elif choice3==3:
            print(up_low_reverse(paragraph))
        elif choice3==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")


    elif choice==4:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE SUB-MENU")
        print('=================================================================')
        print(menu4)
        print('=================================================================')
        choice4=int(input("Enter Choice:"))
        if choice4==1:
            print("THE FREQUENCY OF EACH WORD IN THE STRING")
            print(frequency(paragraph))
        elif choice4==2:
            print("The frequency of vowels in the entered string is:",vowel_counter(paragraph))
        elif choice4==3:
             print("The frequency of consonants in the entered string is:",consonant_counter(paragraph))
        elif choice4==4:
            target=input("Enter word to find the frequency:")
            freq_word(paragraph,target)
            
        elif choice4==5:
            max_frequency(paragraph)
        elif choice4==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")
        
    elif choice==5:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE  SUB_MENU")
        print('=================================================================')
        print(menu5)
        print('=================================================================')
        choice5=int(input('Enter Choice:'))
        if choice5==1:
            word_to_find=input("Enter word to find:")
            if find(paragraph,word_to_find)==True:
              print("Yes,","'"+word_to_find+"'","is present in the entered string.")
            else:
              print("No,","'"+word_to_find+"'","is not present in the entered string.") 
        elif choice5==2:
            word_to_be_replaced1=input("Enter word to find:")
            word_to_replace=input("Enter word to replace it with:")
            print(find_replace(paragraph,word_to_be_replaced1,word_to_replace))
        elif choice5==-1:
            print("Thank you for using this program")
            break            
        else:
            print("Invalid Input, Enter a valid input!")
    

    elif choice==6:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE  SUB_MENU")
        print('=================================================================')
        print(menu6)
        print('=================================================================')
        choice6=int(input('Enter Choice:'))
        if choice6==1:
            print(reverse(paragraph))
        elif choice6==2:
            rev_word(paragraph)
        elif choice6==3:
            rev_even_word(paragraph)
        elif choice6==4:
            rev_odd_word(paragraph)
        elif choice6==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")

    
    elif choice==7:
        vowel_correct_checker(paragraph)
    
    elif choice==8:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE  SUB_MENU")
        print('=================================================================')
        print(menu8)
        print('=================================================================')
        choice8=int(input('Enter Sub-choice:'))
        if choice8==1:
            word_to_be_removed=input("Enter the word to be removed:")
            remove(paragraph,word_to_be_removed)
        elif choice8==2:
            remove_whitespace(paragraph)
        elif choice8==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")
    
    
    elif choice==9:
        index=int(input("Enter index where word is to be entered:"))
        word_to_be_added=input("Enter word to inserted:")
        print(word_adder(paragraph,index,word_to_be_added))
    
    elif choice==10:
        print('=================================================================')
        print("SELECT YOUR CHOICE FROM THE SUB_MENU")
        print('=================================================================')
        print(menu10)
        print('=================================================================')
        choice10=int(input('Enter Choice:'))
        if choice10==1:
            target=input("Enter word to find its position:")
            position(paragraph,target)
        elif choice10==2:
            even_string(paragraph)
        elif choice10==3:
            odd_string(paragraph)
        elif choice10==5:
            unique_characters(paragraph)
        elif choice10==4:
             duplicate_characters(paragraph) 
        elif choice10==-1:
            print("Thank you for using this program")
            break       
        else:
            print("Invalid Input, Enter a valid input!")
    
    elif choice==-1:
        print("Thank you for using this program")
        break    
    
    
    continu=capital(input("Do you want to continue(Y/N)?"))
    if continu=="Y":
        pass
    elif continu=='N':
        print("Thank you for using this program")
        break



  
    
