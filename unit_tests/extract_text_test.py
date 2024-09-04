import unittest
import extract_text

_TEST_PHRASE = "unit testing is your friend"

class ChunkingTest(unittest.TestCase):

    def test_chunking_ok(self):
        expected = ["unit testing", "is your", "friend"]
        self.assertEqual(extract_text.chunking(_TEST_PHRASE, 2), expected)

    def test_chunking_input_shorter_than_token_count(self):
        expected = [_TEST_PHRASE]
        self.assertEqual(extract_text.chunking(_TEST_PHRASE, 10), expected)

    def test_chunking_empty_string(self):
        expected = []
        self.assertEqual(extract_text.chunking("", 2), expected)

    def test_chunking_non_positive_token_count_error(self):
        with self.assertRaises(ValueError):
            extract_text.chunking(_TEST_PHRASE, 0)

        with self.assertRaises(ValueError):
            extract_text.chunking(_TEST_PHRASE, -3)


if __name__ == '__main__':
    unittest.main()
