"""Build Markdown docs and the product homepage into one Pages artifact."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'build' / 'site'


def main():
    # Only remove this script's generated output, never source files.
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(ROOT / 'site', OUTPUT)
    subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict'], cwd=ROOT, check=True)
    (OUTPUT / '.nojekyll').touch()
    print(f'Pages artifact: {OUTPUT}')


if __name__ == '__main__':
    main()
