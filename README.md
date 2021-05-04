# PDF to Audiobook (split by character length or something)

Uses Textract and Google Wavenet


## Install dependencies
```
conda create --name <name>
conda activate <name>
pip install -r requirements.txt
```

## Install system dependencies (linux only)
```
apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig|

```

## Export your GCloud credentials as an environment variable and set the quota
```
export GOOGLE_APPLICATION_CREDENTIALS="path"
```
(free tier is 10,000 char quota per month)

Create a quota.txt with the number 10000 (it will stop you if the chars exceed this quota)


## Usage

```python3 main.py <filepath_to_pdf> <filename_for_saved_mp3>```

Sample:
```python3 main.py './samples/wagelabor.pdf' part_of_book```

NOTE: remove the line in main to do the whole pdf:

```truncated_text = text[1:1000] #CHANGE THIS TO BLOW THROUGH YOUR FREE LIMITS```

