# Download Google Images using Python
This is a simple bit of Python code to let you download Images from Google by using custom keywords. It uses the [Google Images Download](https://github.com/hardikvasa/google-images-download/blob/master/README.rst#config-file-format) library to accomplish this.

# Prerequisites
- [Python 2](https://www.python.org/downloads)
- pip
- [Google Images Download (python package)](https://github.com/hardikvasa/google-images-download/blob/master/README.rst#config-file-format)

# How to Download Images
- Clone this repository - `git clone https://github.com/sunnyg1210/downloadGoogleImages.git`
- Make sure all the above prerequisite libraries are installed
- Run the main file - `python download_google_images.py`

# How to change Keywords
The code uses a JSON format with each object containing a 'word' and 'limit' key value pairs. The word key can take multiple keywords seperated by a **comma** and the limit specified for each object will be the number of images download per keyword specified in the word string. You can multiple keyword objects in the keyword array.

To add/remove keywords, open the `./download_google_images.py` file and make changes to the contents in the **Edit This Section**.
Once you have made your desired changes, run the main file using `python download_google_images.py`.
All done :)

# Where are my Images stored?
The images will be stored in a newly created folder named 'Downloads'. It will be in the same directory as this repository.

# Customise the Arguments in the `downloadImages()` function
To add more filters and other options in the `args` section of the `downloadImages()` function, see [here](https://github.com/hardikvasa/google-images-download#arguments) 

# Disclaimer
Please do not download or use any image that violates its copyright terms. Google Images is a search engine that merely indexes images and allows you to find them. It does NOT produce its own images and, as such, it doesn't own copyright on any of them. The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners, even if they do not explicitly carry a copyright warning. You may not reproduce copyright images without their owner's permission, except in "fair use" cases, or you could risk running into lawyer's warnings, cease-and-desist letters, and copyright suits. Please be very careful before its usage!

This program takes no responsibility whatsoever regarding the images you download from Google using this program's code.
