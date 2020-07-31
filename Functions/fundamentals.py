# optional param
def get_tag_block(content, css_class='success'):
    return f'<div class="{css_class}">{content}</div>'


# named param
def get_tag_block2(content, css_class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{css_class}">{content}</{tag}>'


# callable
def get_tag_block3(content, *args, css_class='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)
    return f'<{tag} class="{css_class}">{html}</{tag}>'


# packing & unpacking
def get_tag_list(*items):
    list = ''.join(f'<li>{item}</li>' for item in items)  # generator
    return f'<ul>{list}</ul>'


# named packing & named unpacking
def get_formatted_attrs(attrs, supported):
    return ' '.join(f'{key.split("_")[-1]}="{value}"' for key, value
                    in attrs.items() if key in supported)


block_attrs = ('block_access_key', 'block_id')


def get_tag_block4(content, *args, css_class='success', inline=False,
                   **news_attrs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else\
        content(*args, **news_attrs)
    attrs = get_formatted_attrs(news_attrs, block_attrs)
    return f'<{tag} {attrs} class="{css_class}">{html}</{tag}>'


ul_attrs = ('ul_id', 'ul_style')


def get_tag_list2(*items, **news_attrs):
    list = ''.join(f'<li>{item}</li>' for item in items)  # generator
    attrs = get_formatted_attrs(news_attrs, ul_attrs)
    return f'<ul {attrs}>{list}</ul>'


if __name__ == '__main__':
    # test with assertions
    assert get_tag_block('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    print(get_tag_block('block'))

    print(get_tag_block2('block', inline=True))
    # <span class="success">block</span>

    print(get_tag_block(get_tag_list('Alice', 'Jon', 'Peter'), css_class='info'))
    # <div class="info"><ul><li>Alice</li><li>Jon</li><li>Peter</li></ul></div>

    print(get_tag_block3(get_tag_list, 'Apple', 'Samsung', css_class='info'))
    # <div class="info'><ul><li>Apple</li><li>Samsung</li></ul></div>

    print(get_tag_block4(get_tag_list2, 'Apple', 'Samsung', css_class='info',
                         block_access_key='m', block_id='content',
                         ul_id='list'))
    # <div key="m" id="content" class="info"><ul id="list"><li>Apple</li>
    # <li>Samsung</li></ul></div>
