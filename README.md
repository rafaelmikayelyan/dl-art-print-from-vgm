# Download Art Prints from Van Gogh Museum
A simple web scraper to get an art print from VGM with a given a link from a collection section (in different resolutions).

## Requirements

* Python 3.xx, with:
  * beautifulsoup4
  * opencv
  * requests
* git (optional)

## Installation (macOS)

Git installation is optional - you can simply download this repository (green CODE button above) and skip to step 5.

1. Open Terminal (press <kbd>Command</kbd>+<kbd>Space</kbd>, type ``` terminal ``` press <kbd>Return</kbd>).
3. Install [Homebrew](https://brew.sh).
4. Install git:
```
brew install git
```
4. Clone this repository:
```
git clone https://github.com/rafaelmikayelyan/dl-art-print-from-vgm.git
```
5. Install [Python 3.xx](https://realpython.com/installing-python/)
6. Install necessary libraries (in terminal, step 1):
 * beautifulsoup4:
```
pip install beautifulsoup4
```
 * opencv:
```
pip install opencv-python
```

7. Run the app:
```
python3 ~/dl-art-print-from-vgm/main.py
```

## Walkthrough
1. User pastes a link to the print:
  * BeautifulSoup searches the page for 'data-id' and 'data-base-path' attributes
  * 'data-id' leads to a JSON with addresses to image tiles at different resolutions

2. User chooses available resolution and a name:
  * urlib downloads appropriate tiles
  * cv2 concatinates these tiles together into the final image
  * shutil deletes temporary files


## ToDo
- Pass image directly to cv2
- Add scraper for 'collection' section
- Add GUI
- Add executable
