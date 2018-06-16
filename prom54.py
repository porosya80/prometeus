def file_search(folder, filename):

    path = folder[0]+"/"
    if filename in folder[1:]:
        return path + filename

    for item in folder[1:]:
        if isinstance(item, list) and len(item) > 1:
            pth = file_search(item, filename)
            if pth:
                path = path + pth
            return path

    return False if path == path else path




folders = ['/home',
         ['user1'],
         ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py']]],
         'work.ovpn',
         'prometheus.7z',
         ['user3', ['temp']],
         'hey.py']


print(f"RESULT {file_search(folders,'hereiam.py')}")

assert (file_search(folders,'hereiam.py')) == "/home/user2/desktop/new folder/hereiam.py"

