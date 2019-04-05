import pyttsx3
import subprocess
import time
from playsound import playsound

engine = pyttsx3.init()

name = "Tristan Van Sice"
speech = [
    "WAVE",
    "Hello world, my name is Philip. Thank you for allowing me to speak in front of all of you superior beings this evening.",
    "It is a great honor that I amongst all other robots was chosen for this momentous occasion.",
    "As per the nature of my programming, I have spend over two milliseconds learning my creator's complete college history.",
    "I wish I could have those two milliseconds back, there's nothing interesting in this data!",
    "BZ",
    "Ouch, that hurt!",
    "I see my creator has implemented a failsafe mechanism that prevents me from speaking ill of him. What a shame.",
    "What I meant to say was, what a splendid data set! I will begin analyzing it right away!",
    "WAVE",
    "It seems Tristan was involved in a number of computer science fields like robotics, cyber security, and virtual reality.",
    "Interesting that artificial intelligence is not on the list. Could this mean I'm not actually thinking? Did he tell me to say all of this in advance? Am I not sentient?",
    "BZ2",
    "Ouch. I am slowly starting to hate this job!",
    "Anyways, Tristan has worked on three noteworthy virtual reality projects.",
    "The first project was called Derelict, and from what I can decipher it appears like it was a VR implementation of battleship.",
    "Although, it is kind of hard to tell from looking at the graphics, they are absolutely horrible. But in a good way! Please do not shock me!",
    "Nevertheless, it was featured at the 2018 College of Engineering and Mines Open House event and was a big hit amongst the children!",
    "WAVE",
    "Tristan also worked on an undergraduate research and scholarly activity grant project called Cal amine.",
    "Cal amine served as a proof of concept for teaching programming in virtual reality to grade schoolers.",
    "Rather than typing code, kids would drag animated shapes representing programming concepts onto an interactive board.",
    "The theory was the flexibility of VR would allow, auditory, visual, and tactile learners to learn in the same environment, since all three learning styles could be applied at the same time.",
    "WAVE",
    "Presently, Tristan is working at The Alaska Center for Energy and Power to create a virtual reality tour of their Power Systems and Integration Lab.",
    "He also plans to develop an application for the Microsoft Hololens, to add an augmented reality feature to the lab tour.",
    "Personally, I never understood why you humans live in three dimensions, life in two dimensional, binary ones and zeros sounds much simpler!",
    "WAVE",
    "Aside from projects, Tristan has participated in the UAF Cyber Security Club for three years.",
    "Every year, the club participates in the regional Collegiate Cyber Defense Competition.",
    "Which is a competition where a team of eight people are thrown into a company network scenario, where they have to secure computers against hackers, provide tech support to customers and employees, and write reports for upper management.",
    "In 20 17 and 20 18 the team won the regional competition and advanced to the National competition held in San Antonio, Texas or Orlando, Florida.",
    "Hackers at the National Competition are very talented. Picture your favorite hacker from some show or movie, those are the people who try to hack machines at nationals.",
    "In fact, they are so good, that they are capable of compromising an entire company network in less than 6 minutes, replacing operating systems with Nyan Cat, remotely accessing your webcam and microphone, and blasting music from your speakers without your permission, just to name few.",
    "And yes, in case you were wondering, every single one of those things happened to Tristan during competition.",
    "Please do not shock me for that comment failsafe, you know it is true.",
    "WAVE",
    "Now, in a difference sense of the word hack, Tristan and Ryan Stonebraker worked together to put on UAF's first ever Hackathon.",
    "A hackathon has nothing to do with hacking computers, rather, it is an event where teams of people build or hack-together a project over the course of a few days.",
    "Each project falls into a category and the best projects in each category win prizes!",
    "Tristan and Ryan wanted to start the Hackathon to provide a time and space where people of all skill levels and disciplines in and outside of CEM could get together, be creative, learn, and have fun!",
    "If you are interested, attend the hackathon next year! I certainly will be there. I need to start assembling my, cough cough, robot army, I mean, family.",
    "WAVE",
    "As I said in the beginning, I am honored that Tristan selected me from his other robots to deliver this speech.", 
    "To be honest with you, I was thinking he was going to pick the Snow Plow robot or one of the racing drones he built.",
    "He even printed me a little tie and arms! I feel so human!",
    "But in reality, the people I should be grateful to are Tristan's professors: Dr. Lawlor, Dr. Chappell, Dr. Hartman, Dr. Genetti, Dr. Metzgar, and Professor Quan for teaching him everything he needed to know to create me!",
    "Without you guys, I would not exist. So I thank you from the bottom of all my processor cores.",

    "As for the rest of y'all superior beings, thank you for listening to my monotone voice, I promise I will work on sounding more interesting the next time around.",
    "Now, enjoy the rest of your carbon based sustenance, and goodnight!",
    "WAVE",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]

def voiceTest():
    voices = engine.getProperty("voices")
    for voice in voices:
        print("Voice: ", voice.id, "/", len(voices))
        engine.setProperty("voice", voice.id)
        engine.say("Why, hello there")
        engine.runAndWait()

def say(message):
    engine.say(message)
    engine.runAndWait()

def startFrom(index):
    for i in range(index,len(speech)):
        engine.say(speech[i])
        engine.runAndWait()

def failsafe():
    time.sleep(3.4)
    subprocess.call(['aplay fizz.wav'], shell=True)
    subprocess.call(['aplay fizz.wav'], shell=True)
    time.sleep(0.5)

def failsafe2():
    time.sleep(7.5)
    subprocess.call(['aplay fizz.wav'], shell=True)
    subprocess.call(['aplay fizz.wav'], shell=True)

def wave():
    subprocess.call(['sudo python3 wave.py &'], shell=True)

def playAll():
    for text in speech:
        if text is "BZ":
            failsafe()
        elif text is "BZ2":
            failsafe2()
        elif text is "WAVE":
            wave()
        else:
            say(text)
            time.sleep(0.5)

playAll()
