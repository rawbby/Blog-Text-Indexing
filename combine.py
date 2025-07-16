from pathlib import Path


def main():
    all_chapter = []
    for chapter in Path('.').glob('[0-9][0-9]_*.md'):
        all_chapter.append(chapter.read_text(encoding="utf-8", errors="replace"))
    Path('0.md').write_text('\n'.join(all_chapter), encoding="utf-8", errors="replace")


if __name__ == '__main__':
    main()
