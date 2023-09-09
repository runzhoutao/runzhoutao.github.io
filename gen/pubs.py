import json

file = open("pubs.json")

pubs = json.load(file)

import yattag

doc, tag, text, line = yattag.Doc().ttl()

with tag("ul"):
    for pub in pubs:
        with tag("li"):
            with tag("p"):
                line("b", pub["title"])
                doc.stag("br")
                text(", ".join(pub["authors"]))
                doc.stag("br")
                text(pub["conference"] + " ")
                with tag("strong"):
                    text(f"({pub['confabbr']})")
                doc.stag("br")

                if "award" in pub:
                    line("b", pub["award"] ,style = "color: red")
                    doc.stag("br")
                # ==== links ====

                if "paper" in pub:
                    line("a", "[paper]", href = pub["paper"])
                if "code" in pub:
                    line("a", "[code]", href = pub["code"])
                if "video" in pub:
                    line("a", "[video]", href = pub["video"])
            doc.stag("br")

fout = open("test.html", "w")
fout.write(yattag.indent(doc.getvalue()))
fout.close

