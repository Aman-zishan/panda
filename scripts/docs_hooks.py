"""Keep new pages discoverable and repository-relative links useful on the site."""
import re
from copy import deepcopy
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASE_NAV = []


def on_config(config):
    global BASE_NAV
    BASE_NAV = deepcopy(config['nav'])
    return config


def on_files(files, config):
    config['nav'] = deepcopy(BASE_NAV)
    def destinations(items):
        for item in items:
            if isinstance(item, str):
                yield item
            elif isinstance(item, dict):
                yield from destinations(item.values())
            elif isinstance(item, list):
                yield from destinations(item)

    listed = set(destinations(config['nav']))
    extra_pages = []
    for file in sorted(files.documentation_pages(), key=lambda f: f.src_uri):
        if file.src_uri in listed:
            continue
        heading = re.search(r'^#\s+(.+)$', Path(file.abs_src_path).read_text(), re.MULTILINE)
        title = heading.group(1).strip() if heading else Path(file.src_uri).stem.replace('-', ' ').title()
        extra_pages.append({title: file.src_uri})
    if extra_pages:
        config['nav'].append({'More docs': extra_pages})
    return files


def on_page_markdown(markdown, page, config, files):
    def replace(match):
        target = match.group(1)
        path, separator, fragment = target.partition('#')
        resolved = (Path(page.file.abs_src_path).parent / path).resolve()
        if resolved.is_relative_to(REPO) and not resolved.is_relative_to(REPO / 'docs'):
            url = 'https://github.com/Aman-zishan/panda/blob/main/'
            return '](' + url + resolved.relative_to(REPO).as_posix() + separator + fragment + ')'
        return match.group(0)

    return re.sub(r'\]\((\.\./[^)]+)\)', replace, markdown)
