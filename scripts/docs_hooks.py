"""Keep repo-relative legal links useful on GitHub and the generated docs site."""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


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
