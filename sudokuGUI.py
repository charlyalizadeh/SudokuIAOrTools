import tkinter as tk
import tkinter.font as tkFont

class Sudoku:
    def __init__(self):
        #----WINDOW----
        self.window = tk.Tk()
        self.window.geometry("700x400")
        for i in range(3):
            self.window.grid_columnconfigure(i,weight = 1)
            self.window.grid_rowconfigure(i,weight = 1)
        self.window.grid_columnconfigure(3,weight = 2)
        

        #----MAIN FRAMES : the big squares----
        self.mainFrames = []
        iColumn = 0
        iRow = 0
        for i in range(9):
            self.mainFrames.append(tk.Frame(self.window,bd=1,bg='black'))
            self.mainFrames[i].grid(column = iColumn, row = iRow,sticky = 'WESN')
            if iColumn == 2:
                iColumn=0
                iRow+=1
            else:
                iColumn+=1

        #----SECOND FRAMES & LABELS : the little squares----
        self.numbers = []
        self.secondFrames = []
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        for i in range(9):
            for j in range(3):
                self.mainFrames[i].grid_rowconfigure(j,weight = 1)
                self.mainFrames[i].grid_columnconfigure(j,weight = 1)
            iColumn = 0
            iRow = 0
            index = 0
            self.secondFrames.append([])
            self.numbers.append([])
            for j in range(9):
                self.secondFrames[i].append(tk.Frame(self.mainFrames[i],bd = 1,bg='black'))
                self.numbers[i].append(tk.Label(self.secondFrames[i][index],text = ' ',bg='white',fg='black',bd=4,font = fontStyle))
                self.secondFrames[i][index].grid(column=iColumn,row = iRow,sticky='WESN')
                self.numbers[i][index].pack(fill='both',expand=True)
                index+=1
                if iColumn==2:
                    iColumn=0
                    iRow+=1
                else:
                    iColumn+=1
        fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        #----BUTTON SOLVE, GENERATE, CLEAR----
        self.menuFrame = tk.Frame(self.window,bg = 'black')
        self.menuFrame.grid(row = 0,rowspan = 3,column = 3,sticky = 'WESN')
        for i in range(3):
            self.menuFrame.grid_rowconfigure(i,weight=1)
        self.menuFrame.grid_columnconfigure(0,weight=1)

        self.buttonSolve = tk.Button(self.menuFrame,text = 'SOLVE',  font = fontStyle,fg = 'white',bd=1,activebackground= 'black', relief=tk.FLAT,bg='black')
        self.buttonSolve.grid(row=0)

        self.generateFrame = tk.Frame(self.menuFrame,bg = 'black')
        self.generateFrame.grid(row = 1,sticky = 'WESN')
        self.buttonGenerate = tk.Button(self.generateFrame,text = 'GENERATE', font = fontStyle,fg = 'white',bd=1,activebackground= 'black', relief=tk.FLAT,bg='black')
        self.buttonGenerate.grid(column=0)

        self.buttonClear = tk.Button(self.menuFrame,bd=1,text = 'CLEAR',  font = fontStyle,justify = 'center',fg = 'white',activebackground= 'black', relief=tk.FLAT,bg='black')
        self.buttonClear.grid(row = 2)

        #----DIFFICULTY---
        self.difficultyFrame = tk.Frame(self.generateFrame,bg = 'black')
        self.difficultyFrame.grid(row = 0,column = 1,sticky = 'WESN')
        for i in range(5):
            self.difficultyFrame.rowconfigure(i,weight = 1)
        self.buttonDifficulty = []
        index = 0
        for i in ['VERY EASY','EASY','NORMAL','HARD','VERY HARD']:
            #self.images['button'+i] = tk.PhotoImage(file='image/'+i+'.gif')
            self.buttonDifficulty.append(tk.Button(self.difficultyFrame,text = i, fg = 'white', font = fontStyle,bg = 'black',relief=tk.FLAT,activebackground= 'black'))
            self.buttonDifficulty[index].grid(row = index)
            index+=1

    def __setitem__(self,index,value):
        if isinstance(index,str):
            type = index 
            for i in range(9):
                for j in range(9):
                    x,y = self.translateCoordinates(i,j)
                    self.numbers[x][y][type] = value[i*9+j]
        else:
            i,j = self.translateCoordinates(index[0],index[1])
            type = index[2]
            self.numbers[i][j][type] = value

    def __getitem__(self,index):
        i,j = self.translateCoordinates(index[0],index[1])
        type = index[2]
        return self.numbers[i][j][type] 

    def translateCoordinates(self,indexI,indexJ):
        partI = 0 if indexI<=2 else 1 if indexI<=5 else 2
        partJ = 0 if indexJ<=2 else 1 if indexJ<=5 else 2
        part = partJ+partI*3
        index = indexJ%3 + indexI%3*3
        return part,index

    def clearBg(self,color = 'white'):
        for i in range(9):
            for j in range(9):
                self.numbers[i][j].config(bg = color)

    def clearFg(self,color = 'black'):
        for i in range(9):
            for j in range(9):
                self.numbers[i][j].config(fg = color)

    def start(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()

