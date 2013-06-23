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

APIS = {
  'Java SE 7':
     'http://docs.oracle.com/javase/7/docs/api/', 
  'Java EE 6':
    'http://docs.oracle.com/javaee/6/api/', 
  'Guava':
    'http://docs.guava-libraries.googlecode.com/git-history/release/javadoc/', 
}

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
    # sort by type name
    return sorted(index, key=lambda x: x[1])

def dump_to_file(f, index):
    data = {
        'apis': APIS,
        'types': index,
    }
    json.dump(data, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    index = load_indexes(APIS)
    dump_to_file(sys.stdout, index)

# EOF
