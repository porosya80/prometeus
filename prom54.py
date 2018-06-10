def file_search(folder, filename):
    print (" Vizov FUNC")
    # print (folder)
    result = ""
    print(folder[0])
    path=folder[0]

    if filename in folder:
        print ("ok")
    for i in folder:
        # print(i)
        if i == filename:
            print("ok")
            path += "/" +filename
            print("path ok {}".format(path))
            return path
        elif isinstance(i, list):
            path +=  "/" + (file_search(i, filename))
            # print("path list {}".format(path))

    print(path)
    return path

    # print(folder.count(filename))








print(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))