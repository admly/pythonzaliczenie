import re

file_to_write = open("output.txt", 'w', encoding="utf8")


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    file_to_write.write(cleantext)
    f.close()


f = open("./strona.html", encoding="utf8")
clean_html(f.read())
