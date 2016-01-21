from PIL import Image
import argparse
import requests
from io import BytesIO

parser = argparse.ArgumentParser(description='Use to specify a collection')
parser.add_argument("-p", "--pid", dest="pid", help="pid that you want", required=True)
parser.add_argument("-l", "--link", dest="fedoraurl", help="url of fedora instance")
parser.add_argument("-f", "--filename", dest="destfilename", help="name of file you want to save your set to")
args = parser.parse_args()

def harvestobject(pid, fedoraurl, filename):
    requesturl = fedoraurl + '/objects/' + pid +'/datastreams/OBJ/content'
    r = requests.get(requesturl)
    if r.status_code == 200:
        imageFile = r.content
        img = Image.open(BytesIO(imageFile))
        print('Saving image')
        img.save('temp/' + filename)
    else:
        print('Could not find object')
        print(requesturl)


if __name__ == "__main__":

    # Defaults
    fedoraurl = 'http://digital.lib.utk.edu:8080/fedora'
    pid = ''
    filename = "mytif.tif"

    if args.fedoraurl:
        fedoraurl = "http://{0}".format(args.fedoraurl)
    if args.pid:
        pid = args.pid
    if args.destfilename:
        filename = "{0}.txt".format(args.destfilename)

harvestobject(pid, fedoraurl, filename)