#python programm to convert time 
#from 12 hr to 24hr format
def convert24(str1):
    #check if last two element is am or pm
    #is am and first two elements are 12
    if str1[-2:] == "AM" and str1[:2]=="12":
        return "00"+str1[2:-2]
    elif str1[-2:]=="AM":
        return str1[-2:]
        #check if last two element 
        # is pm and first two are 12
    elif str1[-2:]=="PM" and str1[:2]=="12":
        return str1[:-2]
    else:
        #add 12 to hour and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]
#driver code
print(convert24("08:05:45 PM"))                