import re
import argparse

parser = argparse.ArgumentParser(description='Recieves file and creates a .sanitized file')
parser.add_argument("-i", dest="filename", required=False,
                    help="input file with two matrices")

args = parser.parse_args()

content = ""
if args.filename:
    with open(args.filename) as f:
        content = "".join(f.readlines())
else:
    parser.print_help()
    print "\r\nEXAMPLE for output:"
    content = "GET http://domain.com/?xxx=50.123&latA=50.8392 HTTP/1.1|109|200" \
           + "\r\n" + "GET http://domain.com/request?lon=-9.233333333333333&lat=3.7425&timeslot=today HTTP/1.1|123|200"

p = re.compile('=(\-?\d{1,}(\.\d+){1,})')
ret = p.sub("=XX.XX", content)

if args.filename:
    sanitizedFilename = args.filename + ".sanitized"
    with open(sanitizedFilename, 'w') as fw:
        fw.write(ret)

    print "Written succesully to -> " + sanitizedFilename
else:
    print ret