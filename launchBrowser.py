import webbrowser
import time

# List of websites 
websites = [
    'https://www.google.com',
    'https://www.github.com',
]

chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each website in a new tab
for url in websites:
    webbrowser.get('chrome').open_new_tab(url)
    time.sleep(1)  # Pause for a second to allow browser to open the tab
