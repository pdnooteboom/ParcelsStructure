try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import os
from datetime import datetime, timedelta
from progressbar import ProgressBar


class ExampleData():

    def __init__(self, url, filenames, path):
        self.url = url
        self.filenames = filenames
        self.path = path

    def download(self):
        """Function used to download example data from http://oceanparcels.org/examples-data"""
        if not os.path.exists(self.path):
                os.makedirs(self.path)

        pbar = ProgressBar()
        print("Downloading %s ..." % (self.url.split("/")[-1]))
        for filename in pbar(self.filenames):
                if not os.path.exists(os.path.join(self.path, filename)):
                        f = urlopen(self.url + "/" + filename)
                        with open(os.path.join(self.path, filename), 'wb') as temp_file:
                                temp_file.write(f.read())


dates = [datetime(2002, 1, 1) + timedelta(days=x) for x in range(0, 100)]
globfiles = [x.strftime("%Y%m%d") + "000000-GLOBCURRENT-L4-CUReul_hs-ALT_SUM-v02.0-fv01.0.nc" for x in dates]

ExampleData(url="http://oceanparcels.org/examples-data/GlobCurrent_example_data",
                filenames=globfiles,
                path="examples/GlobCurrent_example_data").download()
