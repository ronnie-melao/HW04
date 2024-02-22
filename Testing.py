import unittest

from HW04a import getUserRepoCommits

class TestHW04a(unittest.TestCase):

    def testMyRepo(self): 
        self.assertNotEqual(getUserRepoCommits('ronnie-melao'),'Repo: CS-546 Number of commits: 30\nRepo: HW00-Tools_Setup Number of commits: 1\nRepo: HW01-Testing-triangle-classification Number of commits: 1\nRepo: HW02 Number of commits: 13\nRepo: HW04 Number of commits: 2','Wrong commits')
        
    def testRichKempinski(self): 
        self.assertNotEqual(getUserRepoCommits('richkempinski'),'Repo: csp Number of commits: 2\nRepo: hellogitworld Number of commits: 30\nRepo: helloworld Number of commits: 6\nRepo: Mocks Number of commits: 10\nRepo: Project1 Number of commits: 2\nRepo: richkempinski.github.io Number of commits: 9\nRepo: threads-of-life Number of commits: 1\nRepo: try_nbdev Number of commits: \nRepo: try_nbdev2 Number of commits: 5','Wrong commits')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()