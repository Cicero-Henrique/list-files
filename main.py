import glob
import os

def get_extensions():
    extensions = []
    f = open('list.txt', 'r')
    for line in f:
        extensions.append(line.strip('\n'))
    f.close()
    return extensions

def write_in_file(files):
    f = open('films.txt', 'x')
    for x in files:
        f.write(x +'\n')
        # extensions.append(line.strip('\n'))
    f.close()

def validateFolderName(original_url):
    url = original_url
    for letter in url:
        if letter == '[':
            url = url.replace(letter, '(')
        if letter == ']':
            url = url.replace(letter, ')')
    if url != original_url:
        os.rename(original_url, url)
    return url

def isDir(path):
    return os.path.isdir(path)

def search_videos(url, dashes):
    names = []
    for extension in EXTENSIONS:
        videos = glob.glob(url + "\\*." + extension)
        for x in videos:
            names.append(dashes + '- ' + str(x.replace(url+'\\', '').replace('.' + extension, '')))
    if len(names) != 0:
        names = [dashes + ' ' + url] + names
    return names

def search_in_folder(old_url, videos, dashes):
    url = validateFolderName(old_url)
    videos = videos + search_videos(url, dashes)
    dashes = dashes + '-'
    all_files = glob.glob(url+ "\*")
    for file in all_files:
        if isDir(file):
            videos = videos + search_in_folder(file, [], dashes)
    return videos

EXTENSIONS = get_extensions()
url = ''
complete_list = search_in_folder(url, [], '-')
write_in_file(complete_list)
# for i in complete_list:
#     print(i)
