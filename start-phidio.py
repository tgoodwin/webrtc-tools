import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def loadPage(driver, room):
    # Load page
    driver.get('https://www.webrtc-wim.net/?' + room)

    # Wait for the page to load and roulette btn to become visible
    # WebDriverWait(driver, 15).until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, "#roulette")))


# def joinConversation(driver, joinCall):

    # wait till access is granted
    # WebDriverWait(driver, 15).until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, ".chatting")))

def logStats(driver):
    # driver.find_element_by_id("roulette").click()
    print 'joining call for 3 minutes'
    # wait 3 minutes
    time.sleep(180)
    print 'clicking logStats'
    driver.find_element_by_id("logStats").click()
    time.sleep(10)
    print 'done with call'
    driver.quit()
    sys.exit()


def waitForCall(driver):
    print 'waiting for call'


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--reduce-security-for-testing")
    chrome_options.add_argument("--use-file-for-fake-video-capture=/home/ubuntu/webrtc-tools/in_to_tree_420_720p50.y4m")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    try:
        arguments = sys.argv
        if len(arguments) < 2:
            loadPage(driver, 'testroom')
        else
            loadPage(driver, sys.argv[1])

        if '-log' in arguments:
            logStats(driver)
        else:
            waitForCall(driver)

    finally:
        print 'done'

# -args --use-file-for-fake-video-capture=/Users/bartjansen/in_to_tree_420_720p50.y4m --use-fake-device-for-media-stream --enable-features=WebRTC-H264WithOpenH264FFmpeg

# usage:
# to wait for call run: python start-phidio.py
# to join call: python start-phidio.py -join