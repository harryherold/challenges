import xml.etree.ElementTree as ET
from collections import Counter

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
REPLACE_CHARS = str.maketrans('-', ' ')

def get_tags() -> list:
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tree = ET.parse('rss.xml')
    root = tree.getroot()
    return [tag.text.translate(REPLACE_CHARS).lower() for tag in root.iter('category')]



def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    pass


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
