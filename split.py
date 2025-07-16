from pathlib import Path


def main():
    all_chapter = Path('0.md').read_text('utf-8', 'replace').split('\n# ')
    all_chapter = {i: '# ' + c for i, c in enumerate(all_chapter, 1)}
    all_chapter[1] = all_chapter[1][2:]

    for chapter in Path('.').glob('[0-9][0-9]_*.md'):
        chapter.write_text(all_chapter[int(chapter.name[:2])], 'utf-8', 'replace')


if __name__ == '__main__':
    main()
