
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pywhatkit

def send_whatsapp_message(receiver_number, message):

    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    
    input("Scan the QR code and press Enter once logged in")

   
    url = f"https://web.whatsapp.com/send?phone={receiver_number}&text={message}"

    # Open the chat with the receiver number
    driver.get(url)

    # Wait for the send button to load
    try:
        # if the  wait driver is running then the send button 
        send_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='send']"))
        )
        print("Send button found")
        
        # Send the message
        send_button.click()
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"Failed to send message: {e}")

    driver.quit()

    time.sleep(10)
    # this is other try if the seluinuim doesnt work 
    pywhatkit.sendwhatmsg(receiver_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1, wait_time=10)

if __name__ == "__main__":
 #my number if you want to ask me anything ☎️
 receiver_number = "+212703225919" 
 message = "Happy Birthday to you!"
 send_whatsapp_message(receiver_number, message)