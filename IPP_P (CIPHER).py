from google.colab import drive
drive.mount('/content/drive') #mount sherlock.txt

import matplotlib.pyplot as plt
import itertools

def removeNonLetters(s):
    '''This function returns a list of alphabets (both upper and lower cases) without the spaces, numerals and special charcters'''
    Letter ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result =''
    for i in s:
        #Checks for all the alphabets by comparing with 'Letter'. If yes we add it to 'result'.
        if i in Letter:
            result = result+i
    return result

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    f = open(filename, "r")
    s = f.read()
    lc_letters ='abcdefghijklmnopqrstuvwxyz'
    result =''
    for i in s:
        if i in lc_letters:
            result = result + i
    return result

def letter_distribution(s):
    '''Input the string s which comprises of only lowercase letters. THe function counts
    the number of occurrences of each letter and return a dictionary'''
    CountLetters ={}
    for i in s:
        #If the letter is not present in our dictionary we create a new key and make its value '1'
        if i not in CountLetters.keys():
            CountLetters.update({i: 1})
        else:
            #If the letter is already present in our dictionary we just increment the past value by '1'
            val = CountLetters.get(i)
            val = val + 1
            CountLetters.update({i:val})
    return CountLetters

def substitution_encrypt(s,d):
    '''This function encrypts the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters in english. We return the resulting string'''
    encrypted_text =''
    for i in s:
        encrypted_text = encrypted_text + d.get(i)
    return encrypted_text

def substitution_decrypt(s,d):
    '''This function decrypts the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. It returns the resulting string'''
    
    decrypted =''
    i = 0
    #Creating a new dictionary by swapping the keys and values for easy comparisons
    d2 = {y:x for x,y in d.items()}
    while i<len(s):
        counter = 1 #min_length
        while(counter<=1): #max_length):
            strng = s[i:i+counter]
            if strng in d2.keys():
                decrypted = decrypted + d2.get(strng)
                break
            else:
                counter+=1
        i+=counter
    print(decrypted)
    return decrypted

def  generate_password(s,password): #this function ensures that the length of key is equal to length of 
    password=list(password)
    if len(s) == len(password):
        return password
    
    else:
         for i in range(len(s)-len(password)):
             password.append(password[i%len(password)])
    return "".join(password)

def rotate_text(s,r):
    m = r%(len(s))
    rotated_s = s[len(s)-m:len(s)] +  s[0:len(s)-m]
    return rotated_s

def vigenere_encrypt(s,password):
    alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    vignere_matrix=[]
    for i in range(0,26):
        vignere_matrix.append(rotate_text(alphabet, 26-i))
    #print( vignere_matrix) 
    pswd=generate_password(s,password)
    encrypted_text=[]
    for i in range(len(s)) :
        column=ord(s[i])-97
        row=ord(pswd[i])-97
        #print(row)
        #print(column)
        encrypted_text.append(vignere_matrix[row][column])
        #print( encrypted_text)
    return("" . join(encrypted_text)) 



def vigenere_decrypt(encrypted,password):
     alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
     vignere_matrix=[]
     for i in range(0,26):
        vignere_matrix.append(rotate_text(alphabet, 26-i))
     #print( vignere_matrix) 
     pswd=generate_password(encrypted,password)
     decrypted_text=[]
     for i in range(len(encrypted)):
         row=ord(pswd[i])-97
         for j in range(0,26):
           #print(vignere_matrix[row][j])
           #print( encrypted[i])
           if vignere_matrix[row][j] == encrypted[i] :
             decrypted_text.append(alphabet[j])
             break
     return("" . join(decrypted_text))

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    m = r%(len(s))
    rotated_s = s[len(s)-m:len(s)] +  s[0:len(s)-m]
    print(s)
    total = len(s)
    collided =0
    for i in range(len(s)):
        if s[i] == rotated_s[i]:
            collided+=1
    print(collided,'out of',total)

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, we predict the d'''
    CountSubs ={}
    #--------finding the frequency of each letter in encrypted text---------------------------
    for i in s:
        if i not in CountSubs.keys():
            CountSubs.update({i: 1})
        else:
            val = CountSubs.get(i)
            val = val + 1
            CountSubs.update({i:val})
    for i in CountSubs.keys():
        val = CountSubs.get(i)
        freq = (float(val)/float(len(s)))*100
        CountSubs.update({i:freq})
    values_l =[]
    #------sorting the letters based on frequency---------------------------------------------
    for i in CountSubs.values():
        values_l.append(i)
    values_l.sort(reverse=True)
    sc2 = {y:x for x,y in CountSubs.items()}
    desc_order =[]
    for i in values_l:
        desc_order.append(sc2.get(i))
    # shift = ord(desc_order[0])-ord('e')
    # if shift<0:
    #     shift = shift + 123
    # else:
    #     shift = shift + 97
    # print(shift)
    english_frequencies = 'etaionsrhldcumfgpwybvkjxzq'
    dict_key ={}
    #-----dictionary of substituted letters----------------------------------------------------
    for i in range( 0,26):
        dict_key.update({english_frequencies[i]:desc_order[i]})
    
    #----finding the occurence of three letter words-----------------------------------
    three_letter_words =[]
    for i in range(0,len(s)):
        word = s[i:i+3]
        #print(word)
        three_letter_words.append(word)
    three_letter_words_dict ={}
    for i in three_letter_words:
        if i not in three_letter_words_dict.keys():
            occur = three_letter_words.count(i)
            #print(occur)
            three_letter_words_dict.update({i:occur})
    #print(three_letter_words_dict)
    for i in three_letter_words_dict.keys():
        val = three_letter_words_dict.get(i)
        freq = (float(val)/float(len(s)))*100
        three_letter_words_dict.update({i:freq})
    #print(three_letter_words_dict)
    #frequency_list = three_letter_words_dict.values()
    #max_index = frequency_list.index(max(frequency_list))
    return three_letter_words_dict



with open('/content/drive/My Drive/sherlock.txt', 'r') as f: 
  s_text = f.read()
s = textstrip('/content/drive/My Drive/sherlock.txt')
d = {'a':'d', 'b':'e', 'c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q', 'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x','v': 'y', 'w':'z', 'x': 
         'a', 'y': 'b', 'z': 'c'}
e = substitution_encrypt(s,d)
#s = substitution_decrypt(e,d)
D = cryptanalyse_substitution(e)
D_ = {k: v for k, v in sorted(D.items(), key=lambda item: item[1], reverse =True)}
D_15 = dict(itertools.islice(D_.items(), 15))
Frequent_trigraphs =['the','and','tha','ent','ion','tio','for','nde','has','nce' ,'edt','tis','oft','sth','men']
D_15_keys = []
D_15_keys = list(D_15.keys())
for i in range(0,15):
  print(D_15_keys[i],':',Frequent_trigraphs[i])

#-------------Plotting------------------------------------------
myList = D_15.items()
myList = sorted(myList)
x, y = zip(*myList)

plt.plot(x, y)
plt.xlabel('Trigraph')
plt.ylabel('Frequency')
plt.title('Trigraph Frequency')
plt.show()

def getFrequency(s,k,frequency,start):
    for i in range(start,len(s),k):
        index=ord(s[i])-ord('a')
        frequency[index]=frequency[index]+1
    return frequency

def sort_dict(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get,reverse=True)  

    for w in sorted_keys:
      sorted_dict[w] = dict[w]

    return sorted_dict

def cryptanalyse_vigenere_afterlength(s,k): 
      '''Given the string s which is known to be vigenere encrypted with a
        password of length k, find out what is the password'''
      alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
      key=[]
      for j in range(0,k):
          frequency = [0] *(26)
          frequency=getFrequency(s, k, frequency, j)
          freqPerc={}
          for i in range(26):
              totalChar = len(s) / k
              freqPerc.update({i:(((float)(frequency[i]) / (totalChar))* 100)})
              #print(freqPerc)
              
          v=[]    
          d=sort_dict(freqPerc)
          v.extend(d.keys())
          key.append( alphabet[(v[0]-4+26)%26])
      return(key)

def findFrequentString(dict):
  '''
  Finds the frequency of each n-letter word in the encrypted string
  '''
  sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse =True)}
  sorted_dict_keys = sorted_dict.keys()
  result = []
  for i in sorted_dict_keys:
    if sorted_dict.get(i)>1:
      result.append(i)
    else:
      break
  return result

def findRepeatedSpacing(s,e):
  '''
  Finds the average spacing between repeating sub strings.
  '''
  spacing = 0
  count = 0
  index = e.find(s)
  counter = 0
  while 0<index<len(e) :
    counter = counter+index+len(s)
    strng = ''
    strng =  strng + e[counter:]
    #print(index)
    if strng.find(s)==-1:
      break
    else:
      spacing = spacing + (strng.find(s))
      index = strng.find(s)
      count = count + 1
  return (float(spacing)/count)+len(s)

def return_factors(x):
   ''' Returns the factors of the input number x
   '''
   l = []
   for i in range(1, 20):
       if x % i == 0:
           l.append(i)
   return l

def find_multiLetter_frequency(s,n):
    '''Finds the frequency of n-letter 
    words in the encrypted text'''
    n_letter_words =[]
    for i in range(0,len(s)):
        word = s[i:i+n]
        #print(word)
        n_letter_words.append(word)
    n_letter_words_dict ={}
    for i in n_letter_words:
        #print(i)
        if i not in n_letter_words_dict.keys():
            occur = n_letter_words.count(i)
            #print(occur)
            n_letter_words_dict.update({i:occur})
    return n_letter_words_dict

def most_frequent(L):
    '''Returns the most frequent 
    element in the input list'''
    counter = 0
    num = L[0]
     
    for i in L:
        curr_frequency = L.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
  #----finding the occurence of four letter words-----------------------------------
    four_letter_words_dict = find_multiLetter_frequency(s,4)
    #print(four_letter_words_dict)
    four_letter_freqs = findFrequentString(four_letter_words_dict)
  #-----finding the occurence of five letter words----------------------------------
    five_letter_words_dict = find_multiLetter_frequency(s,5)
    #print(five_letter_words_dict)
    five_letter_freqs = findFrequentString(five_letter_words_dict)
  #--------finding the occurence of six letter words-------------------------------
    six_letter_words_dict = find_multiLetter_frequency(s,6)
    six_letter_freqs = findFrequentString(six_letter_words_dict)
    #print(five_letter_freqs)
  #------Calling the Repeated Spacing function to find the spacing----------------
    RepeatedSpacing =[]
    for i in four_letter_freqs:
      result = int(findRepeatedSpacing(i,s))
      RepeatedSpacing.append(result)
    for j in five_letter_freqs:
      result = int(findRepeatedSpacing(j,s))
      RepeatedSpacing.append(result)
  #-----Finding the common factor in all spacings to get the key length----------
    #print(RepeatedSpacing)
    
    if len(RepeatedSpacing)==0:
      print('No repetitive substrings found in encrypted text!!!!!')
      return
    else:
      key_array = []
      for k in range(0,len(RepeatedSpacing)):
          list_s = return_factors(RepeatedSpacing[k])
          #print(list_s)
          for i in list_s:
            #print(i)
            if i>1:
                key_array.append(i)
      key = most_frequent(key_array)
      #print(key_array,key)
      return key

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    k = cryptanalyse_vigenere_findlength(s)
    pswd = cryptanalyse_vigenere_afterlength(s,k)
    print('Password of Vigenere Cipher :' ,pswd)
    print('Decrypted Text:' ,vigenere_decrypt(s,pswd))

with open('/content/drive/My Drive/sherlock.txt', 'r') as f: 
  s_text = f.read()
s = textstrip('/content/drive/My Drive/sherlock.txt')
e = vigenere_encrypt(s,'plaksha')
p = vigenere_decrypt(e,'plaksha')

#------We have taken a chunk of encrypted text for testing purposes. Cryptanylsing the entire encrypted text will take a little longer!!---------------

m = e[0:10000]
cryptanalyse_vigenere(m)