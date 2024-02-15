import csv
import requests
from datetime import datetime
from boxsdk import Client, OAuth2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_aptnotes_csv(filename):  
    url = 'https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.csv'  
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(output_file, 'wb') as file:
            file.write(response.content)

        print(f'Successfully downloaded: {output_file}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def download_aptnote(url, filename):

    # Replace 'path_to_webdriver_executable' with the path to your WebDriver executable
    #chromedriver_path = '/Users/hungnguyen/CODE/chromedriver'
    driver = webdriver.Chrome()
    # The URL of the Box.com shared link
    url = 'https://app.box.com/s/ce4fr8p0mxv2pjcvh4pmma1q7oqc4vnc/'

    try:
        driver.get(url)
        
        # Wait for the download button to become clickable
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download")]')))
        
        # Click the download button
        download_button.click()

        print("Clicked the download button. Please wait for the download to complete.")
        
        # Add a delay or use WebDriverWait to wait for the download to finish

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window (this doesn't terminate the WebDriver process)
        driver.quit()

def parse_csv(filename):
    third_column_entries = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the CSV has at least 4 columns
            if len(row) >= 4:
                third_column_entries.append(row[3])
    return third_column_entries


# Get the current date and time
current_datetime = datetime.now()
# Format the date in ddmmyyyy format
formatted_date = current_datetime.strftime("%d%m%Y")
output_file = 'APTnotes_'+formatted_date +'.csv'  # Replace with the desired local file name
download_aptnotes_csv(output_file)
entries = parse_csv(output_file)

auth = OAuth2(
    client_id='lb2ibcsmb5i6zhbkcvdxyuvp81xh1ezo',
    client_secret='xWqTVPEAugVUswNUfcfu3XIS7pO2xuG9',
    access_token='Le5mNho40g3WXEUJ29hBfIt783ncJ4ma',
)
client = Client(auth)
me = client.user().get()
print(f'My user ID is {me.id}')


for entry in entries:
    ouput_file = '../RawReports/'+entry.split('/')[-1]+'.pdf'
    download_aptnote(entry, ouput_file)



