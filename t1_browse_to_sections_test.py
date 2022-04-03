from .browse_to_sections import find_name


# note that test reveals tha script does not always work as expected
# TODO cover edge cases
@pytest.mark.parametrize('input,                                   expected_output',
                         [['<h2 id="cosmos-songs_1">'
                           '<strong>Cosmos Songs</strong></h2>',   ''],
                          ['<h2 id="cosmos-books_1">'
                           '<a name="cosmos_books"></a>'
                           '<strong>Cosmos Books</stro',           '="cosmos_books'],
                          ['<h2 id=\"atlantic-ocean\">'
                           '<a name="atlantic_ocean"></a>' 
                           '<strong>Atlantic Ocean</strong></h2>', '"><a name="atlantic_ocean']])
def test1_find_name(input, expected_output):
    assert find_name('name', input) == expected_output
