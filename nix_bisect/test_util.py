"""Utilities for testing a build"""


from subprocess import run, Popen, PIPE
from .git_bisect import quit_bad, quit_good, quit_skip, abort


def exit_code(command):
    """Run a shell command and return its exit code"""
    result = run(command, shell=True, encoding="utf-8")
    return result.returncode


def query_user():
    """Query the user for the bisect result and act on it"""
    while True:
        var = input("Please evaluate the run (good/bad/skip/abort): ")
        if var == "good":
            quit_good()
        if var == "bad":
            quit_bad()
        if var == "skip":
            quit_skip()
        if var == "abort":
            abort()


def shell(script):
    """Execute a shell script"""
    process = Popen("sh", stdin=PIPE)
    process.communicate(input=script)
    process.wait()
