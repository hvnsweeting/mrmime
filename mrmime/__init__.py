'''
Program which help automate daily tasks. When cron is not work simply with
cmd output, this program designed to have a log file to track what changed.
Wed Apr 22 00:56:31 ICT 2015
'''

import logging
import os
import subprocess as spr
import shlex
import time


INTERVAL = 60


logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


local_repos = [
    '/Users/hvn/Github/bfs/common',
    '/Users/hvn/Github/FOSS/salt'
]


def git_fetch(repo):
    cmd = 'git fetch --all -p'
    logger.info('Fetching in %s', repo)
    os.chdir(repo)
    out = spr.check_output(shlex.split(cmd))
    logger.info(out)


def git_fetch_repos():
    for lrepo in local_repos:
        git_fetch(lrepo)


def do_jobs():
    git_fetch_repos()


def main():
    do_jobs()
    while time.sleep(INTERVAL):
        logger.debug('Waiting %d seconds', INTERVAL)
        do_jobs()


if __name__ == "__main__":
    main()
