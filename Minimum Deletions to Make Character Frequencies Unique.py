# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/?envType=daily-question&envId=2023-09-12

#  Counter fuction: Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked. elements() is one of the functions of Counter class, when invoked on the Counter object will return an itertool of all the known elements in the Counter object.

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        dele = 0
        unique_set =set()

        for char, freq in cnt.items():
            while freq > 0 and freq in unique_set:
                freq -= 1
                dele +=1
            unique_set.add(freq)
        
        return dele


        
