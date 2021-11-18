# Download Art Prints from Van Gogh Museum
A simple web scraper to get an art print from VGM with given link (in different resolutions).

### Walkthrough
1. User pastes a link to the print:
  * BeautifulSoup searches the page for 'data-id' and 'data-base-path' attributes
  * 'data-id' leads to a JSON with addresses to image tiles at different resolutions

2. User chooses available resolution and a name:
  * urlib downloads appropriate tiles
  * cv2 concatinates these tiles together into the final image
  * shutil deletes temporary files
