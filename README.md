# Download Art Prints from Van Gogh Museum
A simple web scraper to get an art print from VGM with a given a link from a collection section (in different resolutions).

## Installation (macOS)

1. Open Terminal.
2. Install [Homebrew](https://brew.sh).
3. Install git:
```
brew install git
```
4. Clone this repository:
```
git clone https://github.com/rafaelmikayelyan/dl-art-print-from-vgm.git
```
5. Install [Python 3.xx](https://realpython.com/installing-python/)
6. Install necessary libraries:
 * beautifulsoup4:
```
pip install beautifulsoup4
```
 * beautifulsoup4:
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
