# IDY Launcher
# Developed by IK4IDY - Alessio Vacondio (2019)
# Version 1.0 Base
#
# DVBSDR - Developed by F5OEO (Saint Evariste)
#
import Tkinter as tk
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
window = tk.Tk()  # type: Tk

Frv = tk.IntVar()
Mdv = tk.IntVar()
Fcv = tk.IntVar()
Csv = tk.IntVar()
Fmv = tk.IntVar()
Plv = tk.IntVar()
Usv = tk.IntVar()
Cav = tk.IntVar()
Rtv = tk.IntVar()
Cdv = tk.IntVar()

# Parameter DVBSDR FILE


# Frequency List
FrqList = ("2406.000",  # 1
           "2405.250",  # 2
           "2405.750",  # 3
           "2407.750",  # 4
           "2408.250",  # 5
           "2408.750",  # 6
           "2409.250",  # 7
           "2409.750",  # 8
           "2407.625",  # 9
           "2407.875",  # 10
           "2408.125",  # 11
           "2408.375",  # 12
           "2408.625",  # 13
           "2408.875",  # 14
           "2409.125",  # 15
           "2409.375",  # 16
           "2409.625",  # 17
           "2409.875")  # 18
# Symbolrate List
RateList = ("2000",  # 1
            "1000",  # 2
            "1000",  # 3
            "333",  # 4
            "333",  # 5
            "333",  # 6
            "333",  # 7
            "333",  # 8
            "125",  # 9
            "125",  # 10
            "125",  # 11
            "125",  # 12
            "125",  # 13
            "125",  # 14
            "125",  # 15
            "125",  # 16
            "125",  # 17
            "125")  # 18

# Slot (It's not a parameter, useful for display)
SlotList = ("1",  # 1
            "1",  # 2
            "2",  # 3
            "1",  # 4
            "2",  # 5
            "3",  # 6
            "4",  # 7
            "5",  # 8
            "1",  # 9
            "2",  # 10
            "3",  # 11
            "4",  # 12
            "5",  # 13
            "6",  # 14
            "7",  # 15
            "8",  # 16
            "9",  # 17
            "10")  # 18

# Constellation
ConstList = ("QPSK",
             "8PSK",
             "16PSK",
             "32PSK")

# Mode
CodeList = ("H264",
            "H265")

# Mode
ModeList = ("DVBS",
            "DVBS2")

# FEC
FecList = ("1/4",
           "1/3",
           "2/5",
           "1/2",
           "3/5",
           "2/3",
           "3/4",
           "4/5",
           "5/6",
           "8/9",
           "9/10")

# Frame
FrameList = ("$SHORT_FRAME",
             "$LONG_FRAME")

# Pilots
PilotList = ("$WITH_PILOTS",
             "$WITHOUT_PILOTS")

# USample
SampList = ("1",
            "2",
            "4")

# Ratio
RatiList = ("4:3",
            "16:9")

def clrfld():
    FR.delete(0, 'end')
    SR.delete(0, 'end')
    VID.delete(0, 'end')
    GOP.delete(0, 'end')
    PP.delete(0, 'end')
    RES.delete(0, 'end')


# Rate and frequency Function
def sel():
    print("valore :" + str(Frv.get()))

    FR.delete(0, 'end')
    FR.insert(0, FrqList[Frv.get()])

    SR.delete(0, 'end')
    SR.insert(0, RateList[Frv.get()])



def opnfle(NameFl):
    fl = open(NameFl, "r")
    clrfld()
    FR.insert(0, fl.readline().replace("\n", ""))   # Frequenza
    SR.insert(0, fl.readline().replace("\n", ""))   # Symbol rate
    VID.insert(0, fl.readline().replace("\n", ""))  # Video FPS
    GOP.insert(0, fl.readline().replace("\n", ""))  # Group of Pictures
    PP.insert(0, fl.readline().replace("\n", ""))   # PCR_PTS
    Frv.set(int(fl.readline()))                       # Freq./Speed
    Csv.set(int(fl.readline()))                       # Constellation
    Mdv.set(int(fl.readline()))                       # Mode
    Cav.set(int(fl.readline()))                       # Calibrate
    Fmv.set(int(fl.readline()))                       # Frame
    Rtv.set(int(fl.readline()))                       # Ratio
    Plv.set(int(fl.readline()))                       # Pilots
    Fcv.set(int(fl.readline()))                       # FEC
    Usv.set(int(fl.readline()))                       # Usample
    Cdv.set(int(fl.readline()))                       # Codec
    RES.insert(0, fl.readline().replace("\n", ""))    # Video Res(x)
    PWR.set(int(fl.readline()))                       # Power
    fl.close()


# Open Paramaters
def OpenBtFn():
    print("Open Button")
    NameFl = askopenfilename()
    print(NameFl)
    opnfle(NameFl)



# Save Parameters
def SaveBtFn():
    print("Save Button")
    NameFl = asksaveasfilename()
    print(NameFl)
    fl = open(NameFl, "w+")
    fl.write(FR.get() + "\n")  # Frequenza
    fl.write(SR.get() + "\n")  # Symbol rate
    fl.write(VID.get() + "\n")  # Video FPS
    fl.write(GOP.get() + "\n")  # Group of Pictures
    fl.write(PP.get() + "\n")  # PCR_PTS
    fl.write(str(Frv.get()) + "\n")  # Freq./Speed
    fl.write(str(Csv.get()) + "\n")  # Constellation
    fl.write(str(Mdv.get()) + "\n")  # Mode
    fl.write(str(Cav.get()) + "\n")  # Calibrate
    fl.write(str(Fmv.get()) + "\n")  # Frame
    fl.write(str(Rtv.get()) + "\n")  # Ratio
    fl.write(str(Plv.get()) + "\n")  # Pilots
    fl.write(str(Fcv.get()) + "\n")  # FEC
    fl.write(str(Usv.get()) + "\n")  # Usample
    fl.write(str(Cdv.get()) + "\n")  # Codec
    fl.write(RES.get() + "\n")       # Video Res(x)
    fl.write(str(PWR.get()) + "\n")  # Power
    fl.close()


# Start TX !
def TranBtFn():
    print("TX Button")
    fl = open("/home/user/dvbsdr/scripts/jetson_nano.sh", "r")
    fl1 = open("/home/user/dvbsdr/scripts/jetson_nano_l.sh", "w")
    for line in fl:
        if "FREQ=" in line:
           line = "FREQ=" + FR.get() + "\n"
        elif "SYMBOLRATE=" in line:
            line = "SYMBOLRATE=" + SR.get() + "\n"
        elif "FECNUM=" in line:
            strf = FecList[Fcv.get()-1]
            line = "FECNUM=" + strf[0] + "\n"
        elif "FECDEN=" in line:
            strf = FecList[Fcv.get()-1]
            line = "FECDEN=" + strf[2:3] + "\n"
        elif "MODE=" in line:
            line = "MODE=" + ModeList[Mdv.get()-1] + "\n"
        elif "CONSTELLATION=" in line:
            line = "CONSTELLATION=" + ConstList[Csv.get()-1] + "\n"
        elif "GAIN=" in line and "DGAIN" not in line:
            gn = PWR.get()
            gnp = gn / 100.00
            line = "GAIN=" + str(gnp) + "\n"
        elif "TYPE_FRAME=" in line:
            line = "TYPE_FRAME=" + FrameList[Fmv.get()-1] + "\n"
        elif "PILOTS=" in line:
            line = "PILOTS=" + PilotList[Plv.get()-1] + "\n"
        elif "CALIBRATE_BEFORE_TX=" in line:
            line = "CALIBRATE_BEFORE_TX=" + str(Cav.get()) + "\n"
        elif "RATIO=" in line:
            line = "RATIO=" + RatiList[Rtv.get()-1] + "\n"
        elif "VIDEO_FPS=" in line:
            line = "VIDEO_FPS=" + VID.get() + "\n"
        elif "VIDEO_GOP=" in line:
            line = "VIDEO_GOP=" + GOP.get() + "\n"
        elif "PCR_PTS=" in line:
            line = "PCR_PTS=" + PP.get() + "\n"
        elif "CODEC=" in line:
            line = "CODEC=" + CodeList[Cdv.get()-1] + "\n"
        elif "UPSAMPLE=" in line:
            line = "UPSAMPLE=" + SampList[Usv.get()-1] + "\n"
        fl1.write(line)
    fl1.close()
    fl.close()

window.geometry("600x600")
window.resizable(0, 0)
window.title("DVBSDR-IDY LAUNCH")

# 1 =============================================================================================================
txtFR = "SR/Frequency/Slot"
txtFR_out = tk.Label(window, text=txtFR, justify=tk.LEFT, padx=20)
txtFR_out.grid(row=0, column=0)

# 2 =============================================================================================================
FR = ""
FR = tk.Entry(window, justify="center", width=8)
FR.grid(row=19, column=0)

tk.Radiobutton(window, text=RateList[0] + " KS-" + FrqList[0] + "-" + SlotList[0], padx=20, variable=Frv, value=0,
               command=sel).grid(row=1, sticky="W")
tk.Radiobutton(window, text=RateList[1] + " KS-" + FrqList[1] + "-" + SlotList[1], padx=20, variable=Frv, value=1,
               command=sel).grid(row=2, sticky="W")
tk.Radiobutton(window, text=RateList[2] + " KS-" + FrqList[2] + "-" + SlotList[2], padx=20, variable=Frv, value=2,
               command=sel).grid(row=3, sticky="W")
tk.Radiobutton(window, text=RateList[3] + " KS-" + FrqList[3] + "-" + SlotList[3], padx=20, variable=Frv, value=3,
               command=sel).grid(row=4, sticky="W")
tk.Radiobutton(window, text=RateList[4] + " KS-" + FrqList[4] + "-" + SlotList[4], padx=20, variable=Frv, value=4,
               command=sel).grid(row=5, sticky="W")
tk.Radiobutton(window, text=RateList[5] + " KS-" + FrqList[5] + "-" + SlotList[5], padx=20, variable=Frv, value=5,
               command=sel).grid(row=6, sticky="W")
tk.Radiobutton(window, text=RateList[6] + " KS-" + FrqList[6] + "-" + SlotList[6], padx=20, variable=Frv, value=6,
               command=sel).grid(row=7, sticky="W")
tk.Radiobutton(window, text=RateList[7] + " KS-" + FrqList[7] + "-" + SlotList[7], padx=20, variable=Frv, value=7,
               command=sel).grid(row=8, sticky="W")
tk.Radiobutton(window, text=RateList[8] + " KS-" + FrqList[8] + "-" + SlotList[8], padx=20, variable=Frv, value=8,
               command=sel).grid(row=9, sticky="W")
tk.Radiobutton(window, text=RateList[8] + " KS-" + FrqList[9] + "-" + SlotList[9], padx=20, variable=Frv, value=9,
               command=sel).grid(row=10, sticky="W")
tk.Radiobutton(window, text=RateList[10] + " KS-" + FrqList[10] + "-" + SlotList[10], padx=20, variable=Frv, value=10,
               command=sel).grid(row=11, sticky="W")
tk.Radiobutton(window, text=RateList[11] + " KS-" + FrqList[11] + "-" + SlotList[11], padx=20, variable=Frv, value=11,
               command=sel).grid(row=12, sticky="W")
tk.Radiobutton(window, text=RateList[12] + " KS-" + FrqList[12] + "-" + SlotList[12], padx=20, variable=Frv, value=12,
               command=sel).grid(row=13, sticky="W")
tk.Radiobutton(window, text=RateList[13] + " KS-" + FrqList[13] + "-" + SlotList[13], padx=20, variable=Frv, value=13,
               command=sel).grid(row=14, sticky="W")
tk.Radiobutton(window, text=RateList[14] + " KS-" + FrqList[14] + "-" + SlotList[14], padx=20, variable=Frv, value=14,
               command=sel).grid(row=15, sticky="W")
tk.Radiobutton(window, text=RateList[15] + " KS-" + FrqList[15] + "-" + SlotList[15], padx=20, variable=Frv, value=15,
               command=sel).grid(row=16, sticky="W")
tk.Radiobutton(window, text=RateList[16] + " KS-" + FrqList[16] + "-" + SlotList[16], padx=20, variable=Frv, value=16,
               command=sel).grid(row=17, sticky="W")
tk.Radiobutton(window, text=RateList[17] + " KS-" + FrqList[17] + "-" + SlotList[17], padx=20, variable=Frv, value=17,
               command=sel).grid(row=18, sticky="W")

# 2 =============================================================================================================
txtPW = "Power %"
txtPW_out = tk.Label(window, text=txtPW, justify=tk.LEFT, padx=20)
txtPW_out.grid(row=24, column=0)
PWR = tk.Scale(from_=0, to=100, resolution=1, orient="horizontal")
PWR.grid(row=25, column=0)

# 3 =============================================================================================================
txtCS = "Constellation"
txtCS_out = tk.Label(window, text=txtCS, justify=tk.LEFT, padx=20)
txtCS_out.grid(row=0, column=1, sticky="W")
tk.Radiobutton(window, text="QPSK", padx=20, variable=Csv, value=1).grid(row=1, column=1, sticky="W")
tk.Radiobutton(window, text="8PSK", padx=20, variable=Csv, value=2).grid(row=2, column=1, sticky="W")
tk.Radiobutton(window, text="16PSK", padx=20, variable=Csv, value=3).grid(row=3, column=1, sticky="W")
tk.Radiobutton(window, text="32PSK", padx=20, variable=Csv, value=4).grid(row=4, column=1, sticky="W")

# 4 ===========================================================================================================
txtFC = "FEC"
txtFC_out = tk.Label(window, text=txtFC, justify=tk.LEFT, padx=10)
txtFC_out.grid(row=0, column=2, sticky="W")
tk.Radiobutton(window, text="1/4", padx=10, variable=Fcv, value=1).grid(row=1, column=2, sticky="W")
tk.Radiobutton(window, text="1/3", padx=10, variable=Fcv, value=2).grid(row=2, column=2, sticky="W")
tk.Radiobutton(window, text="2/5", padx=10, variable=Fcv, value=3).grid(row=3, column=2, sticky="W")
tk.Radiobutton(window, text="1/2", padx=10, variable=Fcv, value=4).grid(row=4, column=2, sticky="W")
tk.Radiobutton(window, text="3/5", padx=10, variable=Fcv, value=5).grid(row=5, column=2, sticky="W")
tk.Radiobutton(window, text="2/3", padx=10, variable=Fcv, value=6).grid(row=1, column=3, sticky="W")
tk.Radiobutton(window, text="3/4", padx=10, variable=Fcv, value=7).grid(row=2, column=3, sticky="W")
tk.Radiobutton(window, text="4/5", padx=10, variable=Fcv, value=8).grid(row=3, column=3, sticky="W")
tk.Radiobutton(window, text="5/6", padx=10, variable=Fcv, value=9).grid(row=4, column=3, sticky="W")
tk.Radiobutton(window, text="8/9", padx=10, variable=Fcv, value=10).grid(row=5, column=3, sticky="W")
tk.Radiobutton(window, text="9/10", padx=10, variable=Fcv, value=11).grid(row=6, column=3, sticky="W")

# 5 =============================================================================================================
txtMD = "Mode"
txtMD_out = tk.Label(window, text=txtMD, justify=tk.LEFT, padx=20)
txtMD_out.grid(row=7, column=1, sticky="W")
tk.Radiobutton(window, text="DVB-S", padx=20, variable=Mdv, value=1).grid(row=8, column=1, sticky="W")
tk.Radiobutton(window, text="DVB-S2", padx=20, variable=Mdv, value=2).grid(row=9, column=1, sticky="W")

# 6 =============================================================================================================
txtCD = "Codec"
txtCD_out = tk.Label(window, text=txtCD, justify=tk.LEFT, padx=20)
txtCD_out.grid(row=7, column=2, sticky="W")
tk.Radiobutton(window, text="h264", padx=20, variable=Cdv, value=1).grid(row=8, column=2, sticky="W")
tk.Radiobutton(window, text="h265", padx=20, variable=Cdv, value=2).grid(row=9, column=2, sticky="W")

# 7 =============================================================================================================
txtCL = "Calibrate"
txtCL_out = tk.Label(window, text=txtCL, justify=tk.LEFT, padx=20)
txtCL_out.grid(row=7, column=3, sticky="W")
tk.Checkbutton(window, text="Cal.", padx=20, variable=Cav).grid(row=8, column=3, sticky="W")

# 8 =============================================================================================================
txtFM = "Frame"
txtFM_out = tk.Label(window, text=txtFM, justify=tk.LEFT, padx=20)
txtFM_out.grid(row=11, column=1, sticky="W")
tk.Radiobutton(window, text="Short", padx=20, variable=Fmv, value=1).grid(row=12, column=1, sticky="W")
tk.Radiobutton(window, text="Long", padx=20, variable=Fmv, value=2).grid(row=13, column=1, sticky="W")

# 9 =============================================================================================================
txtPL = "Pilots"
txtPL_out = tk.Label(window, text=txtPL, justify=tk.LEFT, padx=10)
txtPL_out.grid(row=11, column=2, sticky="W")
tk.Radiobutton(window, text="With", padx=10, variable=Plv, value=1).grid(row=12, column=2, sticky="W")
tk.Radiobutton(window, text="Without", padx=10, variable=Plv, value=2).grid(row=13, column=2, sticky="W")

# 10 ===========================================================================================================
txtUS = "Usample"
txtUS_out = tk.Label(window, text=txtUS, justify=tk.LEFT, padx=10)
txtUS_out.grid(row=10, column=3, sticky="W")
tk.Radiobutton(window, text="1", padx=10, variable=Usv, value=1).grid(row=11, column=3, sticky="W")
tk.Radiobutton(window, text="2", padx=10, variable=Usv, value=2).grid(row=12, column=3, sticky="W")
tk.Radiobutton(window, text="4", padx=10, variable=Usv, value=3).grid(row=13, column=3, sticky="W")

# 11 ===========================================================================================================
txtRT = "Ratio"
txtRT_out = tk.Label(window, text=txtRT, justify=tk.LEFT, padx=20)
txtRT_out.grid(row=15, column=1, sticky="W")
tk.Radiobutton(window, text="4:3", padx=20, variable=Rtv, value=1).grid(row=16, column=1, sticky="W")
tk.Radiobutton(window, text="16:9", padx=20, variable=Rtv, value=2).grid(row=17, column=1, sticky="W")

# 12 ===========================================================================================================
txtRes = "Video Res(x)"
txtRes_out = tk.Label(window, text=txtRes, justify=tk.LEFT, padx=20)
txtRes_out.grid(row=15, column=2)
RES = ""
RES = tk.Entry(window, justify="center", width=4)
RES.grid(row=16, column=2)

# 13 ===========================================================================================================
txtVid = "Video FPS"
txtVID_out = tk.Label(window, text=txtVid, justify=tk.LEFT, padx=20)
txtVID_out.grid(row=15, column=3)
VID = ""
VID = tk.Entry(window, justify="center", width=3)
VID.grid(row=16, column=3)

# 14 ===========================================================================================================
txtSR = "Symbol rate"
txtSR_out = tk.Label(window, text=txtSR, justify=tk.LEFT, padx=5)
txtSR_out.grid(row=19, column=1)
SR = ""
SR = tk.Entry(window, justify="center", width=5)
# SR.insert(1, "1000")
SR.grid(row=20, column=1)

# 15 ===========================================================================================================
txtPP = "PCR_PTS"
txtPP_out = tk.Label(window, text=txtPP, justify=tk.LEFT, padx=20)
txtPP_out.grid(row=19, column=2)
PP = ""
PP = tk.Entry(window, justify="center", width=7)
# PP.insert(0, "200000")
PP.grid(row=20, column=2)

# 16 ===========================================================================================================
txtGO = "Video GOP"
txtGO_out = tk.Label(window, text=txtGO, justify=tk.LEFT, padx=20)
txtGO_out.grid(row=19, column=3)
GOP = ""
GOP = tk.Entry(window, justify="center", width=4)
# GOP.insert(1, "100")
GOP.grid(row=20, column=3)



OpenBt = tk.Button(text="Open", command=OpenBtFn)
OpenBt.grid(row=30, column=1)

SaveBt = tk.Button(text="Save", command=SaveBtFn)
SaveBt.grid(row=30, column=2)

TranBt = tk.Button(text="TX", fg="red", command=TranBtFn)
TranBt.grid(row=30, column=3)

NameFl = '/home/user/dvbsdr/pyt/base'
opnfle(NameFl)


if __name__ == "__main__":
    print(SR.get())
    print(Mdv.get())
    window.mainloop()
