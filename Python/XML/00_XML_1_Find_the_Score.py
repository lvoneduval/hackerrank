def get_attr_number(node):
      return(len(node.attrib) + sum([get_attr_number(s) for s in node]))
