import requests
import zipfile
import platform
import sys

chrome_version = '89.0.4389.23'
edge_version = '89.0.774.75'
gecko_version = 'v0.29.1'


def install_chrome_driver_package(link):
    chromedriver_content = requests.get(link)

    chromedriver_file = open('Chromedriver.zip', 'wb')
    chromedriver_file.write(chromedriver_content.content)
    chromedriver_file.close()

    with zipfile.ZipFile('Chromedriver.zip') as zip_file:
        zip_file.extractall('ChromeDriver')


def install_edge_driver_package(link):
    edgedriver_content = requests.get(link)

    edgedriver_file = open('Edgedriver.zip', 'wb')
    edgedriver_file.write(edgedriver_content.content)
    edgedriver_file.close()

    with zipfile.ZipFile('Edgedriver.zip') as zip_file:
        zip_file.extractall('EdgeDriver')


if __name__ == '__main__':

    try:
        driver_file = open('DriverToUse.txt', 'w')
        browser_select = sys.argv[1]
        if browser_select == 'chrome':
            install_chrome_driver_package(f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip')
            driver_file.writelines('chrome')
            driver_file.close()

        elif browser_select == 'edge':
            install_edge_driver_package(f'https://msedgedriver.azureedge.net/{edge_version}/edgedriver_win32.zip')
            driver_file.writelines('edge')
            driver_file.close()

        else:
            print('Supported web browsers are chrome and edge')
            exit()

    except IndexError:
        print('Usage (Windows): installer.py webbrowser [eg: installer.py chrome]')
        print('Usage (Linux/Mac): python3 installer.py webbroser [eg: python3 installer.py firefox]')
        exit()
