from tkinter import*
from tkinter import messagebox as m_box

geometryX = 340
geometryY = 200

def raise_frame(frame):
    frame.tkraise()

class FormulaCalculator:
    def __init__(self, master):
        master.title("Newton's 2nd Law Calculator")
        master.configure(background="#ecd59f")
        master.minsize(geometryX, geometryY)
        master.maxsize(geometryX, geometryY)
        
        self.speed = Frame(master, bg='#ecd59f')
        self.weight = Frame(master, bg='#ecd59f')
        self.momentum = Frame(master, bg='#ecd59f')
        self.force = Frame(master, bg='#ecd59f')
        
        for frame in (self.speed, self.force, self.weight, self.momentum):
            frame.grid(row=0, column=0, sticky='news')

        # ==============================================================================================================
        # ======================= Speed Menu Layout ====================================================================
        # ==============================================================================================================

        # Labels
        self.spTitleLabel = Label(self.speed, text="Speed", font=("Helvetica", 10, 'bold'), bg='#ecd59f').grid(row=0, column=1)
        self.spDistanceLabel = Label(self.speed, text="Distance (m): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=1, column=0)
        self.spTimeLabel = Label(self.speed, text="Time (s): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=2, column=0)
        self.spSpeedLabel = Label(self.speed, text="Speed (m/s):  ", font=("Helvetica", 9), bg='#ecd59f').grid(row=3, column=0)

        # Entry boxes
        self.spDistance = Entry(self.speed, bg='#d1d1d1')
        self.spTime = Entry(self.speed, bg='#d1d1d1')
        self.spSpeed = Entry(self.speed, bg='#d1d1d1')

        # Packing the entry boxes into the frame
        self.spDistance.grid(row=1, column=1)
        self.spTime.grid(row=2, column=1)
        self.spSpeed.grid(row=3, column=1)

        # Button 
        self.spConvertSpeed = Button(self.speed, text="Calculate Speed", font=("Helvetica", 9), command=self.speedCalcSpeed).grid(row=4, column=1)
        self.spConvertDistance = Button(self.speed, text="Calculate Distance", font=("Helvetica", 9), command=self.speedCalcDist).grid(row=5, column=1)
        self.spConvertTime = Button(self.speed, text="Calculate Time", font=("Helvetica", 9), command=self.speedCalcTime).grid(row=6, column=1)
        self.spClear = Button(self.speed, text="Clear", font=("Helvetica", 9),command=self.ClearSpeed).grid(row=5, column=0)

        # ==============================================================================================================
        # ======================= Force Menu Layout ====================================================================
        # ==============================================================================================================
        
        # Labels
        self.foTitleLabel = Label(self.force, text="Force", font=("Helvetica", 10, 'bold'), bg='#ecd59f').grid(row=0, column=1)
        self.foAcceleration = Label(self.force, text="Acceleration (m/s²): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=1, column=0)
        self.foMassLabel = Label(self.force, text="Mass (kg): ", font=("Helvetica", 9),bg='#ecd59f').grid(row=2, sticky="e")
        self.foForceLabel = Label(self.force, text="Force (N): ", font=("Helvetica", 9),bg='#ecd59f').grid(row=3, sticky="e")

        # Entry boxes
        self.foAcceleration = Entry(self.force, bg='#d1d1d1')
        self.foMass = Entry(self.force, bg='#d1d1d1')
        self.foForce = Entry(self.force, bg='#d1d1d1')

        # Entry pack
        self.foAcceleration.grid(row=1, column=1)
        self.foMass.grid(row=2, column=1)
        self.foForce.grid(row=3, column=1)

        # Buttons
        self.foConvertAcceleration = Button(self.force, text="Calculate Acceleration", font=("Helvetica", 9),command=self.foCalcAcceleration)
        self.foConvertMass = Button(self.force, text="Calculate Mass", font=("Helvetica", 9),command=self.foCalcMass)
        self.foConvertForce = Button(self.force, text="Calculate Force", font=("Helvetica", 9),command=self.foCalcForce)
        self.foClear = Button(self.force, text="Clear", font=("Helvetica", 9),command=self.ClearForce)

        self.foConvertAcceleration.grid(row=4, column=1)
        self.foConvertMass.grid(row=5, column=1)
        self.foConvertForce.grid(row=6, column=1)
        self.foClear.grid(row=5, column=0)

        # ==============================================================================================================
        # ======================= Weight Menu Layout ===================================================================
        # ==============================================================================================================

        # Labels
        self.weTitleLabel = Label(self.weight, text="Earth's Gravity Constant", font=("Helvetica", 10, 'bold'), bg='#ecd59f').grid(row=0, column=1)
        self.weGravityLabel = Label(self.weight, text="Gravity (N/kg): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=1, column=0)
        self.weMassLabel = Label(self.weight, text="Mass (kg): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=2, column=0)
        self.weWeightLabel = Label(self.weight, text="Weight (N): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=3, column=0)

        # Entry Boxes
        self.weGravity = Entry(self.weight, bg='#d1d1d1')
        self.weMass = Entry(self.weight, bg='#d1d1d1')
        self.weWeight = Entry(self.weight, bg='#d1d1d1')

        # Entry pack
        self.weGravity.grid(row=1, column=1)
        self.weMass.grid(row=2, column=1)
        self.weWeight.grid(row=3, column=1)
        
        # Buttons
        self.weConvertGravity = Button(self.weight, text="Calculate Gravity", font=("Helvetica", 9), command=self.weCalcGravity)
        self.weConvertMass = Button(self.weight, text="Calculate Mass", font=("Helvetica", 9), command=self.weCalcMass)
        self.weConvertWeight = Button(self.weight, text="Calculate Weight", font=("Helvetica", 9), command=self.weCalcWeight)
        self.weClear = Button(self.weight, text="Clear", font=("Helvetica", 9),command=self.ClearWeight)
        
        self.weConvertGravity.grid(row=4, column=1)
        self.weConvertMass.grid(row=5, column=1)
        self.weConvertWeight.grid(row=6, column=1)
        self.weClear.grid(row=5, column=0)

        # ==============================================================================================================
        # ======================= Momentum Menu Layout =================================================================
        # ==============================================================================================================

        # Labels
        self.moTitleLabel = Label(self.momentum, text="Momentum", font=("Helvetica", 10, 'bold'), bg='#ecd59f').grid(row=0, column=1)
        self.moVelocityLabel = Label(self.momentum, text="Velocity (m/s): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=1, sticky="e")
        self.moMassLabel = Label(self.momentum, text="Mass (kg): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=2, sticky="e")
        self.moMomentumLabel = Label(self.momentum, text="Momentum (kg·m/s): ", font=("Helvetica", 9), bg='#ecd59f').grid(row=3, column=0)

        # Entry Boxes
        self.moVelocity = Entry(self.momentum, bg='#d1d1d1')
        self.moMass = Entry(self.momentum, bg='#d1d1d1')
        self.moMomentum = Entry(self.momentum, bg='#d1d1d1')

        # Entry pack
        self.moVelocity.grid(row=1, column=1)
        self.moMass.grid(row=2, column=1)
        self.moMomentum.grid(row=3, column=1)        

        # Buttons
        self.moConvertVelocity = Button(self.momentum, text="Calculate Velocity", font=("Helvetica", 9), command=self.moCalcVelocity)
        self.moConvertMass = Button(self.momentum, text="Calculate Mass", font=("Helvetica", 9), command=self.moCalcMass)
        self.moConvertMomentum = Button(self.momentum, text="Calculate Momentum", font=("Helvetica", 9), command=self.moCalcMomentum)
        self.moClear = Button(self.momentum, text="Clear", font=("Helvetica", 9),command=self.ClearMomentum)

        self.moConvertVelocity.grid(row=4, column=1)
        self.moConvertMass.grid(row=5, column=1)
        self.moConvertMomentum.grid(row=6, column=1)
        self.moClear.grid(row=5, column=0)

        # ==============================================================================================================
        # ========================= Menu bar Layout ====================================================================
        # ==============================================================================================================
        self.menubar = Menu(master)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=master.destroy)

        self.formulamenu = Menu(self.menubar, tearoff=0)
        self.formulamenu.add_radiobutton(label="Force", command=lambda: raise_frame(self.force))
        self.formulamenu.add_radiobutton(label="Weight", command=self.insertGravity)
        self.formulamenu.add_radiobutton(label="Momentum", command=lambda: raise_frame(self.momentum))

        self.insertmenu = Menu(self.menubar, tearoff=0)
        self.insertmenu.add_radiobutton(label="Speed", command=lambda: raise_frame(self.speed))

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_command(label="\u22EE")
        self.menubar.add_cascade(label="Forces Formula", menu=self.formulamenu)
        self.menubar.add_command(label="\u22EE")
        self.menubar.add_cascade(label="Other", menu=self.insertmenu)

        master.config(menu=self.menubar)

    # ============================ INSERT FUNCTIONS ====================================================================
    
    def insertGravity(self):
        raise_frame(self.weight)
        self.weGravity.delete(0, END)
        self.weGravity.insert(INSERT, "9.81")
    
    # ==================================================================================================================
    # ======================= Logical Processes ========================================================================
    # ==================================================================================================================
    
    #====== SPEED CALCULATIONS ======#
    
    def speedCalcSpeed(self):
        self._distance = float(self.spDistance.get())
        self._time = float(self.spTime.get())
    
        self.spSpeed.delete(0, END)
        self.spSpeed.insert(INSERT, str(self._distance / self._time))
    
    def speedCalcTime(self):
        self._distance = float(self.spDistance.get())
        self._speed = float(self.spSpeed.get())
    
        self.spTime.delete(0, END)
        self.spTime.insert(INSERT, str(self._distance / self._speed))
    
    def speedCalcDist(self):
        self._speed = float(self.spSpeed.get())
        self._time = float(self.spTime.get())
    
        self.spDistance.delete(0, END)
        self.spDistance.insert(INSERT, str(self._time * self._speed))
    
    #====== FORCE CALCULATIONS ======#
    
    def foCalcAcceleration(self):
        self._mass = float(self.foMass.get())
        self._force = float(self.foForce.get())    
        
        self.foAcceleration.delete(0, END)
        self.foAcceleration.insert(INSERT, str(self._force / self._mass))

    def foCalcMass(self):
        self._acceleration = float(self.foAcceleration.get())
        self._force = float(self.foForce.get())
    
        self.foMass.delete(0, END)
        self.foMass.insert(INSERT, str(self._force / self._acceleration))
    
    def foCalcForce(self):
        self._mass = float(self.foMass.get())
        self._acceleration = float(self.foAcceleration.get())
    
        self.foForce.delete(0, END)
        self.foForce.insert(INSERT, str(self._mass * self._acceleration))
    
    #====== WEIGHT CALCULATIONS ======#
    
    def weCalcGravity(self):
        self._mass = float(self.weMass.get())
        self._weight = float(self.weWeight.get())
    
        self.weGravity.delete(0, END)
        self.weGravity.insert(INSERT, str(self._weight / self._mass))
    
    def weCalcMass(self):
        self._gravity = float(self.weGravity.get())
        self._weight = float(self.weWeight.get())
    
        self.weMass.delete(0, END)
        self.weMass.insert(INSERT, str(self._weight / self._gravity))
    
    def weCalcWeight(self):
        self._gravity = float(self.weGravity.get())
        self._mass = float(self.weMass.get())
    
        self.weWeight.delete(0, END)
        self.weWeight.insert(INSERT, str(self._mass * self._gravity))
    
    #====== MOMENTUM CALCULATIONS ======#
    
    def moCalcVelocity(self):
        self._momentum = float(self.moMomentum.get())
        self._mass = float(self.moMass.get())
    
        self.moVelocity.delete(0, END)
        self.moVelocity.insert(INSERT, str(self._momentum / self._mass))
    
    def moCalcMass(self):
        self._momentum = float(self.moMomentum.get())
        self._velocity = float(self.moVelocity.get())
    
        self.moMass.delete(0, END)
        self.moMass.insert(INSERT, str(self._momentum / self._velocity))
    
    def moCalcMomentum(self):
        self._mass = float(self.moMass.get())
        self._velocity = float(self.moVelocity.get())
    
        self.moMomentum.delete(0, END)
        self.moMomentum.insert(INSERT, str(self._mass * self._velocity))

    #====== CLEAR FUNCTION ======#

    def setEntry(self, where, what):
        if where.get():
            where.delete(0, len(where.get()))
            where.insert(0, str(what))
        
    def ClearForce(self):
        if self.foAcceleration.get() == '' and self.foForce.get() == '' and self.foMass.get() == '':
            m_box.showerror("Error", "Already on a Cleared State! Please put a number!")                
        else:
            self.setEntry(self.foMass, '')
            self.setEntry(self.foForce, '')
            self.setEntry(self.foAcceleration, '')

    def ClearSpeed(self):
        if self.spDistance.get() == '' and self.spTime.get() == '' and self.spSpeed.get() == '':
            m_box.showerror("Error", "Already on a Cleared State! Please put a number!")                
        else:
            self.setEntry(self.spDistance, '')
            self.setEntry(self.spTime, '')
            self.setEntry(self.spSpeed, '')

    def ClearWeight(self):
        if self.weMass.get() == '' and self.weWeight.get() == '':
            m_box.showerror("Error", "Already on a Cleared State! Please put a number!")                
        else:
            self.setEntry(self.weMass, '')
            self.setEntry(self.weWeight, '')

    def ClearMomentum(self):
        if self.moVelocity.get() == '' and self.moMass.get() == '' and self.moMomentum.get() == '':
            m_box.showerror("Error", "Already on a Cleared State! Please put a number!")                
        else:
            self.setEntry(self.moVelocity, '')
            self.setEntry(self.moMass, '')
            self.setEntry(self.moMomentum, '')


root = Tk()
main = FormulaCalculator(root)
root.mainloop()
