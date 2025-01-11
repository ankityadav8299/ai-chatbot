import pyperclip
import pyautogui
import google.generativeai as genai
import time

def lastmessage(text,sender_name = "Ankit Yadav"):
    messages = text.strip().split("/2025] ")[-1]
    if(sender_name in messages):
        return False
    return True
    
def googleai(c):
    # assistant_thread = threading.Thread()
    # assistant_thread.start()
    genai.configure(api_key="AIzaSyASTjhJI80UJvowouC55vNED4uY7ksYNR8")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(c)
    # response.max_output_tokens = 250
    # time.sleep(1)
    return (response.text)
pyautogui.click(870,1060)
while(True):
    time.sleep(3)
    pyautogui.moveTo(708,126)
    pyautogui.dragTo(1895,956,duration=1,button='left')
    pyautogui.hotkey('ctrl','c')
    # pyautogui.moveTo(676,912)
    time.sleep(1)
    pyautogui.click(676,912)
    time.sleep(1)
    text = pyperclip.paste()
    if lastmessage(text) == True:
        response = googleai("you are ankit yadav,understand the context and reply so that the other person doesnt know its Ai gneerated, continue the conversation as ankit yadav in same language as another person,give the response only"+text)
        pyperclip.copy(response)
        pyautogui.click(891,978)
        time.sleep(1)
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pyautogui.press('enter')

