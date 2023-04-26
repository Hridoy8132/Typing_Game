words = ['Mango','Apple','run','orange','banana','door','television','mobile','laptop','computer','blue','keyboard',
         'Avocados','Blueberry','Blackcurrant' ,'Cranberry' ,'Cantaloupe'	,'Cherry','Dragonrfruit','Dates',	'Cherimoya',
         'Finger', 'Lime','Fig','Coconut','bluetooth', 'torso', 'female', 'thorax', 'head', 'eyeball', 'brain', 'a spinal nerve', 'lung 2 pieces', 'heart' 
         'liver', 'kidney', 'stomach',' intestine' ,'4 pieces', 'male reproductive organs' , 'Hazelnut','Honeyberries',	'Dragon' 'fruit	Durian',
         'Horned Melon','Hog Plum','Egg fruit',	'Feijoa','Indian Fig',
         'Ice Apple',	'Guava','Fuyu', 'Persimmon','Jackfruit'	,'Jujube',	'Honeydew melon','Jenipapo',
         'Kiwi	Kabosu',	'Kiwano	Kaffir', 'Lime','Lychee	Longan',	'Langsat','Mango',	'Mulberry Pear','Lucuma',
         'Muskmelon'	,'Naranjilla'	,'Passion fruit',	'Mangosteen',
         'Nectarine	Nance',	'Quince	Medlar' ,'fruit', 'Olive'	'Oranges',	'Ramphal',	'Mouse' ,'melon','Papaya Peach',
         'Rose apple', 'apple',	'Noni fruit','Pomegranate','Tangerine',	'Watermelon','Sapota','Star apple' ,'with fetuses']

def labelSlider():
    global count,sliderWords
    text = 'Welcome to Hridoy Typing Speed Game : '
    if(count >= len(text)):
        count = 0
        sliderWords =''
    sliderWords  += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)

    else:
        gameplayDetaillabel.configure(text= 'Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr= messagebox.askretrycancel('Notification',' Play Again Hit Retry Button ')

        if(rr==True):
            score = 0
            timeleft = 120
            miss =0
            timeLabelCount.configure(text= timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):

    global score,miss

    if(timeleft == 120):
        time()
    gameplayDetaillabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):  ### which word show  in display = typing word when that is matched increases score.
        score += 1
        scoreLabelCount.configure(text=score)

    else:
        miss += 1


    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

from tkinter import*
import random
from tkinter import messagebox

##### Root Method:
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg= 'blue')
root.title('Typing Speed Game')
root.iconbitmap('game.ico')
#### variables:

score = 0
timeleft = 120
count = 0
sliderWords = ''
miss = 0

##### Label Methods: bg= background fg = foreground

fontLabel = Label(root,text='',font=('airal',20,'italic bold'),
                  bg='blue',fg='orange',width=40)
fontLabel.place (x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'), bg='blue',fg='red')
wordLabel.place (x=350,y=200)

scoreLabel = Label(root,text='your Score: ',font=('airal',25,'italic bold'), bg='blue')
scoreLabel.place(x=10, y=100)

scoreLabelCount = Label(root,text= score ,font=('airal',25,'italic bold'), bg='blue',fg='yellow')
scoreLabelCount.place(x=30,y=180)

timerLabel =  Label(root,text= 'Time Left : ',font=('airal',25,'italic bold'), bg='blue')
timerLabel.place(x=600,y=100)


timeLabelCount = Label(root,text= timeleft ,font=('airal',25,'italic bold'), bg='blue',fg='yellow')
timeLabelCount.place(x=680,y=180)

gameplayDetaillabel = Label(root,text='Type World And Hit Enter Button ',font=('airal',30,'italic bold'), bg='blue',fg='dark grey')
gameplayDetaillabel.place(x=120,y=450)

#### Entry methods: bd= border.

wordEntry = Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

#######
root.bind('<Return>',startGame)

root.mainloop()