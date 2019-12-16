import re
import subprocess
import sys
from subprocess import PIPE, STDOUT


def command_push(new_tag):
    """Create new tag in git-repository."""
    subprocess.run(["git", "tag", new_tag])


def command_get():
    """Get tag from git-repository."""
    tag = (subprocess.run(["git", "tag"], stdout=PIPE, stderr=STDOUT)).stdout.decode('utf-8')
    if re.search("^janus/v", tag):
        print(tag.strip('janus/v'))
    else:
        print(tag + 'abracadabra')


def command_build_type():
    """Print the type of tag from git-repository."""
    tag = (subprocess.run(["git", "tag"], stdout=PIPE, stderr=STDOUT)).stdout.decode('utf-8')
    if re.search("^janus/v", tag) and re.search("[0-9]$", tag):
            print('production')
    elif 'janus/v' in tag:
            print('development')
    else:
        print('This tag do not belong to Janus')
        raise ValueError


if __name__ == "__main__":
    command = sys.argv[1]

    if command == "push" and len(sys.argv) == 3:
        var = 'janus/v' + sys.argv[2].strip()
        command_push(var)

    elif command == "get":
        command_get()

    elif command == "get-build-type":
        command_build_type()

    else:
        print('make correct input')
