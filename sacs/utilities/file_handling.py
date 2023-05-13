from contextlib import contextmanager

@contextmanager
def fopen(filein, *args, **kwargs):
    """
    Credits:
    https://stackoverflow.com/questions/7268353/how-to-accept-both-filenames-and-file-like-objects-in-python-functions
    """
    if isinstance(filein, str):  # filename
        with open(filein, *args, **kwargs) as f:
            yield f
    else:  # file-like object
        yield filein
