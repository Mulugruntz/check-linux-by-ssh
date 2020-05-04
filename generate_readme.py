import re
import os.path

RE_BEGIN_HELP = re.compile(r'^\[//\]: # \(begin generate_help: (?P<filename>.+\.py)\)$')
RE_END_HELP = re.compile(r'^\[//\]: # \(end generate_help\)$')


def get_help(filename):
    try:
        basename, ext = os.path.splitext(filename)
        module = __import__(basename)
        module.parser.prog = filename
        return module.parser.format_help()
    except AttributeError:
        import subprocess
        return subprocess.check_output(['python2', filename, '-h'])


def main():
    str_readme = ''
    help_detected = False
    help_current = ''
    with open('README.md', 'r') as readme:
        for line in readme:
            match_begin = RE_BEGIN_HELP.match(line)
            match_end = RE_END_HELP.match(line)
            if match_begin is not None:
                help_detected = True
                filename = match_begin.groupdict().get('filename')
                help_current = get_help(filename)
                str_readme += line
            elif match_end is not None:
                help_detected = False
                str_readme += """### Usage\n```\n{}\n```\n""".format(help_current)
                str_readme += line
            elif not help_detected:
                str_readme += line

    with open('README.md', 'w') as readme_out:
        readme_out.write(str_readme)


if __name__ == '__main__':
    main()
