Audio File Manager Project:
Author: Jacques Mathieu
Start Date: 6/13/2019

<b>Goals of this project:</b>
- To design a GUI tool that helps one easily update the metadata tags on one's collection of audio files

  - Features that this project will include that <i>OTHERS do not have:</i> 
	1) Intelligent autocompletion of metadata (more specifically):
	   - Automatically copying the entered song name to album name (if album name is missing)
	   - Automatically copying the entered artist name to the album artist field (if album artist field is missing)
	   - Ability to autofill metadata based on file name (using custom algorithm and locally built database)
	2) Enabling automatic mass conversion of various audio file types to 320kbps .mp3 files (or other specified defaults, though this is a personal project and I do not intend on implementing different defaults anytime soon)
	3) Automatically find new audio files to be modified given a download folder to search through
	4) Option to have these audio files in the download directory moved to a directory where they will be held to be edited and the option to set up this directory for manual access (should the need arise)
	5) Automatically move edited audio files with complete metadata to a destination folder, such as a folder linked to one's Google Play Music account
	   - As of now, these edited audio files will be organized into subfolders named after the date they were moved. Other organizing features may be implemented at a later date
	   
  - Other features this project must have:
    1) Local database that grows following each newly edited song (and by digesting existing collection of correctly tagged music):
       - This will include artist 'objects' that store information such as the official name of the artist, names they're also known by and a list of genres ranked by frequency to aid in autofilling the correct genre for a song by that artist
	   - This will include track/song 'objects' storing information such as the artists responsible, genre, length, album art, album name, filepath, etc.
	   - This will also include album 'objects' storing all relevant information
	   - This will also include genre 'objects' housing the official genre name and other names the genre is known by
	2) A GUI to edit the database if any errors exist
  - Nice to haves:
	1) Automatically download new songs from artists you follow on SoundCloud with the correct metadata and file format (this includes creating scripts to navigate through various 3rd party download sites that one might encounter when using SoundCloud)
	   - At the very least, the information and album art can be downloaded automatically to the local database

### Before Running
1. **Install all required dependencies with the following command:**
    ``` cmd
    pip install -r dependencies.txt
    ```

<b>Tech Stack:</b>
	- Python 3
	- PyCharm IDE
	- QtDesigner (GUI designer for Python based applications)
	   
<b>Development methodology:</b>
	For this project, I will be taking a test-driven approach. This means I  will write tests before I write the code to fulfill those tests. I am not using a testing library at the moment, as I am challenging myself in this regard (and have built a mini test library for this project and another). This is a project I work on in my spare time, thus progress to it may be intermittent.
