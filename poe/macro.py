
# import ctypes
# from system_hotkey import SystemHotkey
from PIL import ImageGrab
import cv2, time
import numpy as np

# SendInput = ctypes.windll.user32.SendInput

# PUL = ctypes.POINTER(ctypes.c_ulong)
# class KeyBdInput(ctypes.Structure):
#     _fields_ = [("wVk", ctypes.c_ushort),
#                 ("wScan", ctypes.c_ushort),
#                 ("dwFlags", ctypes.c_ulong),
#                 ("time", ctypes.c_ulong),
#                 ("dwExtraInfo", PUL)]

# class HardwareInput(ctypes.Structure):
#     _fields_ = [("uMsg", ctypes.c_ulong),
#                 ("wParamL", ctypes.c_short),
#                 ("wParamH", ctypes.c_ushort)]

# class MouseInput(ctypes.Structure):
#     _fields_ = [("dx", ctypes.c_long),
#                 ("dy", ctypes.c_long),
#                 ("mouseData", ctypes.c_ulong),
#                 ("dwFlags", ctypes.c_ulong),
#                 ("time",ctypes.c_ulong),
#                 ("dwExtraInfo", PUL)]
    
# class Input_I(ctypes.Union):
#     _fields_ = [("ki", KeyBdInput),
#                  ("mi", MouseInput),
#                  ("hi", HardwareInput)]

# class Input(ctypes.Structure):
#     _fields_ = [("type", ctypes.c_ulong),
#                 ("ii", Input_I)]

# DIK_ESCAPE          =0x01
# DIK_1               =0x02
# DIK_2               =0x03
# DIK_3               =0x04
# DIK_4               =0x05
# DIK_5               =0x06
# DIK_6               =0x07
# DIK_7               =0x08
# DIK_8               =0x09
# DIK_9               =0x0A
# DIK_0               =0x0B
# DIK_MINUS           =0x0C    #/* - on main keyboard */
# DIK_EQUALS          =0x0D
# DIK_BACK            =0x0E    #/* backspace */
# DIK_TAB             =0x0F
# DIK_Q               =0x10
# DIK_W               =0x11
# DIK_E               =0x12
# DIK_R               =0x13
# DIK_T               =0x14
# DIK_Y               =0x15
# DIK_U               =0x16
# DIK_I               =0x17
# DIK_O               =0x18
# DIK_P               =0x19
# DIK_LBRACKET        =0x1A
# DIK_RBRACKET        =0x1B
# DIK_RETURN          =0x1C    #/* Enter on main keyboard */
# DIK_LCONTROL        =0x1D
# DIK_A               =0x1E
# DIK_S               =0x1F
# DIK_D               =0x20
# DIK_F               =0x21
# DIK_G               =0x22
# DIK_H               =0x23
# DIK_J               =0x24
# DIK_K               =0x25
# DIK_L               =0x26
# DIK_SEMICOLON       =0x27
# DIK_APOSTROPHE      =0x28
# DIK_GRAVE           =0x29    #/* accent grave */
# DIK_LSHIFT          =0x2A
# DIK_BACKSLASH       =0x2B
# DIK_Z               =0x2C
# DIK_X               =0x2D
# DIK_C               =0x2E
# DIK_V               =0x2F
# DIK_B               =0x30
# DIK_N               =0x31
# DIK_M               =0x32
# DIK_COMMA           =0x33
# DIK_PERIOD          =0x34    #/* . on main keyboard */
# DIK_SLASH           =0x35    #/* / on main keyboard */
# DIK_RSHIFT          =0x36
# DIK_MULTIPLY        =0x37    #/* * on numeric keypad */
# DIK_LMENU           =0x38    #/* left Alt */
# DIK_SPACE           =0x39
# DIK_CAPITAL         =0x3A
# DIK_F1              =0x3B
# DIK_F2              =0x3C
# DIK_F3              =0x3D
# DIK_F4              =0x3E
# DIK_F5              =0x3F
# DIK_F6              =0x40
# DIK_F7              =0x41
# DIK_F8              =0x42
# DIK_F9              =0x43
# DIK_F10             =0x44
# DIK_NUMLOCK         =0x45
# DIK_SCROLL          =0x46    #/* Scroll Lock */
# DIK_NUMPAD7         =0x47
# DIK_NUMPAD8         =0x48
# DIK_NUMPAD9         =0x49
# DIK_SUBTRACT        =0x4A    #/* - on numeric keypad */
# DIK_NUMPAD4         =0x4B
# DIK_NUMPAD5         =0x4C
# DIK_NUMPAD6         =0x4D
# DIK_ADD             =0x4E    #/* + on numeric keypad */
# DIK_NUMPAD1         =0x4F
# DIK_NUMPAD2         =0x50
# DIK_NUMPAD3         =0x51
# DIK_NUMPAD0         =0x52
# DIK_DECIMAL         =0x53    #/* . on numeric keypad */
# DIK_F11             =0x57
# DIK_F12             =0x58
# RUN_W               =0x2A
# RUN_S               =0x2A
# RUN_A               =0x2A
# RUN_D               =0x2A

# def PressKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
#     x = Input( ctypes.c_ulong(1), ii_ )
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# def ReleaseKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
#     x = Input( ctypes.c_ulong(1), ii_ )
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# def error(err = "Something else went wrong"):
#     print(err)

# def poison(event, hotkey, args):
#     pass
#     print("---------------------------")
#     try:
#         PressKey(DIK_3)
#         time.sleep(0.08)
#         ReleaseKey(DIK_3)
#         time.sleep(0.08)

#         PressKey(DIK_4)
#         time.sleep(0.08)
#         ReleaseKey(DIK_4)
#         time.sleep(0.08)

#         PressKey(DIK_5)
#         time.sleep(0.08)
#         ReleaseKey(DIK_5)

#         print("Use Poison")
#     except:
#         error()

ah = True
later = time.time()

# def autoheal(event, hotkey, args): 
#     pass
#     print("---------------------------")
#     try:
#         if(ah == True):
#             ah = False
#         else:
#             ah = True

#         print("Auto Heal : ", ah)
#     except:
#         error()
 
# hk = SystemHotkey(consumer=poison).register(('e'))
# h0 = SystemHotkey(consumer=autoheal).register(('0'))

while True:
    if(ah == True):
        im = ImageGrab.grab()
        img_np = np.array(im)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        h, w, _ = frame.shape
        h = int(h/2)
        frame = cv2.resize(frame, (int(w/2), h))
        frame = frame[h-85:h-65, 65:110]

        avg_color_per_row = np.average(frame, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        # cv2.imshow('frame',frame)

        now = time.time()
        difference = int(now - later)
        # print(avg_color, difference)

        if(avg_color[2] < 100 and difference > 6):
            # PressKey(DIK_2)
            # time.sleep(0.1)
            # ReleaseKey(DIK_2)
            print("Heal")
            later = now


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()