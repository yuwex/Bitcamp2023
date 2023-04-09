# Email Ahoy!
![logo](/src/assets/logo.png)

## What is Email Ahoy!
Have you ever been overwhelmed by your overflowing inbox? So have we! We developed a companion for your email that incentivizes you to check it more often to defend your pirate friend from email attacks on your time and attention. Fend off email pirates and get your doubloons up with Email Ahoy. We used the Google gmail API so you can protect your inbox in real time.

## Developed By
* [yuwex](https://github.com/yuwex)
* [Brandon Jenkins](https://github.com/bjenkins0829)
* [Will Rabalais](https://github.com/WillRabalais04)

## How to Install
First, you need to set up this Python environment:
1. Download and Install Python 3.11 from [the Python Foundation](https://www.python.org/downloads/)
2. Clone this repository by clicking the Code button
3. Set up a virtual environment.
   - Open the directory of this repository on your local machine
   - Run `python3.11 -m venv .venv`, which creates a new virtual environment
   - Run `source .venv/bin/activate`, which uses the virtual environment
   - Run `pip install -r requirements.txt`, which installs the required libraries

After setting up a virtual environment, you have to create a Google Developer application. To do this, do the following:
1. Go to https://console.cloud.google.com/apis/credentials and log into your Google account
2. Click `Create Credentials` and choose `OAuth client ID`
3. Set application type to `Desktop App` and set any name
4. Click `Download JSON`
5. Drag that file into the `Bitcamp2023` folder and rename it to `client_secret.json`

After downloading and renaming the Google API credentials, you can now run the project!
1. Make sure you are in the `Bitcamp2023` directory
2. Run `python src/EmailAhoy.py`
3. Enjoy defeating Email Pirates on the Digital Seas!

## How to Use
* After you've linked your email, open the app and see how many unread emails you have
* As emails come in, pay attention to the enemies coming your way and read your emails to protect your pirate

## Assets Used

Images
* [Swords](https://www.123rf.com/free-vector_79145346_pirate-sword-pixel-art.html)
* [Pirate Graphics Set 1](https://0x72.itch.io/16x16-pirates-tileset)
* [Pirate Graphics Set 2](https://www.deviantart.com/lustriouscharming/art)
* [Pirates of the Caribbean Characters](https://www.deviantart.com/lustriouscharming/art/Pirates-of-the-Caribbean-Characters-8-Bit-607468123)
* [Clouds](http://pixelartmaker.com/art/281303a9bbc5eb8)
* [Wallpaper](https://www.wallpaperflare.com/)
* [Wallpaper 2](8-bit-artwork-sky-landscape-clouds-pixel-art-pixels-wallpaper-uvtkj)
* [Clouds](http://pixelartmaker.com/art/281303a9bbc5eb8)
* [Smoke](https://www.pinterest.com.mx/pin/662944007653541905/)

Font
* [Wayfarer's Toybox](https://www.fontspace.com/wayfarers-toy-box-font-f40851)
