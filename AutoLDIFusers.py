#This code was made in Python 3.7 
#and was devloped by HamzaOPLEX 
#Facebook : facebook.com/Hamza0plex
#Website : www.freetechways.xyz
#Youtube : https://www.youtube.com/channel/UCbeSJJWGNppv5decBIjsfuw
#github : github.com/HamzaOPLEX
                                      #With all LOVE and Bugs FROM HAMZAOPLEX 
import os
import sys
users_path = input("Enter the users Path >>>")
check_users_exist = os.path.exists(users_path)
check_users_is_file = os.path.isfile(users_path)
DC_DN = input("Enter You DC DN\nExample DC=ismontic,DC=ma\DC_DN>>> :") #please check this DN path
DC_DM = input("Enter You Domain name\nExample domain.com\ndomain>>> :") #please check this DN path
Users_DN = input("Where do you want to add this users (DN)\nExample DN :ou=NASA,dc=OPLEX,dc=com\nOU-DN>>>") #please check this DN path
if check_users_exist == False :
    print("[!] File Not Found")
    sys.exit()
if check_users_is_file == False :
    print("[!] File Error")
    sys.exit()
def creat_file_ldif() :
    global real_path
    global file_path
    file_path = r'C:\Users\%username%.%userdomain%\Desktop\LDIF.ldif'
    print("We will creat the File Soon .....")
    Admin_name = os.popen("echo %username%").read()
    domain_name = os.popen("echo %userdomain%").read()
    real_path = r"C:\Users\{}.{}\Desktop\LDIF.ldif".format(Admin_name.strip(),domain_name.strip())
    os.system('copy nul '+file_path)
creat_file_ldif()
file_open = open(users_path,'r')
N_lines = len(file_open.readlines())
file_open.close()
def ldif() :
    global dsquery_cmd
    dsquery = 'dsquery user "{}" -name {}'
    dsquery_run = dsquery.format(DC_DN.strip(),user_line.strip())
    dsquery_cmd = os.popen(dsquery_run).read()
    if dsquery_cmd: #if exist exit
        check = "{} is exist".format(user_line.strip())
        print(check)
    if not dsquery_cmd :
        ldif_dict = {}
        user_DN = f'CN={user_line.strip()},{Users_DN.strip()}'
        ChangeType = "add"
        ObjectClass = "user"
        CN = f"{user_line.strip()}"       
        UserPrincipaleName = f"{user_line.strip()}@{DC_DM.strip()}"
        ldif_dict["DN"]=user_DN
        ldif_dict["changetype"]=ChangeType
        ldif_dict["objectClass"]=ObjectClass
        ldif_dict["CN"]=CN
        ldif_dict["userprincipalname"]=UserPrincipaleName
        write_out = open(real_path,"a")
        for i,j in ldif_dict.items() :
            write_out.write(i+": "+j+"\n")
        write_out.close
        a = open(real_path,"a")
        a.write("\n")
        a.close
        print("[+] {} was add to the LDIF file".format(user_line.strip()))
with open(users_path,"r") as file_read :
    for i in range(N_lines):
        user_line = file_read.readline()
        ldif()
if not dsquery_cmd :
    print("Do you want to creat users now Y/N :")
    ldifde = input(">>>")
    if ldifde == 'Y' :
        os.system("ldifde -i -f "+real_path)
    if ldifde == 'N' :
        print("Thanks for your time <3")
        sys.exit()
