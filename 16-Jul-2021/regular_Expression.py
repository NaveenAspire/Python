import re
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" 
def check(Ip):
    if(re.search(regex_ip, Ip)):
        print("Valid Ip address")    
    else:
        print("Invalid Ip address")
Ip =input("Enter the IP address to check")
check(Ip)

regex_phone = "^(([0-9]){10})$"

def checkPhone(phone):
    if(re.search(regex_phone,phone)):
        print("valid Phone")
    else:
        print("Invalid phone")
    
phone = input("Enter Phone Number : ")
checkPhone(phone)