import os,time,sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import prGreen,prRed,prYellow
import subprocess
import platform


prYellow("ℹ️  This script will check if the bot can automatically log in Linkedin for you.")

def checkPython():
    try:
        if(sys.version):
            prGreen("✅ Python is succesfully installed!")
        else:
            prRed("❌ Python is not installed please install Python first: https://www.python.org/downloads/")
    except Exception as e:
        prRed(e)

def checkPip():
    try:
        import pip
        prGreen("✅ Pip is succesfully installed!")
    except ImportError:
        prRed("❌ Pip not present. Install pip: https://pip.pypa.io/en/stable/installation/")

def checkSelenium():
    try:
        import selenium
        prGreen("✅ Selenium is succesfully installed!")
    except ImportError:
        prRed("❌ Selenium not present. Install Selenium: https://pypi.org/project/selenium/")

# def checkFirefox():
#     try:
#         import subprocess
#         output = subprocess.check_output(['firefox', '--version'])
#         if(output):
#             prGreen("✅ Firefox is succesfully installed!")
#         else:
#             prRed("❌ Firefox not present. Install firefox: https://www.mozilla.org/en-US/firefox/")

#     except ImportError as e:
#         prRed(e)

def check_firefox():
    try:
        if sys.platform.startswith('win'):
            # Windows
            firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Update with your Firefox path if different
            command = [firefox_path, '--version']
        elif sys.platform.startswith('darwin'):
            # macOS
            command = ['/Applications/Firefox.app/Contents/MacOS/firefox', '--version']
        else:
            # Linux (assumes Firefox is available in the system's PATH)
            command = ['firefox', '--version']

        # Run the appropriate command to check the version
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        version = output.strip()
        if version:
            print(f"✅ Firefox version {version} is installed!")
        else:
            print("❌ Firefox not present. Install Firefox: https://www.mozilla.org/en-US/firefox/")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Firefox not present. Install Firefox: https://www.mozilla.org/en-US/firefox/")


def checkSeleniumLinkedin():

    options = Options()
    #firefoxProfileRootDir = os.getenv('firefoxProfileRootDir')

    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("-profile")
    #options.add_argument(firefoxProfileRootDir)
    #options.headless = True

    browser = webdriver.Firefox(options=options)

    try:
        browser.get('https://www.ongundemirag.com')
        if(browser.title.index("Ongun")>-1):
            prGreen("✅ Selenium and geckodriver is working succesfully!")
        else:
            prRed("❌ Please check if Selenium and geckodriver is installed")
    except Exception as e:
        prRed(e)

    try:
        browser.get('https://www.linkedin.com/feed/')
        time.sleep(3)
        if "Feed" in browser.title:
            prGreen('✅ Successfully you are logged in to Linkedin, you can now run main bot script!')
        else:
            prRed('❌ You are not automatically logged in, please set up your Firefox Account correctly.')
    except Exception as e:
        prRed(e)
    finally:
        browser.quit()



checkPython()
checkPip()
checkSelenium()
# checkFirefox()
check_firefox()
checkSeleniumLinkedin()
