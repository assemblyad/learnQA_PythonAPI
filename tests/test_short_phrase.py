"""
phrase = input("Set a phrase: ")
print (len(phrase))

class TestShortPhrase:
    def test_phrase_len(self):
        expected_len = 15
        assert len(phrase) <= expected_len, f"The phrase length should be less than {expected_len}"
"""