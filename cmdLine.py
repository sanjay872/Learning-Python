#accepting argument through cmd line
import sys,argparse

#using sys module
# name=sys.argv[1]
# print(name)

parser=argparse.ArgumentParser(
    description="This program prints my name"
)
parser.add_argument('-n','--name',metavar='name',required=True,choice={'san','sanjay'},help="to get name")
arg=parser.parse_args()
print(arg.name)