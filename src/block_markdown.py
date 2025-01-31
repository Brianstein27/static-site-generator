# handles markdown blocks like heading, lists, paragraphs


def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    stripped_splits = []
    for split in splits:
        stripped_split = split.strip("\n").strip()
        if stripped_split != "":
            stripped_splits.append(stripped_split)

    return stripped_splits
