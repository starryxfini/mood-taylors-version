#!/usr/bin/env python3

import argparse

def parse():
    p = argparse.ArgumentParser(prog="mood-taylors-version")
    # ...
    return p.parse_args()
