import os


def project(
    project: str
    , app: str
):
    
    try:
        if not os.path.isdir():
            os.makedirs()
    except OSError:
        print('Error:Creating tasks directory.')

def app():
    pass
