import requests
import img2pdf
import os

#Creating the "images" folder if it's not in the current directory
if not os.path.isdir("images"):
     os.mkdir("images")
     print('\n' + '#' * 36)
     print('The folder "images" will be created!')
     print('#' * 36 + '\n')

def get_data():

    HEADERS = {
    'Accept': '*/*',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.2.381 Yowser/2.5 Safari/537.36'
    }

    img_list = []
    for i in range (1, 49):
        url = f'https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'

        req = requests.get(url = url, headers = HEADERS)
        response = req.content

        #Saving catalog images
        with open(f'images/page_{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'images/page_{i}.jpg')
            print(f'Page {i} of 48 has been downloaded')

    #Converting images to a PDF file
    with open('catalog.pdf', 'wb') as file:
        file.write(img2pdf.convert(img_list))
    print('\n' + '#' * 34)
    print('PDF file was created successfully!')
    print('#' * 34 + '\n')

def main():
    get_data()

if __name__ == '__main__':
    main()
