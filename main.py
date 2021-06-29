import glob
import os.path

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

def isDir(path):
    return os.path.isdir(path)

def search_videos(url):
    names = []
    for extension in EXTENSIONS:
        videos = glob.glob(url + "\\*." + extension)
        for x in videos:
            names.append('- ' + str(x.replace(url+'\\', '').replace('.' + extension, '')))
    return names

def search_in_folder(url, videos):
    videos = videos + search_videos(url)
    all_files = glob.glob(url+ "\*")
    for file in all_files:
        # print(file)
        if isDir(file):
            videos = videos + search_in_folder(file, [])
    return videos

    # names = []
    # for extension in EXTENSIONS:
    #     videos = glob.glob(url + "\*." + extension)
    #     for x in videos:
    #         names.append((x.replace(url+'\\', '').replace('.' + extension, '')))
    # return names

url = ''
complete_list = search_in_folder(url, [])
for i in complete_list:
    print(i)