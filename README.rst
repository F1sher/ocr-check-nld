How to install ocr-check?
==========

1) In first you need to install ``pip`` throught Terminal:
   | - download get-pip.py: ``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``
   | - install it: ``python get-pip.py``

2) cd to the directory where source code of ocr-check will be downloaded

3) Clone this repo: ``git clone https://github.com/F1sher/ocr-check-nld.git``

4) cd to dist direcotory: ``cd ocr-check-nld/dist``

5) Install ocr-check wheel with pip:
   ``pip install ocr_check_nld-0.1.0-py3-none-any.whl``

6) Now you can use it in Terminal like this:
   ``ocr-check path_to_check_file check_lang``
   | For example:
     ``ocr-check ../check_1.jpg eng``
