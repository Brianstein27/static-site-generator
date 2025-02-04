import os
import pathlib

from block_markdown import extract_title, markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source = open(from_path)
    markdown = source.read()
    title = extract_title(markdown)
    template = open(template_path).read()
    template = template.replace("{{ Title }}", title)
    html = template.replace("{{ Content }}", markdown_to_html_node(markdown).to_html())

    index = open(dest_path, "w")
    index.write(html)
    source.close()
    index.close()


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        generate_page(
            f"{dir_path_content}",
            template_path,
            f"{pathlib.Path(dest_dir_path).stem}.html",
        )
    else:
        paths = os.listdir(dir_path_content)
        for path in paths:
            if os.path.isfile(os.path.join(dir_path_content, path)):
                generate_page(
                    os.path.join(dir_path_content, path),
                    template_path,
                    f"{os.path.join(dest_dir_path, pathlib.Path(path).stem)}.html",
                )
            else:
                os.mkdir(os.path.join(dest_dir_path, path))
                generate_pages_recursively(
                    os.path.join(dir_path_content, path),
                    template_path,
                    os.path.join(dest_dir_path, path),
                )
