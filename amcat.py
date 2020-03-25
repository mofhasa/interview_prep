import unittest
from ds import TupleMaxHeapQueue

#Problem 1 Helper functions
def isAlphabet(c):
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        return True
    else:
        return False
def getFrequencyDictForKeyWords(reviews, keywords):
    freqTab = {}
    for r in reviews:
        words = r.split(" ")

        num_of_words = len(words)
        i = 0
        while i < num_of_words:
            if not isAlphabet(words[i][0]):
                words[i] = words[i][1:]

            if not isAlphabet(words[i][-1]):
                words[i] = words[i][:-1]

            test_word = words[i].lower()
            if test_word in keywords:
               if test_word in freqTab.keys():
                   freqTab[test_word] += 1
               else:
                   freqTab[test_word] = 0
                   freqTab[test_word] += 1
            i += 1
    return freqTab

class Solution:

    '''
        Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to
        least frequently mentioned.

        The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews,
        sort alphabetically.
    '''

    def problemOne(self, k, keywords, reviews):
        freqTab = getFrequencyDictForKeyWords(reviews, keywords)
        heap = TupleMaxHeapQueue()

        ret_list = []
        for keyw in freqTab.keys():
            heap.push_item((keyw, freqTab[keyw]))
        result = heap.f_k_ten(k)

        for r in result:
            ret_list.append(r[1])

        return ret_list

    '''
        Given an array of strings products and a string searchWord. We want to design a system that suggests at most 
        three product names from products after each character of searchWord is typed. Suggested products should have 
        common prefix with the searchWord. If there are more than three products with a common prefix return the three 
        lexicographically minimums products.
            
        Return list of lists of the suggested products after each character of searchWord is typed. 
    '''
    def problemTwo(self, products: [str], searchWord: str) -> [[str]]:
        return None
    '''
        Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human 
        beings into zombies every hour. Find out how many hours does it take to infect all humans?
    '''
    def problemThree(self, matrix):
        return None
    '''
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water 
        and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid 
        are all surrounded by water.
    '''
    def problemFour(self, map):
        return None
    '''
        Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

        Conditions:
        
        You will pick exactly 2 numbers.
        You cannot pick the same element twice.
        If you have muliple pairs, select the pair with the largest number.
    '''
    def problemFive(self, nums, target):
        return None
    '''
        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
        
        Return a deep copy of the list.
        
        The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
        
        val: an integer representing Node.val
        random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
    '''
    def problemSix(self, head):
        return None
    '''
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together 
        the nodes of the first two lists.
    '''
    def problemSeven(self, l1, l2):
        return None
    '''
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        
        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.
    '''
    def problemEight(self, matrix):
        return None
    '''
        Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the 
        user has listened to as values.

        Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs 
        within that genre as values. The song can only belong to only one genre.
        
        The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a 
        list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more 
        than one favorite genre if he/she has listened to the same number of songs per each of the genres.
    '''
    def problemNine(self, userSongs, songGenres):
        return None
    '''
        Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    '''
    def problemTen(self, num):
        return None

class AMCATTests(unittest.TestCase):

    def test_one_problemOne(self):
        k = 2
        keywords = ["anacell", "cetracular", "betacellular"]
        reviews = [
            "Anacell provides the best services in the city",
            "betacellular has awesome services",
            "Best services provided by anacell, everyone should use anacell",
        ]
        output = ["anacell", "betacellular"]
        solutions = Solution()
        result = solutions.problemOne(k, keywords, reviews)
        self.assertListEqual(output, result)
    def test_two_one_problemOne(self):
        k = 2
        keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
        reviews = [
            "I love anacell Best services; Best services provided by anacell",
            "betacellular has great services",
            "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell",
            "Betacellular is better than deltacellular.",
        ]
        output = ["betacellular", "anacell"]
        solutions = Solution()
        result = solutions.problemOne(k, keywords, reviews)
        self.assertListEqual(output, result)
    # def test_one_problemTwo(self):
    #     products = ["mobile","mouse","moneypot","monitor","mousepad"]
    #     searchWord = "mouse"
    #     output = [
    #         ["mobile","moneypot","monitor"],
    #         ["mobile","moneypot","monitor"],
    #         ["mouse","mousepad"],
    #         ["mouse","mousepad"],
    #         ["mouse","mousepad"]
    #     ]
    #     solutions = Solution()
    #     result = solutions.problemTwo(products, searchWord)
    #     self.assertListEqual(result, output)
    # def test_two_problemTwo(self):
    #     products = ["bags","baggage","banner","box","cloths"]
    #     searchWord = "bags"
    #     output = [
    #         ["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]
    #     ]
    #     solutions = Solution()
    #     result = solutions.problemTwo(products, searchWord)
    #     self.assertListEqual(result, output)
    # def test_three_problemTwo(self):
    #     products = ["havana"]
    #     searchWord = "havana"
    #     output = [
    #         ["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]
    #     ]
    #     solutions = Solution()
    #     result = solutions.problemTwo(products, searchWord)
    #     self.assertListEqual(result, output)
    # def test_one_problemThree(self):
    #     matrix = [[0, 1, 1, 0, 1],
    #      [0, 1, 0, 1, 0],
    #      [0, 0, 0, 0, 1],
    #      [0, 1, 0, 0, 0]]
    #
    #     solutions = Solution()
    #     hours = solutions.problemThree(matrix)
    #     self.assertEqual(hours, 2)
    # def test_one_problemFour(self):
    #     map =[
    #         [1,1,1,1,0],
    #         [1,1,0,1,0],
    #         [1,1,0,0,0],
    #         [0,0,0,0,0]
    #     ]
    #
    #     solutions = Solution()
    #     islands = solutions.problemFour(map)
    #     self.assertEqual(1, islands)
    # def test_one_problemFour(self):
    #     map =[
    #         [1,1,0,0,0]
    #         [1,1,0,0,0]
    #         [0,0,1,0,0]
    #         [0,0,0,1,1]
    #     ]
    #
    #     solutions = Solution()
    #     islands = solutions.problemFour(map)
    #     self.assertEqual(3, islands)
    # def test_one_problemFive(self):
    #     nums = [1, 10, 25, 35, 60]
    #     target = 90
    #     output = [2, 3]
    #     solutions = Solution()
    #     result = solutions.problemFive(nums, target)
    #     self.assertListEqual(output, result)
    # def test_two_problemFive(self):
    #     nums = [20, 50, 40, 25, 30, 10]
    #     target = 90
    #     output = [1, 5]
    #     solutions = Solution()
    #     result = solutions.problemFive(nums, target)
    #     self.assertListEqual(output, result)
    # def test_one_problemSix(self):
    #     head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    #     output = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    #     solutions = Solution()
    #     result = solutions.problemSix(head)
    #     self.assertListEqual(output, result)
    # def test_two_problemSix(self):
    #     head = [[1,1],[2,1]]
    #     output = [[1,1],[2,1]]
    #     solutions = Solution()
    #     result = solutions.problemSix(head)
    #     self.assertListEqual(output, result)
    # def test_three_problemSix(self):
    #     head = [[3,None],[3,0],[3,None]]
    #     output = [[3,None],[3,0],[3,None]]
    #     solutions = Solution()
    #     result = solutions.problemSix(head)
    #     self.assertListEqual(output, result)
    # def test_four_problemSix(self):
    #     head = []
    #     output = []
    #     solutions = Solution()
    #     result = solutions.problemSix(head)
    #     self.assertListEqual(output, result)
    # def test_one_problemEight(self):
    #     matrix = [
    #       [1,   4,  7, 11, 15],
    #       [2,   5,  8, 12, 19],
    #       [3,   6,  9, 16, 22],
    #       [10, 13, 14, 17, 24],
    #       [18, 21, 23, 26, 30]
    #     ]
    #     target = 5
    #     output = True
    #     solutions = Solution()
    #     result = solutions.problemEight(matrix)
    #     self.assertEquals(result, output)
    # def test_two_problemEight(self):
    #     matrix = [
    #       [1,   4,  7, 11, 15],
    #       [2,   5,  8, 12, 19],
    #       [3,   6,  9, 16, 22],
    #       [10, 13, 14, 17, 24],
    #       [18, 21, 23, 26, 30]
    #     ]
    #     target = 20
    #     output = False
    #     solutions = Solution()
    #     result = solutions.problemEight(matrix)
    #     self.assertEquals(result, output)
    # def test_one_problemNine(self):
    #     userSongs = {
    #                     "David": ["song1", "song2", "song3", "song4", "song8"],
    #                     "Emma": ["song5", "song6", "song7"]
    #                 },
    #     songGenres = {
    #         "Rock": ["song1", "song3"],
    #         "Dubstep": ["song7"],
    #         "Techno": ["song2", "song4"],
    #         "Pop": ["song5", "song6"],
    #         "Jazz": ["song8", "song9"]
    #     }
    #     output = {
    #        "David": ["Rock", "Techno"],
    #        "Emma":  ["Pop"]
    #     }
    #     solutions = Solution()
    #     result = solutions.problemNine(userSongs, songGenres)
    #     self.assertDictEqual(result, output)
    # def test_two_problemNine(self):
    #     userSongs = {
    #        "David": ["song1", "song2"],
    #        "Emma":  ["song3", "song4"]
    #     },
    #     songGenres = {}
    #     output = {
    #        "David": [],
    #        "Emma":  []
    #     }
    #     solutions = Solution()
    #     result = solutions.problemNine(userSongs, songGenres)
    #     self.assertDictEqual(result, output)
    # def test_one_problemTen(self):
    #     num = 3
    #     output = [
    #      [ 1, 2, 3 ],
    #      [ 8, 9, 4 ],
    #      [ 7, 6, 5 ]
    #     ]
    #     solutions = Solution()
    #     result = solutions.problemTen(num)
    #     self.assertListEqual(result, output)

if __name__ == '__main__':
    unittest.main()