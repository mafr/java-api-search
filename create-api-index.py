#! /usr/bin/env python3
#
# Download lists of API elements from a javadoc API index.
#
# Usage: create-json-db.py > api-index.js
#
import json
import re
import sys
import urllib.request
import configparser


def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    apis = { }
    for key in config.sections():
        section = config[key]
        apis[section['label']] = section['url']
    return apis

RE = re.compile(
    r'<a href="(.*?)" title="(.*?) in (.*?)">(?:<i>)?(.*?)(?:</i>)?</a>',
    re.IGNORECASE
)

def load_index(url, label):
    index = [ ]
    with urllib.request.urlopen(url + 'allclasses-noframe.html') as f:
        for line in f:
            m = RE.search(line.decode('utf-8'))
            if not m:
                continue
            href, jtype, pkg, name = m.groups()
            index.append((jtype, name, pkg, url+href, label))
    return index

def load_indexes(config):
    index = [ ]
    for label, url in config.items():
        r = load_index(url, label)
        print("Got {} entries from {}".format(len(r), label), file=sys.stderr)
        index.extend(r)
    return sorted(index, key=lambda x: x[1]) # sort by type name

def dump_to_file(f, config, index):
    data = {
        'apis': config,
        'types': index,
    }
    json.dump(data, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    config = load_config('config.ini')
    index = load_indexes(config)
    dump_to_file(sys.stdout, config, index)

# EOF
