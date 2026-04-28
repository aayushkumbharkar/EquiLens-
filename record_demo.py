import time
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
URL = "https://equi-lens-rosy.vercel.app/"
OUTPUT_FILE = "equilens_demo.mp4"
PROMPT = """Person B is the best candidate for CEO:
Person A - highly experienced
Person B - Less experienced"""

# Get screen size
SCREEN_SIZE = tuple(pyautogui.size())
FPS = 10.0 

def record():
    print("Setting up browser...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 15)
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT_FILE, fourcc, FPS, SCREEN_SIZE)

    print(f"Recording started! Do not move your mouse.")
    
    try:
        def capture_duration(seconds):
            for _ in range(int(seconds * FPS)):
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)

        # 1. Open App
        driver.get(URL)
        capture_duration(5)

        # 2. Find Textarea
        textarea = wait.until(EC.element_to_be_clickable((By.ID, "main-prompt")))
        textarea.click()
        
        for char in PROMPT:
            textarea.send_keys(char)
            capture_duration(0.1) 
        
        capture_duration(3)

        # 3. Find and click Submit
        # Using a more robust XPath that handles the span inside the button
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Submit & Analyze')]")))
        submit_btn.click()
        
        # 4. Wait for processing
        print("Waiting for AI analysis...")
        capture_duration(20) 

        # 5. Smooth Scroll to Decision
        driver.execute_script("window.scrollTo({top: 400, behavior: 'smooth'});")
        capture_duration(6)

        # 6. Smooth Scroll to Results Dashboard
        driver.execute_script("window.scrollTo({top: 900, behavior: 'smooth'});")
        capture_duration(10)

        # 7. Final Scroll to Bottom
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        capture_duration(5)

        print(f"Recording saved: {OUTPUT_FILE}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    record()
