all_lines = list(open("guide.md", "r", encoding="utf-8"))
new_lines = ""
for line in all_lines:
    if "**Capital:**" in line:
        sp = line.strip().split(" ", 1)
        if "http" in sp[1]:
            new_lines += line
        else:
            new_lines += sp[0] + " [" + sp[1] + "]" \
                         + "(" + "https://www.google.com/maps/search/" + sp[1].replace(" ", "%20") + ")" + "\n"
    else:
        new_lines += line
    return new_lines  

def enrich_countries_with_hyperlinks(file_name="guide.md"):
    with open("guide.md", "w", encoding="utf-8") as f:
        new_lines = add_links_to_capitals(file_name)
        f.write(new_lines)
        f.close()
    return new_lines

with open("guide.md", "w", encoding="utf-8") as f:
    f.write(new_lines)
