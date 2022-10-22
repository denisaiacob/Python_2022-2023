'''
The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
Build and return a string that represents the corresponding XML element.
Ex:"<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
'''


def build_xml_element(tag, content, elements):
    xmlString = "\"<" + tag + " "
    for i in elements:
        xmlString = xmlString + i + "=\\\"" + elements.get(i) + " \\ \""
    xmlString=xmlString+"> "+content+" </"+tag+">\""
    return xmlString


if __name__ == '__main__':
    tag = "a"
    content = "Hello there"
    elements = dict(href="http://python.org", _class="my-link", id="someid")
    print(build_xml_element(tag, content, elements))
