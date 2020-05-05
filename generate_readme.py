# -*- coding: utf-8 -*-

import re
import os.path
import string

RE_BEGIN_HELP = re.compile(r'^\[//\]: # \(begin generate_help: (?P<filename>.+\.py)\)$')
RE_END_HELP = re.compile(r'^\[//\]: # \(end generate_help\)$')

RE_BEGIN_TOC = re.compile(r'^\[//\]: # \(begin generate_toc\)$')
RE_END_TOC = re.compile(r'^\[//\]: # \(end generate_toc\)$')

LINK_TOC = u"[📖](#table-of-contents)".encode('utf-8')


def get_help(filename):
    try:
        basename, ext = os.path.splitext(filename)
        module = __import__(basename)
        module.parser.prog = filename
        return module.parser.format_help()
    except AttributeError:
        import subprocess
        return subprocess.check_output(['python2', filename, '-h'])


def generate_toc(toc_names):
    toc = ["## Table of Contents\n\n"]
    for i, toc_name in enumerate(toc_names, start=1):
        toc.append("{i}. [{full_name}](#{slug_name}-)\n".format(
            i=i,
            full_name=toc_name,
            slug_name=toc_name.translate(None, string.punctuation).replace(' ', '-').lower(),
        ).encode())
    return toc + ["\n"]


def main():
    lst_readme = []
    help_detected = False
    help_current = ''
    toc_names = []
    with open('README.md', 'r') as readme:
        for line in readme:
            if line.startswith('## '):
                if "## Table of Contents" in line:
                    continue
                toc_names.append(line[3:].split(LINK_TOC)[0].strip())
                if LINK_TOC not in line:
                    lst_readme.append(line.rstrip() + ' ' + LINK_TOC + '\n')
                else:
                    lst_readme.append(line)
                continue

            match_begin = RE_BEGIN_HELP.match(line)
            match_end = RE_END_HELP.match(line)
            if match_begin is not None:
                help_detected = True
                filename = match_begin.groupdict().get('filename')
                help_current = get_help(filename)
                lst_readme.append(line)
            elif match_end is not None:
                help_detected = False
                lst_readme.append("""### Usage\n```\n{}\n```\n""".format(help_current))
                lst_readme.append(line)
            elif not help_detected:
                lst_readme.append(line)

    idx_toc_begin, idx_toc_end = -1, -1
    for idx, line in enumerate(lst_readme):
        match_begin = RE_BEGIN_TOC.match(line)
        if match_begin is not None:
            idx_toc_begin = idx
            continue

        match_end = RE_END_TOC.match(line)
        if match_end is not None:
            idx_toc_end = idx
            break

    if idx_toc_begin != -1 and idx_toc_end != -1:
        lst_readme = lst_readme[:idx_toc_begin+1] + generate_toc(toc_names) + lst_readme[idx_toc_end:]

    with open('README.md', 'wb') as readme_out:
        readme_out.write(''.join(lst_readme))


if __name__ == '__main__':
    main()
