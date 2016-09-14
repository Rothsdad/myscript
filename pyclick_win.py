import win32con,win32gui,win32api
from ctypes import *
import time

# 虚拟键盘按键编码
VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0}

# 鼠标位置结构体类型
class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]
    
# 获取当前鼠标在桌面中的位置
def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)

# 鼠标左键点击函数
def mouse_left_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        #time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
# 鼠标右键点击函数
def mouse_right_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        #time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    
# 鼠标左键双击函数
def mouse_left_dclick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        #time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# 设置鼠标位置函数
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)
    
# 字符串逐个输入作为键盘输入
def key_string_input(string=''):
    for index in string:
        win32api.keybd_event(VK_CODE[index],0,0,0) # 键盘上的对应虚拟键值按下
        win32api.keybd_event(VK_CODE[index],0,win32con.KEYEVENTF_KEYUP,0)  # # 键盘上的对应虚拟键值弹起
        #time.sleep(0.01)
        
# 字符串整体输入作为键盘输入
def key_overall_input(string=''):
    win32api.keybd_event(VK_CODE[string],0,0,0)
    win32api.keybd_event(VK_CODE[string],0,win32con.KEYEVENTF_KEYUP,0)    
    #time.sleep(0.01)

    
def double_key_together(first_key = '',second_key = ''):
    for index in second_key:
        win32api.keybd_event(VK_CODE[first_key],0,0,0) # 第一功能键按下
        win32api.keybd_event(VK_CODE[index],0,0,0) # 输入第一功能键下的第二个键
        win32api.keybd_event(VK_CODE[index],0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(VK_CODE[first_key],0,win32con.KEYEVENTF_KEYUP,0) # 第一个键弹起
        
if __name__ == "__main__":
    
    # 显示鼠标在桌面上的坐标，改用软件实时显示方便查看
    mouse_position = get_mouse_point()
    print mouse_position
 
    
    # 循环部署5台虚拟机
    for n in range(1,2): 
        
        # 点击开始导入镜像文件
        mouse_left_click(28,32) # 点击文件
        mouse_left_click(61, 79) # 点击部署OVF模板
        time.sleep(3)

        mouse_left_click(1183,792)# 点击下一步
        time.sleep(1)
        mouse_left_click(1183,792)# 点击下一步
        time.sleep(1)
        mouse_left_click(990,348)# 点击输入名称
        time.sleep(1)
        for i in range(40):
            key_overall_input('backspace') # 删除旧名字
            
        double_key_together('shift','ac-') # 输入的名称
        key_string_input('1.0.8')
        double_key_together('shift','-')
        key_string_input('0'+str(n))
        
        mouse_left_click(1183,792)# 点击下一步
        time.sleep(1)
        mouse_left_click(798,471)# 点击选中Thin Provision
        mouse_left_click(1183,792)# 点击下一步
        mouse_left_click(1183,792)# 点击下一步
        mouse_left_click(794,714)# 点击选中部署后打开电源
        mouse_left_click(1183,792)# 点击完成
        
        time.sleep(5)
