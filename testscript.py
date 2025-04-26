import unittest
import os
from script import download_file

class TestDownloadFunctions(unittest.TestCase):
    def test_download_file(self):
        # Use the GitHub .gitignore file URL
        test_url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
        destination = "test_file.gitignore"
        
        # Call the download function
        download_file(test_url, destination)
        
        # Check if the file now exists on your computer
        self.assertTrue(os.path.exists(destination))
        
        # Clean up: delete the file after the test
        os.remove(destination)
        
if __name__ == "__main__":
    unittest.main()