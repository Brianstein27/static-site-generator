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
