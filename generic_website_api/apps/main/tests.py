import forgery_py


def sentences(n):
    return print(forgery_py.lorem_ipsum.sentences(n).capitalize())


sentences(1)