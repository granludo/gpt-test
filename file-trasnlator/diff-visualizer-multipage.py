import difflib
import os

def compare_files_to_html_paged(fromfile, tofile, output_folder, lines_per_page=50):
    with open(fromfile, 'r', encoding='utf-8') as f:
        fromlines = f.readlines()

    with open(tofile, 'r', encoding='utf-8') as f:
        tolines = f.readlines()

    html_diff = difflib.HtmlDiff()
    html_diff._file_template = html_diff._file_template.replace(
        '<style type="text/css">',
        '<style type="text/css">\n.diff td { width: 45%; }'
    )

    os.makedirs(output_folder, exist_ok=True)

    num_pages = max(len(fromlines), len(tolines)) // lines_per_page + 1
    for page in range(num_pages):
        start_line = page * lines_per_page
        end_line = start_line + lines_per_page

        diff = html_diff.make_file(fromlines[start_line:end_line], tolines[start_line:end_line],
                                   fromfile, tofile, context=False, numlines=lines_per_page)

        pagination = "<div style='text-align:center; margin: 20px;'>"
        if page > 0:
            prev_file = f"page_{page}.html"
            pagination += f"<a href='{prev_file}'>&lt;&lt; Prev</a>"

        if page < num_pages - 1:
            if page > 0:
                pagination += " | "
            next_file = f"page_{page + 2}.html"
            pagination += f"<a href='{next_file}'>Next &gt;&gt;</a>"
        pagination += "</div>"

        diff = diff.replace("</body>", pagination + "</body>")

        output_file = os.path.join(output_folder, f"page_{page + 1}.html")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(diff)

# Ejemplo de uso:
fromfile = 'document_v1.txt'
tofile = 'document_v2.txt'
output_folder = 'comparison_pages'

compare_files_to_html_paged(fromfile, tofile, output_folder)
