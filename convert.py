from worker.convert_worker import ConvertWorker
from Arg import Args
import sys

def main():
    args = Args()
    args.parse()
    if args.error:
        print(args.error)
        return
    cw = ConvertWorker(args.args)
    cw.convert()

if __name__ == '__main__':
  main()
