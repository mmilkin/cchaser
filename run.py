#!flask/bin/python
import argparse
from chaser import app
from werkzeug.serving import run_simple
from settings.settings import DEBUG


def main(args):
    threads = args.threads
    threaded = True if threads else False
    run_simple(args.host, args.port, app, use_debugger=DEBUG, threaded=threaded)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', default=False)
    parser.add_argument('-o', '--host', default='localhost')
    parser.add_argument('-p', '--port', type=int, default=8000)
    main(parser.parse_args())
