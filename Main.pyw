import webbrowser
from random import randint
from tkinter import Tk, Frame, Label, StringVar, Button

from PIL import Image, ImageTk

import BuildFromScratch
import listeFlags


class Dice(Frame):

    def __init__(self, root):  # CONSTRUCTEUR
        Frame.__init__(self, root)

        self.titre = StringVar(self)
        self.titre.set("BONNE CHANCE !")
        self.superFlag = ""
        self.web = False

        Label(self, textvariable=self.titre).pack()
        Button(self, text="Preset", command=self.lancer).pack()
        Button(self, text="Scratch", command=self.scratch).pack()

        self.image = ImageTk.PhotoImage(Image.open("images/FFIVFE-Bosses-19Golbez-Color.png"))
        self.label1 = Label(self, image=self.image)
        self.label1.pack()

    # Copier dans le presse paiper
    def copierFlag(self, flag):
        self.clipboard_clear()
        self.clipboard_append(flag)

    # Image du menu
    def imageMenu(self, numFlag):
        self.label1.destroy()
        self.image = ImageTk.PhotoImage(Image.open(listeFlags.DicoImages[numFlag]))
        self.label1 = Label(self, image=self.image)
        self.label1.pack()

    # Choix du flag avec copie et image dans le prog
    def choixFlag(self, numFlag):
        self.titre.set(listeFlags.DicoNomfFlag[numFlag])
        self.copierFlag(listeFlags.DicoFlag[listeFlags.DicoNomfFlag[numFlag]])
        self.imageMenu(numFlag)

    # Choisis une seed pédéfinie
    def lancer(self):
        # Random
        chiffre = (randint(1, 9))

        if chiffre == 1:
            chiffre = (randint(1, 6))
            if chiffre == 1:
                self.choixFlag(chiffre)
                self.imageMenu(chiffre)
            else:
                self.choixFlag(11)
                self.imageMenu(11)

        elif chiffre == 6:
            chiffre = (randint(1, 6))
            if chiffre == 6:
                self.choixFlag(chiffre)
                self.imageMenu(chiffre)
            else:
                self.choixFlag(10)
                self.imageMenu(10)
        else:
            self.choixFlag(chiffre)

        if self.web is False:
            webbrowser.open("http://ff4fe.com/make")
            self.web = True

    # Objectifs
    def randObjectifFlag(self):
        # Objective Mode
        alea = randint(0, 4)
        if alea == 0:
            self.superFlag += "Onone"
        elif alea == 4:
            alea2 = randint(1, 20)
            if alea2 != 4:
                alea = randint(1, 3)
                self.aleaObjectiveMode(alea)
            else:
                self.aleaObjectiveMode(alea2)
        else:
            self.aleaObjectiveMode(alea)

        # Custom objective
        custom = randint(0, 8)
        if custom == 0:
            pass
        else:
            self.customObjective(custom)

        # Random objective
        random = randint(0, 5)
        if random == 0:
            pass
        else:
            self.randomObjective(random)

        # Reward
        if (random or custom) == 0:
            pass
        else:
            reward = randint(1, 2)
            self.rewardObjective(reward)

    def aleaObjectiveMode(self, alea):

        if alea == 4:
            alea2 = randint(1, 20)
            if alea2 != 4:
                alea = randint(1, 3)

        self.superFlag = "Omode:"
        maxObjectifMode = len(BuildFromScratch.DicoObjectivesMode)
        listeObjectif = []

        if alea == maxObjectifMode:
            for i in range(2, maxObjectifMode + 1):
                listeObjectif.append(BuildFromScratch.DicoObjectivesMode[i])
        else:
            while len(listeObjectif) != alea:
                rand2 = randint(2, maxObjectifMode)
                if rand2 == 4:
                    rand2 = randint(1, 30)
                    if rand2 == 4:
                        pass
                    else:
                        rand2 = randint(1, 3)

                if BuildFromScratch.DicoObjectivesMode[rand2] in listeObjectif:
                    pass
                else:
                    listeObjectif.append(BuildFromScratch.DicoObjectivesMode[rand2])

        for i in range(len(listeObjectif)):
            self.superFlag += listeObjectif[i]
            if i != len(listeObjectif) - 1:
                self.superFlag += ","

    def customObjective(self, custom):

        taille = len(BuildFromScratch.DicoObjectiveCustom)
        listeCustom = []

        if self.superFlag == "Onone":
            self.superFlag = "O"
        else:
            self.superFlag += "/"

        while len(listeCustom) != custom:
            rand2 = randint(2, taille)
            if BuildFromScratch.DicoObjectiveCustom[rand2] in listeCustom:
                pass
            else:
                listeCustom.append(BuildFromScratch.DicoObjectiveCustom[rand2])

        if custom == 1:
            self.superFlag += str(1) + ":" + listeCustom[custom]
        else:
            for i in range(custom):
                self.superFlag += str(i + 1) + ":"
                self.superFlag += listeCustom[i]

                if i + 1 != len(listeCustom):
                    self.superFlag += "/"
                else:
                    pass

    def randomObjective(self, random):

        if self.superFlag == "Onone":
            self.superFlag = "O"
        else:
            self.superFlag += "/"

        self.superFlag += "random:" + str(random)

    def rewardObjective(self, reward):
        if reward == 1:
            self.superFlag += "/win:crystal"
        else:
            self.superFlag += "/win:game"

    # Objets Clés
    def randKeyItem(self):
        randkey = randint(0, 1)
        listeKey = []

        if randkey == 0:
            self.superFlag += BuildFromScratch.DicoPrefixe[1] + "vanilla"
        else:
            self.superFlag += BuildFromScratch.DicoPrefixe[1] + "main"
            cleAlea = randint(0, 3)
            if cleAlea == 0:
                pass
            else:
                while len(listeKey) != cleAlea:
                    rand2 = randint(1, 3)
                    if rand2 == 3:
                        rand2 = randint(1, 30)
                        if rand2 != 3:
                            rand2 = randint(1, 2)

                    if BuildFromScratch.DicoKeyItem[rand2] not in listeKey:
                        listeKey.append(BuildFromScratch.DicoKeyItem[rand2])

                for i in listeKey:
                    self.superFlag += "/" + i

    # Options Pass
    def randPass(self):
        aleaPass = randint(0, 3)
        listePass = []
        self.superFlag += BuildFromScratch.DicoPrefixe[2]

        if aleaPass == 0:
            self.superFlag += "none"
        elif aleaPass == 3:
            for i in range(1, 3):
                listePass.append(BuildFromScratch.DicoPass[i])
        else:
            while len(listePass) != aleaPass:
                rand2 = randint(1, 3)
                if rand2 == 3:
                    rand3 = randint(1, 10)
                    if rand3 == 9:
                        listePass.append(BuildFromScratch.DicoPass[rand2])
                else:
                    if BuildFromScratch.DicoPass[rand2] not in listePass:
                        listePass.append(BuildFromScratch.DicoPass[rand2])

        for i in range(len(listePass)):
            if i != len(listePass) - 1:
                self.superFlag += listePass[i] + "/"
            else:
                self.superFlag += listePass[i]

    # Options personnages
    def randCharacter(self):
        listeSpell = []

        charRand = randint(1, 3)
        self.superFlag += BuildFromScratch.DicoPrefixe[3] + BuildFromScratch.DicoCharRand[charRand]
        if charRand != 3:
            charRand = randint(1, 2)
            if charRand == 2:
                self.superFlag += "/maybe"

        chooseStartChar = randint(0, 12)
        if chooseStartChar != 0:
            self.superFlag += "/" + BuildFromScratch.DicoStartChar[chooseStartChar]

        chooseSpell = randint(0, 4)
        if chooseSpell != 0:
            while len(listeSpell) != chooseSpell:
                rand2 = randint(1, 5)
                if BuildFromScratch.DicoCharSpell[rand2] not in listeSpell:
                    listeSpell.append(BuildFromScratch.DicoCharSpell[rand2])

            for i in listeSpell:
                self.superFlag += "/" + i

        permadeath = randint(1, 10)
        if permadeath == 3:
            self.superFlag += "/" + "permadeath"

    # Options Trésors
    def randTreasure(self):
        self.superFlag += BuildFromScratch.DicoPrefixe[4]
        aleatresor = randint(1, 5)
        self.superFlag += BuildFromScratch.DicoTreasure[aleatresor]

        aleatresor = randint(0, 3)
        if aleatresor == 3:
            self.superFlag += "/" + BuildFromScratch.DicoTreasureOption[1]
            self.superFlag += "/" + BuildFromScratch.DicoTreasureOption[2]
        elif aleatresor == 0:
            pass
        else:
            self.superFlag += "/" + BuildFromScratch.DicoTreasureOption[aleatresor]

    # Options Magasins
    def randShop(self):
        listeShop = []
        self.superFlag += BuildFromScratch.DicoPrefixe[5]

        aleaShop = randint(1, 6)
        self.superFlag += BuildFromScratch.DicoShop[aleaShop]

        aleaShop = randint(0, 5)
        if aleaShop != 0:
            while len(listeShop) != aleaShop:
                rand2 = randint(1, 5)
                if BuildFromScratch.DicoShopOption[rand2] not in listeShop:
                    listeShop.append(BuildFromScratch.DicoShopOption[rand2])

            for i in listeShop:
                self.superFlag += "/" + i

    # Options Boss
    def randBoss(self):
        self.superFlag += BuildFromScratch.DicoPrefixe[6]

        aleaBoss = randint(1, 2)
        self.superFlag += BuildFromScratch.DicoBoss[aleaBoss]

        aleaBoss = randint(0, 1)
        if aleaBoss == 1:
            self.superFlag += "/alt:gauntlet"

        aleaBoss = randint(0, 2)
        if aleaBoss != 0:
            self.superFlag += "/" + BuildFromScratch.DicoWyvern[aleaBoss]

    # Options Challenges
    def randChallenge(self):
        listeChal = []
        self.superFlag += BuildFromScratch.DicoPrefixe[7]

        aleaChallenge = randint(0, 3)
        if aleaChallenge == 3:
            aleaChallenge2 = randint(0, 50)
            if aleaChallenge2 != 42:
                aleaChallenge = randint(1, 2)

        if aleaChallenge == 0:
            self.superFlag += "none"
        else:
            while len(listeChal) != aleaChallenge:
                rand2 = randint(1, 3)
                if rand2 == 3:
                    rand3 = randint(1, 50)
                    if rand3 == 17:
                        listeChal.append(BuildFromScratch.DicoChallenge[3])
                else:
                    if BuildFromScratch.DicoChallenge[rand2] not in listeChal:
                        listeChal.append(BuildFromScratch.DicoChallenge[rand2])

        for i in range(len(listeChal)):
            if i != len(listeChal) - 1:
                self.superFlag += listeChal[i] + "/"
            else:
                self.superFlag += listeChal[i]

    # Options Combats
    def randEncounter(self):
        self.superFlag += BuildFromScratch.DicoPrefixe[8]

        aleaEnc = randint(0, 60)
        if aleaEnc == 19:
            self.superFlag += "/" + BuildFromScratch.DicoEncounterToggle[1]
        elif aleaEnc == 32:
            self.superFlag += "/" + BuildFromScratch.DicoEncounterToggle[2]
        elif aleaEnc == 42:
            self.superFlag += "/" + BuildFromScratch.DicoEncounterToggle[3]
        else:
            pass

        aleaEncTabl = randint(0, 30)
        if aleaEncTabl == 1:
            self.superFlag += "/" + BuildFromScratch.DicoEncounterDrop[1]
        elif aleaEncTabl == 2:
            self.superFlag += "/" + BuildFromScratch.DicoEncounterDrop[2]
        else:
            pass

    # Options Glitchs
    def randGlitch(self):
        listeGlitch = []
        self.superFlag += BuildFromScratch.DicoPrefixe[9]

        aleaGlitch = randint(0, 5)
        if aleaGlitch == 0:
            self.superFlag += "none"
        else:
            while len(listeGlitch) != aleaGlitch:
                rand2 = randint(1, 5)
                if BuildFromScratch.DicoGlitch[rand2] not in listeGlitch:
                    listeGlitch.append(BuildFromScratch.DicoGlitch[rand2])

            for i in range(len(listeGlitch)):
                if i != len(listeGlitch) - 1:
                    self.superFlag += listeGlitch[i] + "/"
                else:
                    self.superFlag += listeGlitch[i]

    # Options Autres
    def randOther(self):
        aleaKit = randint(1, 4)
        self.superFlag += " -kit:" + BuildFromScratch.DicoOtherStarter[aleaKit]

        aleaAda = randint(0, 10)
        if aleaAda == 8:
            self.superFlag += " " + BuildFromScratch.DicoOther[1]

        aleaSpoon = randint(0, 10)
        if aleaSpoon == 4:
            self.superFlag += " " + BuildFromScratch.DicoOther[2]

    # Crée un seed à partir de rien
    def scratch(self):
        self.superFlag = ""
        self.randObjectifFlag()
        self.randKeyItem()
        self.randPass()
        self.randCharacter()
        self.randTreasure()
        self.randShop()
        self.randBoss()
        self.randChallenge()
        self.randEncounter()
        self.randGlitch()
        self.randOther()

        self.titre.set("BON COURAGE")
        self.copierFlag(self.superFlag)
        self.imageMenu(12)

        if self.web is False:
            webbrowser.open("http://ff4fe.com/make")
            self.web = True


root = Tk()
root.title("Slackh's FF4 Flag Randomizer")
Dice(root).pack()

root.mainloop()
