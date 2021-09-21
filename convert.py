from worker.convert_worker import ConvertWorker
from worker.compatibility_worker import CompatibilityWorker
from Arg import Args
import sys

def main():
    args = Args()
    args.parse()
    if args.error:
        print(args.error)
        return
    dw = CompatibilityWorker(args.args)
    dw.check()
    cw = ConvertWorker(args.args)
    cw.convert()

if __name__ == '__main__':
  main()
