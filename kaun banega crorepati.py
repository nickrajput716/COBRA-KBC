# COBRA KBC 
import random
import time
kbc="COBRA KBC"
print(f"welcome to the {kbc}")
players_mood=int(input("Wana play ??? \n1. yes  \n2. no "))
questions=[ "What is the capital of India?\n1. Mumbai\n2. Delhi\n3. Kolkata\n4. Chennai",
    "Who wrote the National Anthem of India?\n1. Rabindranath Tagore\n2. Mahatma Gandhi\n3. Subhash Chandra Bose\n4. Sardar Patel",
    "What is the largest planet in our solar system?\n1. Earth\n2. Mars\n3. Jupiter\n4. Saturn",
    "Who is known as the 'Father of the Nation' in India?\n1. Jawaharlal Nehru\n2. Mahatma Gandhi\n3. Bhagat Singh\n4. Subhash Chandra Bose",
    "Which is the smallest continent by land area?\n1. Europe\n2. Australia\n3. Antarctica\n4. South America",
    "What is the square root of 144?\n1. 12\n2. 14\n3. 16\n4. 18",
    "Who discovered gravity?\n1. Isaac Newton\n2. Albert Einstein\n3. Galileo Galilei\n4. Nikola Tesla",
    "What is the chemical symbol for water?\n1. O2\n2. H2O\n3. CO2\n4. NaCl",
    "Which is the longest river in the world?\n1. Amazon\n2. Nile\n3. Ganga\n4. Yangtze",
    "Which Indian festival is known as the festival of lights?\n1. Diwali\n2. Holi\n3. Eid\n4. Christmas"]
questions_50_50=["What is the capital of India?\n1. Mumbai (X)\n2. Delhi\n3. Kolkata\n4. Chennai (X)",
    "Who wrote the National Anthem of India?\n1. Rabindranath Tagore\n2. Mahatma Gandhi (X)\n3. Subhash Chandra Bose\n4. Sardar Patel (X)",
    "What is the largest planet in our solar system?\n1. Earth (X)\n2. Mars (X)\n3. Jupiter\n4. Saturn",
    "Who is known as the 'Father of the Nation' in India?\n1. Jawaharlal Nehru (X)\n2. Mahatma Gandhi\n3. Bhagat Singh\n4. Subhash Chandra Bose (X)",
    "Which is the smallest continent by land area?\n1. Europe\n2. Australia\n3. Antarctica (X)\n4. South America (X)",
    "What is the square root of 144?\n1. 12\n2. 14 (X)\n3. 16\n4. 18 (X)",
    "Who discovered gravity?\n1. Isaac Newton\n2. Albert Einstein (X)\n3. Galileo Galilei (X)\n4. Nikola Tesla",
    "What is the chemical symbol for water?\n1. O2 (X)\n2. H2O\n3. CO2 (X)\n4. NaCl",
    "Which is the longest river in the world?\n1. Amazon\n2. Nile\n3. Ganga (X)\n4. Yangtze (X)",
    "Which Indian festival is known as the festival of lights?\n1. Diwali\n2. Holi\n3. Eid (X)\n4. Christmas (X)"]
answers=[2, 1, 3, 2, 2, 1, 1, 2, 2, 1]
lifelines=[" 1.50:50"," 2.PHONE A FRIEND "," 3.AUDIENCE POLL"," 4.SWITCH THE QUESTION","5.ASK THE EXPERT"," 6.POWER PAPLU"," 7.NONE"]
stage_coin=1000
total_coin=0
A=[1,2,3,4]
B=[5,6,7,8,9]
used_lifelines=[]
once_used=[9]
z=0
while players_mood==1:
    for i in range(1,11):
        stage_coin*=i
        selected_question=random.choice(questions)
        question_index=questions.index(selected_question)
        answer_index=questions.index(selected_question)
        print(f"YOUR QUESTION IS {selected_question} AND THE QUESTION IS FOR  {stage_coin}RS  ")
        time.sleep(2)
        choosen_lifeline=int(input(f"DO YOU WANT TO USE ANY OF THE LIFELINES  FROM {lifelines}  "))
        if choosen_lifeline==7:
            players_response=int(input(f" THEN WHAT'S THE ANSWER  :"))
        else:
         while choosen_lifeline!=9:
            if len(lifelines)>1:  
                if choosen_lifeline== 1:
                    # 50:50
                    try:
                        if once_used.index(1)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN HENCE DISQUALIFIED ")
                            z=1
                            break
                    except:
                       print(f"SO NOW AFTER REMOVING THE 2 INCORRECT OPTIONS WE HAVE : {questions_50_50[question_index]}")
                       players_response=int(input(f" THEN WHAT'S THE ANSWER  :"))
                       used_lifelines.append(lifelines[choosen_lifeline-1])
                       lifelines.pop(choosen_lifeline-1)
                       choosen_lifeline=9
                       once_used.append(1)
                       print(once_used)
                elif choosen_lifeline== 2:
                    # PHONE A FRIEND
                    try:
                        if once_used.index(2)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN SO YOU ARE DISQUALIFIED ")
                            z=1
                            break
                    except:
                     phone_number= int(input(f"ENTER THE NUMBER YOU WANT TO CALL"))
                     releative_name=input(f"WHAT'S YOUR RELATION WITH THe CALLER ")
                     print(f"CALLING {phone_number}....")
                     print(f"_")
                     time.sleep(1)
                     print(f"HELLO {releative_name} G , I AM THE HOST OF COBRA KBC ,YOURS FRIEND IS HERE WITH ME AND HE WANT YOUR HELP TO WIN A PRIZE OF {stage_coin}RS NOW YOUR FRIEND WILL SPEAK WITH YOU \n")
                     time.sleep(1)
                     print(F"USER ,YOU HAVE 30 SEC TO ASK QUESTION\n ")
                     time.sleep(5)
                     print(f"HELLO {releative_name} G THE QUESTION IS {selected_question} NOW TELL ME WHATS THE CORRECT OPTIONS \n ")
                     time.sleep(5)
                     print(f"SO ACCORING TO ME OPTION NUMBER {random.choice(A)} IS THE CORRECT OPTION \n ")
                     time.sleep(1)
                     print(f"THANK YOU {releative_name} G\n")
                     players_response=int(input(f" SO I CHOOSE THE OPTION NUMBER :"))
                     used_lifelines.append(lifelines[choosen_lifeline-1])
                     lifelines.pop(choosen_lifeline-1)
                     choosen_lifeline=9
                    
                elif choosen_lifeline== 3:
                    # AUDIENCE POLL
                    try:
                        if once_used.index(3)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN SO YOU ARE DISQUALIFIED ")
                            z=1
                            break
                    except:
                     print(f"SO YOU HAVE CHOOSEN AUDIENCE POLL NOW WE WILL TAKE A POLL BETWEEN THE AUDIENCE AND TELL YOU THE PERCENTAGE OF ALL THE OPTIONS TO BE CORRECT ACCORDING TO THE AUDIENCE ")
                     time.sleep(6)
                     print(f"SO WE HAVE THE RESULTS AS :")
                     time.sleep(2)
                     print(f" \n1.{random.choice(B)*random.choice(B)} \n2.{random.choice(B)*random.choice(B)} \n3.{random.choice(B)*random.choice(B)} \n4.{random.choice(B)*random.choice(B)}")
                     time.sleep(2)
                     players_response=int(input(f" SO NOW ACCORDING TO THE POLL GIVE YOUR ANSWER  :"))
                     used_lifelines.append(lifelines[choosen_lifeline-1])
                     lifelines.pop(choosen_lifeline-1)
                     choosen_lifeline=9
                    
                elif choosen_lifeline== 4:
                    # SWITCH THE QUESTION
                    try:
                        if once_used.index(4)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN SO YOU ARE DISQUALIFIED ")
                            z=1
                            break
                    except:
                     print(f"YOU HAVE CHOOSEN SWITCH THE QUESTION LIFELINE SO YOUR THE NEW QUESTION IS :")
                     time.sleep(2)
                     questions.pop(question_index)
                     new_question =random.choice(questions)
                     new_question_index=questions.index(new_question)
                     print(f"SO YOUR NEW QUESTION IS\n {new_question} ")
                     time.sleep(4)
                     players_response=int(input(f" THEN WHAT'S THE ANSWER  :"))
                     time.sleep(3)
                     used_lifelines.append(lifelines[choosen_lifeline-1])
                     lifelines.pop(choosen_lifeline-1)
                     choosen_lifeline=9
                    
                     if players_response==answers[questions.index(new_question)]:
                         print(f"CORRECT ANSWER YOU WON {stage_coin}RS AND TILL NOW YOU HAD WON A TOTAL OF {total_coin+stage_coin}RS \n")            
                     else:
                        print(f"SORRY WRONG ANSWER , YOU ARE GOING TO TAKE {total_coin}RS TO YOUR HOME TONIGHT \n")    
                elif choosen_lifeline== 5:
                    # ASK THE EXPERT
                    try:
                        if once_used.index(5)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN SO YOU ARE DISQUALIFIED ")
                            z=1
                            break
                    except:
                     print(f"SO YOU HAVE CHOOSEN ASK THE EXPERT LIFELINE SO NOW OUR EXPERT WILL TALK TO YOU ")
                     time.sleep(2)
                     C=[answers[answer_index],answers[answer_index+1],answers[answer_index-1]]
                     print(f"HEY USER I HAD SEEN YOUR QUESTION AND ACCORDING TO MY EXPERTIES THE CORRECT ANSWER IS OPTION NUMBER :{random.choice(C)}")
                     players_response=int(input(f"SO AFTER ASKING THE EXPERT WHAT'S YOUR ANSWER :"))
                     used_lifelines.append(lifelines[choosen_lifeline-1])
                     lifelines.pop(choosen_lifeline-1)
                     choosen_lifeline=9
                    
                elif choosen_lifeline== 6:
                    # POWER PAPLU
                    try:
                        if once_used.index(6)==True:
                            print(f"SORRY CAN'T USE THIS LIFELINE AGAIN SO YOU ARE  DISQUALIFIED ")
                            z=1
                            break
                    except:
                     if len(used_lifelines)!=0:
                        revived_option=int(input((f"WHICH OF THE USED LIFELINE YOU WANT TO REVIVE AGAIN AMONG {used_lifelines}:")))
                        choosen_lifeline=revived_option
                        continue
                     else:
                        print("YOU CAN'T USE THIS LIFELINE NOW BECAUSE YOUR ALL LIFELINES ARE STILL ALIVE")
                        players_response=int(input(f" TELL THE ANSWER NOW  :"))
                        break
                else:
                   print("YOU HAVE CHOOSEN A INVALID LIFELINE SO YOU ARE DISQUILIFIED ")
                   break
            else:
              print(f" SORRY ,NO LIFELINES LEFT ")
              players_response=int(input(f" THEN WHAT'S THE ANSWER  :"))
        if choosen_lifeline!=4:             
            if players_response==answers[questions.index(selected_question)]:
             print(f"CORRECT ANSWER YOU WON {stage_coin}RS AND TILL NOW YOU HAD WON A TOTAL OF {total_coin+stage_coin}RS \n")           
            elif z==1:
                break
            else:
              print(f"SORRY WRONG ANSWER , YOU ARE GOING TO TAKE {total_coin}RS TO YOUR HOME TONIGHT \n")
              break
        total_coin+=stage_coin
        questions.pop(question_index)
        answers.pop(question_index)
        if i in range(1,10):
          players_mood=int(input("Wana To Go To The Next Level ???  \n1. yes  \n2. no "))
          if players_mood!=1:
              break
    print(f"THAT'S ALL FOR TODAY")
    time.sleep(2)
    if total_coin>0:
        input(f"TODAY YOU HAD WON  {total_coin}RS WHAT WILL YOU DO WITH IS MONEY ")
        print("GREAT, GOOD LUCK FOR YOUR FUTURE ")
    else:
        print(F"BETTER LUCK NEXT TIME ")
    break
else:
        print("Thank you !!!")