# Rickroll-Detector
Identify rickroll links whether it's a direct YT link or a bit.ly link or a shorturl.at link or even a redirect

## Purpose of the project
Prevent yourself from getting rickrolled through links (If you're annoyed by them) <br/>

## Frameworks used
Selenium for python

## Requirements
Py >= 3.7 <br>
Chrome Browser <br>
Requests library and selenium for python. <br />
Git-scm

## Setup
Clone the repository to your favoured location using the command: ``` git clone https://github.com/TheProgrammingArchive/Rickroll-Detector/ ```
The Project structure is as followed <br>
```
RickrollDetector
├── LICENSE
├── README.md
└── rickroll_detector
    ├── ChromeDriver
    │   └── chromedriver
    ├── Chromedriver.zip
    ├── find_identity.py
    ├── installer.py
    └── sources.py
```

## Options
### find_identity.py -c "link": 
Searches for a certain SME tag in the video to check if it's a rickroll or not

### find_identity.py -cmt "link"
Searches for any mentions about rickrolls in the comment section of the video

### find_identity.py -t "link"
Searches for certain keywords in the video title to determine if it's a rickroll or not

### find_identity.py -pl "link"
Sometimes rickroll videos are taken from certain rickroll playlists. Checks for certain keywords in the playlist name, if nothing was found returns 'No playlist found'

### find_identity.py -plv "link"
Prints a list of all the videos in a playlist of a video if found, if the video isn't in a playlist returns 'No playlist found'

### find_identity.py -dsc "link"
Prints description of the video.

### find_identity.py -d "link"
Prints details of the video such as title, view count, date uploaded, like count, dislike count 
```
['Title:', 'Rick Astley - Never Gonna Give You Up (Video)', 'Views:', '918,026,549 views', 'Date:', '24 Oct 2009', 'Likes:', '9.2M', 'Dislikes: ', '272K']
```

### find_identity.py -od "link"
Prints the name of the channel and subscriber count 

```
['Channel name:', 'Official Rick Astley', 'Subscriber count:', '2.04M subscribers']
```

### find_identity.py -chnc "link"
Searches for the name of certain flagged channels and alerts the user if the link is a rickroll

## Usage
Linux <br>
```
ubuntu@yt:~/rickroll-detector/rickroll-detector$ python3 find_identity.py -option "link"
```

Windows <br>
```
C:\pathtodetector\rickroll_detector> find_identity.py -option "link"
```
