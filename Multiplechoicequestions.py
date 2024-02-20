#Things to fix
#Regardless of user's input in lower case it should convert to uppercase automatically 
#still trying to figure out the code 
#Enjoy  


class Mcq:

    def __init__ (self, prompts, answers):
        self.prompts = prompts
        self.answers = answers
        

print("Welcome to Trivia Questions\n The questions are to test your knowledge\n")
print("ALWAYS GIVE YOUR ANSWERS IN UPPERCASE lETTERS\n\n")


Question_prompts = [
                    "1. Who sang the title song for the latest Bond film, No Time to Die?\n A. Adelle B. Sam Smith C. Billie Eilish \n\n",
                    "2. Which flies a green, white, and orange (in that order) tricolor flag?\n A. Ireland B. Ivory Coast C. Italy \n\n",
                    "3. What company makes the Xperia model of smartphone?\n  A. Samsung B. Sony C. Nokia \n\n",
                    "4. Which city is home to the Brandenburg Gate?\n A. Vienna B. Zurich C. Berlin\n\n",
                    "5. Which of the following is NOT a fruit?\n A. Rhubarb B. Tomatoes C. Avocados\n\n",
                    "6. Where was the first example of paper money used?\n A. China B. Turkey C. Greece\n\n",
                    "7. Who is generally considered the inventor of the motor car?\n A. Henry Ford B. Karl Benz C. Henry M. Leland\n\n",
                    "8. If you were looking at Iguazu Falls, on what continent would you be?\n A. Asia B. Africa C. South America \n\n",
                    "9. What number was the Apollo mission that successfully put a man on the moon for the first time in human history?\n A. Apollo 11 B. Apollo 12 C. Apollo 13 \n\n",
                    "10. Which of the following languages has the longest alphabet?\n A. Greek B. Russian C. Arabic \n\n",
                    "11. Who was the lead singer of the band The Who?\n A. Roger Daltrey B. Don Henley C. Robert Plant \n\n",
                    "12. What spirit is used in making a Tom Collins?\n A. Vodka B. Rum C. Gin \n\n",
                    "13. The fear of insects is known as what?\n A.Entomophobia B. Arachnophobia C. Ailurophobia \n\n",
                    "14. What was the name of the Franco-British supersonic commercial plane that operated from 1976-2003?\n A. Accord B. Concorde C. Mirage \n\n",
                    "15. Which horoscope sign is a fish?\n A. Aquarius B. Cancer C. Pisces\n\n",
                    "16. What is the largest US state (by landmass)?\n A. Texas B. Alaska C. California \n\n",
                    "17. Which app has the most total users?\n A. TikTok B. Snapchat C. Instagram \n\n",
                    "18. Which Game of Thrones character is known as the Young Wolf?\n A. Robb Stark B. Arya Stark C. Sansa Stark \n\n",
                    "19. What city hosted the 2002 Olympic Games?\n A. Tokyo B. Beijing C. Sydney\n\n",
                    "20. How many plays do people (generally) believe that Shakespeare wrote?\n A. 27 B. 37 C. 47 \n\n",
                    "21. Which of the following was considered one of the Seven Ancient Wonders?\n A. Colosseum B. Great Wall of China C. Colossus of Rhodes\n\n",
                    "22. Who directed the Academy Award-winning movie, Gladiator?\n A. Ridley Scott B. James Cameron C. Steven Soderbergh \\n\n",
                    "23. How long did dinosaurs live on the earth?\n A. 100-150 million years B. 150-200 million years C. 200+ million years\n\n",
                    "24. What Italian city is famous for its system of canals?\n A. Rome B. Naples C. Venice \n\n",
                    "25. What is the strongest muscle in the human body?\n A. Jaw B. Heart C. Glutes \n\n",
                    "26. What is the longest-running Broadway show ever?\n A. Les Miserable B. The Lion King C. The Phantom of the Opera \n\n",
                    "27. Where was tea invented?\n A. England B. USA C. China\n\n",
                    "28. Where was the earliest documented case of the Spanish flu?\n A. USA B. Spain C. Mexico \n\n",
                    "29. Which of the following languages is NOT driven from Latin?\n A. French B. Portuguese C. English \n\n",
                    "30. Arnold Schwarzenegger was married to a member of what famous US political family?\n A. The Kennedys B. The Bushes C. The Rockefellers \n\n",
                    ]

Question_answers = [
    Mcq(Question_prompts[0], "C"),
    Mcq(Question_prompts[1], "A"),
    Mcq(Question_prompts[2], "B"),
    Mcq(Question_prompts[3], "C"),        
    Mcq(Question_prompts[4], "A"),
    Mcq(Question_prompts[5], "A"),
    Mcq(Question_prompts[6], "B"),
    Mcq(Question_prompts[7], "C"),
    Mcq(Question_prompts[8], "A"),
    Mcq(Question_prompts[9], "B"),
    Mcq(Question_prompts[10], "A"),
    Mcq(Question_prompts[11], "C"),
    Mcq(Question_prompts[12], "A"),
    Mcq(Question_prompts[13], "B"),
    Mcq(Question_prompts[14], "C"),
    Mcq(Question_prompts[15], "B"),
    Mcq(Question_prompts[16], "C"),
    Mcq(Question_prompts[17], "A"),
    Mcq(Question_prompts[18], "C"),
    Mcq(Question_prompts[19], "B"),
    Mcq(Question_prompts[20], "C"),
    Mcq(Question_prompts[21], "A"),
    Mcq(Question_prompts[22], "B"),
    Mcq(Question_prompts[23], "C"),
    Mcq(Question_prompts[24], "A"),
    Mcq(Question_prompts[25], "C"),
    Mcq(Question_prompts[26], "C"),
    Mcq(Question_prompts[27], "A"),
    Mcq(Question_prompts[28], "C"),
    Mcq(Question_prompts[29], "A"),
    
]

def run_trivia(Question_answers):
    score = 0
    for each_questions in Question_answers:
        answer = input(each_questions.prompts)
        if answer == each_questions.answers :
            score += 1
            print("Correct")
        else: 
            print("Wrong answer!!! Try again\n REMEMBER TO GIVE ANSWERS IN UPPERCASE LETTERS")
            answer = input(each_questions.prompts)
            while answer == each_questions.answers:
                score += 0.5
                print("You got it right this time")
                break
            else:
                print(f"You got it wrong and the answer is {each_questions.answers}\n REMEMBER TO GIVE ANSWERS IN UPPERCASE LETTERS")

    
    marks = (score/(len(Question_answers))) * 100
    if marks > 90:
       print("You're in the upper percentile\n Congrats Summa Cum Laude")
    elif marks > 75:
        print("You're in the middle percentile\n Congrats Magna Cum Laude")
    elif marks > 60:
        print("You're in the lower percentile\n Congrats Cum Laude")
    else: 
        print("Congrats for participating in the trivia\n Thank you ")
    
    print(f"Your score is {str(score)}\n The total number of questions is {str(len(Question_answers))}")
    

run_trivia(Question_answers)
 

                    