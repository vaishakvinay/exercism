def parse(markdown):
    lines = markdown.split("\n")
    result = []
    in_list = False

    def format_inline(text):


        while "__" in text:
            start = text.find("__")
            end = text.find("__", start + 2)

            if end == -1:
                break

            bold_text = text[start + 2:end]

            text = (
                text[:start]
                + f"<strong>{bold_text}</strong>"
                + text[end + 2:]
            )

      
        while "_" in text:
            start = text.find("_")
            end = text.find("_", start + 1)

            if end == -1:
                break

            italic_text = text[start + 1:end]

            text = (
                text[:start]
                + f"<em>{italic_text}</em>"
                + text[end + 1:]
            )

        return text

    for line in lines:

    
        if line.startswith("#"):
            level = 0
            while level < len(line) and line[level] == "#":
                level += 1

            if level <= 6 and level < len(line) and line[level] == " ":
                if in_list:
                    result.append("</ul>")
                    in_list = False

                text = line[level:].strip()
                text = format_inline(text)
                result.append(f"<h{level}>{text}</h{level}>")
            else:
                if in_list:
                    result.append("</ul>")
                    in_list = False

                text = format_inline(line)
                result.append(f"<p>{text}</p>")

    
        elif line.startswith("* "):
            if not in_list:
                result.append("<ul>")
                in_list = True

            item_text = line[2:]
            item_text = format_inline(item_text)
            result.append(f"<li>{item_text}</li>")

        
        else:
            if in_list:
                result.append("</ul>")
                in_list = False

            text = format_inline(line)
            result.append(f"<p>{text}</p>")

   
    if in_list:
        result.append("</ul>")

    return "".join(result)