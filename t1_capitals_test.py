import re

import pytest

from .Capitals import add_links_to_capitals, enrich_countries_with_hyperlinks


@pytest.fixture
def type_of_file(request):
    file_name = request.param
    if file_name == 'empty_guide.md':
        return 'This is the first line we want to test\n'\
               'This is the second line  to test.\n'\
               'This is the third and last line to check'
    elif file_name == 'guide_with_capitals.md':
        return '**Capital:** Kairo\n'\
               '**Capital:** Jakarta\n'\
               '**Capital:** Madrid'


def create_fake_guide_file(file_name, test_content):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(test_content)
        f.close()


@pytest.mark.parametrize('type_of_file,              name_of_file,             is_modified',
                         [['empty_guide.md',         'empty_guide.md',         False],
                          ['guide_with_capitals.md', 'guide_with_capitals.md', True]],
                         indirect=['type_of_file'])
def test1_check_capitals_script(type_of_file, name_of_file, is_modified):
    original_guide_file = type_of_file
    create_fake_guide_file(name_of_file, type_of_file)
    new_guide_file = add_links_to_capitals(name_of_file)
    assert (original_guide_file == new_guide_file) is not is_modified


@pytest.mark.parametrize('type_of_file,              name_of_file,             is_modified',
                         [['empty_guide.md',         'empty_guide.md',         False],
                          ['guide_with_capitals.md', 'guide_with_capitals.md', True]],
                         indirect=['type_of_file'])
def test2_add_links_to_capitals(type_of_file, name_of_file, is_modified):
    enrich_countries_with_hyperlinks(name_of_file)
    lines_of_new_guide_file = list(open(name_of_file, "r", encoding="utf-8"))
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s" \
            r"()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{}" \
            r";:'\".,<>?«»“”‘’]))"
    assert all(bool(re.findall(regex, lines_of_new_guide_file[line_number])) for 
               line_number in range(0, 3)) is is_modified
