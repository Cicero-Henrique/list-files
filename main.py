import glob
import os.path
import os

EXTENSIONS = [
    'webm',
    'mkv',
    'flv',
    'avi',
    'wmv',
    'amv',
    'mp4',
    'flv'
]

def goDeep(files):
    for file in files:
        if isDir(file):
            search_in_folder()

def isValidUrl(url):
    for letter in url:
        if letter == '[':
            url = url.replace(letter, '(')
        if letter == ']':
            url = url.replace(letter, ')')
    return url

def isDir(path):
    return os.path.isdir(path)

def search_videos(url):
    names = []
    for extension in EXTENSIONS:
        videos = glob.glob(url + "\\*." + extension)
        for x in videos:
            names.append('- ' + str(x.replace(url+'\\', '').replace('.' + extension, '')))
    return names

def search_in_folder(old_url, videos):
    url = isValidUrl(old_url)
    if url != old_url:
        os.rename(old_url, url)
    videos = videos + search_videos(url)
    all_files = glob.glob(url+ "\*")
    for file in all_files:
        if isDir(file):
            videos = videos + search_in_folder(file, [])
    return videos

url = ''
complete_list = search_in_folder(url, [])
for i in complete_list:
    print(i)