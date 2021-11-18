# Download Art Prints from Van Gogh Museum
A simple web scraper to get an art print from VGM with given link (in different resolutions).

### Walkthrough
1. User pastes the link with the print:
  * BeautifulSoup searches the page for 'data-id' and 'data-base-path' attributes
  * 'data-id' leads to a JSON with image tiles at different resolutions

2. User chooses resolution and name:
  * cv2 concatinates appripreate tiles together into the final image
