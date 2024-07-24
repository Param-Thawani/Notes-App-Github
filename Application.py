#Param Thawani
import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Combine the script directory and the file name to get the full path
file_path = os.path.join(script_dir, "NotesStorage.txt")
# Notes class
class Notes:
    def __init__(self, name, text):
        self.text = text
        self.name = name
    def getName(self):
        return self.name   
    def getText(self):
        return self.text   
    def setName(self, name):
        self.name = name
    def setText(self, text):
        self.text = text
#class to store notes across sessions
class notesStorage:
    def __init__(self,filePath):
        self.filePath = filePath
    def saveNotes(self,Allnotes):
        self.Allnotes = Allnotes
        notesAsString = []
        for y in Allnotes:
            notesAsString.append(y.getName())
            notesAsString.append(y.getText())
        notesAsString
        with open (self.filePath,'w') as file:
            fileNumb = 1
            for i in notesAsString:
                file.write(i)
                if(fileNumb!=len(notesAsString)):
                    file.write(" asdf ")
                fileNumb += 1
            file.close()
    def loadNotes(self):
        try:
            with open(file_path,"r") as file:
                var = file.read()
        except FileNotFoundError:
            return -1
        stringsAsNotes = []
        stringsAsNotes = var.split(" asdf ")
        count = 1
        notesAsStrings = []
        for j in stringsAsNotes:
            if(count%2==0):
                note = Notes(stringsAsNotes[count-2], j)
                notesAsStrings.append(note)
            count+=1
        return notesAsStrings

# User Interface class
class UI:
    def textInput(self):
        text = input()
        text+= "\n"
        while text.find("asdf")==-1:
            text+=input()
            text+= "\n"
        text = text.replace("asdf\n", "")
        return text
    def __init__(self):
        self.allNotes = []
    def textBased(self):
        store = notesStorage(file_path)
        if(store.loadNotes()!=-1):
            self.allNotes = store.loadNotes()
        print("welcome new user!")
        answer = int(input("to write a new note type [1], to edit previous notes type [2], to exit application type [0] "))
        while answer != 0:
            if(answer == 1):
                name = input("what would you like to name the note? ")
                print("you may now start typing the note, type [a][s][d][f][enter] to finish the note:")
                text = self.textInput()
                note = Notes(name, text)
                self.allNotes.append(note)
            elif(answer == 2):
                if(len(self.allNotes)!=0):
                    noteNumb = 1
                    for i in self.allNotes:
                        print("Note "+str(noteNumb)+" [ Name: "+i.getName()+" ]")
                        noteNumb+=1
                    selectedNote = int(input("which note would you like to change/read? "))-1
                    while(selectedNote > len(self.allNotes)-1 or selectedNote < 0):
                        print("please try again by entering a note address that exists from the following:")
                        noteNumb = 1
                        for i in self.allNotes:
                            print("Note "+str(noteNumb)+" [ Name: "+i.getName()+" ]")
                            noteNumb+=1
                        selectedNote = int(input("which note would you like to change/read? "))-1
                    whatIsChanging = int(input(" if you would like to change the name of the note, type [1] \n if you would like to change the contents of the note, type [2] \n if you would like to read the contents of the note, type [3] \n if you would like to select another note, type [4] \n if you would like to delete this note, type [5] \n if you would like to exit to the main menu, type [0] \n"))
                    noteName = "[ " + self.allNotes[selectedNote].getName() + " ]"
                    while(whatIsChanging != 0):
                        if(whatIsChanging == 1 ):
                            newName = input("what would you like to rename "+noteName+" to? ")
                            self.allNotes[selectedNote].setName(newName)
                            print(noteName+" is now named [ "+ self.allNotes[selectedNote].getName()+" ]")
                        elif(whatIsChanging == 2):
                            print("type what you would like to replace the contents of "+noteName+" to below, type [a][s][d][f][enter] to finish the note:")
                            newText = self.textInput()
                            self.allNotes[selectedNote].setText(newText)
                        elif(whatIsChanging == 3):
                            print("the contents of "+noteName+" are as follows:")
                            print("\n"+self.allNotes[selectedNote].getText()+"\n")
                        elif(whatIsChanging == 5):
                            deleteAsk = input("are you sure you would like to delete note "+str(selectedNote+1)+" ? y/n ")
                            if(deleteAsk == "y"):
                                self.allNotes.remove(self.allNotes[selectedNote])
                                print(noteName+" has been deleted succesfully")
                            elif(deleteAsk == "n"):
                                print(noteName+" has not been deleted")
                        if(len(self.allNotes)!=0):
                            noteNumb = 1
                            for i in self.allNotes:
                                print("Note "+str(noteNumb)+" [ Name: "+i.getName()+" ]")
                                noteNumb+=1
                            selectedNote = int(input("which note would you like to change/read? "))-1
                            whatIsChanging = int(input(" if you would like to change the name of the note, type [1] \n if you would like to change the contents of the note, type [2] \n if you would like to read the contents of the note, type [3] \n if you would like to select another note, type [4] \n if you would like to delete this note, type [5] \n if you would like to exit to the main menu, type [0] \n"))
                        else:
                            whatIsChanging = 0
                else:
                    print("sorry, you have not written any notes previously, please select another option: ")
            elif(answer !=0):
                print("please try again:")
            if(answer!=0):
                answer = int(input("to write a new note type [1], to edit previous notes type [2], to exit application type [0] "))
        store.saveNotes(self.allNotes)
        exit()
# main function
def main():
    ui= UI()
    ui.textBased()
main()