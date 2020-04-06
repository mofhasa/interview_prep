import unittest
from ds import TupleMaxHeapQueue, Graph_und
import heapq, math
import queue


def calculateDistance(A):
    return math.sqrt((A[0] ** 2) + (A[1] ** 2))

#Problem 1 Helper functions
def isAlphabet(c):
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        return True
    else:
        return False
def getFrequencyDictForKeyWords(reviews, keywords):
    freqTab = {}
    for r in reviews:
        words = list(set(r.split(" ")))

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
#Problem 3 Helper functions
def initializeQueue(q, matrix):
    i = 0
    j = 0
    for x in matrix:
        j=0
        for y in x:
            if y == 1:
                q.put((i,j))
            j+=1
        i+=1

    q.put((-1,-1))

def safeIndex(i, n, matrix):
    if (i[0] + n[0] < 0 or i[0] + n[0] >= len(matrix)) or (i[1] + n[1] < 0 or i[1] + n[1] >= len(matrix[i[0]])):
        return False
    else:
        return True

def markAndAddNeighbors(q, matrix):
    neigh = [(0, -1), (0, 1), (-1, 0), (1,0)]
    while q.queue[0] != (-1,-1):
        curr_i = q.get()
        for n in neigh:
            if safeIndex(curr_i, n, matrix):
                if matrix[curr_i[0]+n[0]][curr_i[1]+n[1]] == 0:
                    matrix[curr_i[0]+n[0]][curr_i[1]+n[1]] = 1
                    q.put((curr_i[0]+n[0],curr_i[1]+n[1]))
    q.get()
    q.put((-1,-1))

#Problem 4 Helper functions
def safeIndex_islands(map, i, j, cols , rows, visited):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return False
    else:
        if visited[i][j] == 0 and map[i][j] == 1:
            return True
        else:
            return False

def DFS_islands(i, j, matrix, visited, cols_guide, rows_guide, cols, rows):
    visited[i][j] = 1

    for x in range(4):
        if safeIndex_islands(matrix, i+rows_guide[x], j+cols_guide[x], cols, rows, visited) == True:
            DFS_islands(i+rows_guide[x], j+cols_guide[x], matrix, visited, cols_guide, rows_guide, cols, rows)

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
    def problemTwo(self, products, searchWord):
        i = 1
        searchWLen = len(searchWord)
        results = []

        while i <= searchWLen:
            search_curr = searchWord[0:i]
            candidates = []
            for p in products:
                if p.startswith(search_curr):
                    heapq.heappush(candidates, p)

            top3 = []
            for j in range(3):
                top3.append(heapq.heappop(candidates))
                if len(candidates) == 0:
                    break
            results.append(top3)
            i+=1
        return results

    '''
        Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human 
        beings into zombies every hour. Find out how many hours does it take to infect all humans?
    '''
    def problemThree(self, matrix):
        q = queue.Queue()
        initializeQueue(q, matrix)
        hours = 0
        while q.queue[0] != (-1,-1):
            markAndAddNeighbors(q, matrix)
            if len(q.queue) != 1:
                hours += 1
        return hours

    '''
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water 
        and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid 
        are all surrounded by water.
    '''
    def problemFour(self, map):
        row_guide = [-1,-1,-1,0,0,1,1,1]
        col_guide = [-1,0,1,-1,1,-1,0,1]

        row_guide_h = [0,-1,0,1]
        col_guide_h = [-1,0,1,0]

        cols = len(map[0])
        rows = len(map)

        visited = [[0 for i in range(cols)] for j in range(rows)]

        i = 0
        j = 0
        islands = 0
        while i < rows:
            j = 0
            while j < cols:
                if map[i][j] == 1 and visited[i][j] == 0:
                    DFS_islands(i,j,map,visited,col_guide_h, row_guide_h, cols, rows)
                    islands += 1
                j+=1
            i+=1

        return islands

    '''
        Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

        Conditions:
        
        You will pick exactly 2 numbers.
        You cannot pick the same element twice.
        If you have muliple pairs, select the pair with the largest number.
    '''
    def problemFive(self, nums, target):
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        print(nums)
        print(target)
        while i < j:
            if nums[i] + nums[j] == target:
                return [i,j]
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i]+ nums[j] > target:
                j -= 1
            print(i,j)

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
    def problemEight(self, matrix, target):
        topRight = (0, len(matrix[0])-1)
        try:
            while True:
                if target < matrix[topRight[0]][topRight[1]]:
                    topRight = (topRight[0], topRight[1]-1)
                elif target > matrix[topRight[0]][topRight[1]]:
                    topRight = (topRight[0]+1, topRight[1])
                else:
                    return True
        except IndexError:
            return False

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

    '''
        Given an underected connected graph with n nodes labeled 1..n. A bridge (cut edge) is defined as an edge which, when removed, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). Equivalently, an edge is a bridge if and only if it is not contained in any cycle. The task is to find all bridges in the given graph. Output an empty list if there are no bridges.
        
        Input:
        
        n, an int representing the total number of nodes.
        edges, a list of pairs of integers representing the nodes connected by an edge.
    '''
    def problemEleven(self, n, edges):
        graph = Graph_und(n, edges)

        pass

    '''
    
    '''
    def actualTestOne(self, X, N, locations):
            heap_dist = []
            topX = []

            for location in locations:
                heapq.heappush(heap_dist, (calculateDistance(location), location))

            for i in range(X):
                best = heapq.heappop(heap_dist)[1]
                topX.append((best[0], best[1]))

            return topX

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
    def test_one_problemTwo(self):
        products = ["mobile","mouse","moneypot","monitor","mousepad"]
        searchWord = "mouse"
        output = [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
        ]
        solutions = Solution()
        result = solutions.problemTwo(products, searchWord)
        self.assertListEqual(result, output)
    def test_two_problemTwo(self):
        products = ["bags","baggage","banner","box","cloths"]
        searchWord = "bags"
        output = [
            ["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]
        ]
        solutions = Solution()
        result = solutions.problemTwo(products, searchWord)
        self.assertListEqual(result, output)
    def test_three_problemTwo(self):
        products = ["havana"]
        searchWord = "havana"
        output = [
            ["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]
        ]
        solutions = Solution()
        result = solutions.problemTwo(products, searchWord)
        self.assertListEqual(result, output)
    def test_one_problemThree(self):
        matrix = [
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
        ]

        solutions = Solution()
        hours = solutions.problemThree(matrix)
        self.assertEqual(hours, 2)
    def test_one_problemFour(self):
        map =[
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]
        ]

        solutions = Solution()
        islands = solutions.problemFour(map)
        self.assertEqual(1, islands)
    def test_two_problemFour(self):
        map =[
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
        ]

        solutions = Solution()
        islands = solutions.problemFour(map)
        self.assertEqual(3, islands)
    # def test_one_problemFive(self):
    #     nums = [1, 10, 25, 35, 60]
    #     target = 60
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
    def test_one_problemEight(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        target = 5
        output = True
        solutions = Solution()
        result = solutions.problemEight(matrix, target)
        self.assertEqual(result, output)
    def test_two_problemEight(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        target = 20
        output = False
        solutions = Solution()
        result = solutions.problemEight(matrix, target)
        self.assertEqual(result, output)
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
    # def test_one_problemEleven(self):
    #     n = 6
    #     edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
    #     solutions = Solution()
    #     result = solutions.problemEleven(n, edges)
    # def test_one_problemTwelve(self):
    #     map = [['O', 'O', 'O', 'O'],
    #      ['D', 'O', 'D', 'O'],
    #      ['O', 'O', 'O', 'O'],
    #      ['X', 'D', 'D', 'O']]
    #     solutions = Solution()
    #     result = solutions.problemTwelve(map)
    #     self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()