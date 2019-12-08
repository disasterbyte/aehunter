import os
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', metavar='', help='directory to search and clean')
group.add_argument('-f', '--file', metavar='', help='file to clean')
parser.add_argument('-r', '--recursive', action='store_true', help='recursively search directory')
parser.add_argument('-o', '--output', metavar='', help='write output to file')
args = parser.parse_args()

if not args.directory.endswith('\\'):
    args.directory += '\\'

def parse_file(root, filename):
    target_file = os.path.join(root, filename)
    try:
        with open(target_file, 'rb') as f:
            content = f.read()
            # true</autoElevate>
            if b'\x74\x72\x75\x65\x3c\x2f\x61\x75\x74\x6f\x45\x6c\x65\x76\x61\x74\x65\x3e' in content:
                print('    ' + target_file)
                results.append(target_file)

    except OSError as e:
        print('[!] OSError: {}'.format(e))
        pass

    except Exception as e:
        print('[!] Error: {}'.fomrat(e))
        pass

def parse_folder(directory):
    abs_dir = os.path.abspath(directory)

    if args.recursive:
        for root, subdirs, files in os.walk(abs_dir):
            for filename in files:
                if filename.endswith('.exe'):
                    parse_file(root, filename)

    else:
        for filename in os.listdir(abs_dir):
            if not os.path.isdir(filename):
                if filename.endswith('.exe'):
                    parse_file(abs_dir, filename)


results = []

if args.directory:
    parse_folder(args.directory)

elif args.file:
    parse_file(os.path.dirname(args.file), os.path.basename(args.file))

print('[+] Indentifed {} executables with autoElevate = True'.format(len(results)))

if args.output:
    print('[+] Saving output...')
    with open(args.output, 'a+') as f:
        for r in results:
            f.write('{}\n'.format(r))

print('[+] Complete!')
