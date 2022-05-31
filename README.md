# Download Art Prints from Van Gogh Museum
A simple web scraper to get an art print from VGM using a link from a collection section of the museum (with choice of different resolutions if available).

## Requirements

* [Python 3.xx](https://realpython.com/installing-python/), with:
  * [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  * [opencv](https://pypi.org/project/opencv-python/)
  * [requests](https://pypi.org/project/requests/)
* git (optional, see Installation)

## Installation (macOS)

1. Open Terminal (press <kbd>Command</kbd>+<kbd>Space</kbd>, type ``` terminal ``` press <kbd>Return</kbd>).
2. Check if you have Python3.xx installed using the following command:
```
python3 --version
```
If you get an error 'No such file or directory", then install Python 3.xx [here](https://realpython.com/installing-python/).

3. Install necessary libraries (see requiremets):

Git installation is optional - you can simply download this repository (green 'CODE' button above) and unzip it into your Downloads folder, then skip to step 7.

#### Optional Git instalation

4. Install [Homebrew](https://brew.sh).
5. Install [git](https://formulae.brew.sh/formula/git#default)
6. Clone this repository:
```
cd ~/Downloads
git clone https://github.com/rafaelmikayelyan/dl-art-print-from-vgm.git
```

7. Run the app:
```
python3 ~/Downloads/dl-art-print-from-vgm/main.py
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
