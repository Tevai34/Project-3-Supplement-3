import unittest
import os
from script import download_file

class TestDownloadFunctions(unittest.TestCase):
    def test_download_file(self):
        test_url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
        destination = "test_file.gitignore"
        
        download_file(test_url, destination)
        self.assertTrue(os.path.exists(destination))
        os.remove(destination)
        
if __name__ == "__main__":
    unittest.main()