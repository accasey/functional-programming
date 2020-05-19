def tag_old(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag(name, **attributes):
    result = '<' + name
    for k, v in attributes.items():
        result += f' {k}="{v}"'
    result += '>'
    return result

print(tag('img', src='Monet.jpg', alt='Sunrise by Claude Monet', border=1))