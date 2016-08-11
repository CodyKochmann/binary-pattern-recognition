# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-07-21 08:13:01
# @Last Modified 2016-08-11
# @Last Modified time: 2016-08-11 13:30:04

import sys
sys.setrecursionlimit(1000000)
from random import randint
from collections import deque

def longest_key(input_dict):
    """ returns the longest key in a dictionary """
    longest = 0
    for k in input_dict.keys():
        k = len(k)
        if k > longest:
            longest = k
    return longest

def calculate_similarity(l_one, l_two):
    """ calculates the similarity of two lists """
    best_score = 0
    # determine how many tests are needed
    if len(l_one) is len(l_two):
        tests = 1
    else:
        len(l_one) - len(l_two)
        if len(l_one) < len(l_two):
            l_two, l_one = l_one, l_two
    for offset in range(tests):
        similar = 0
        for i in range(len(l_two)):
            if l_one[i+offset] is l_two[i]:
                similar+=1
        if similar > best_score:
            best_score = similar
    return best_score / float(len(l_one))

def binary_str_to_pattern(i):
    """ returns the opposite of binary_pattern_to_str() """
    if isinstance(i, list):
        return i
    out = deque()
    for x in i:
        out.append(x.upper() == 'T')
    return list(out)


def binary_pattern_to_str(i):
    if isinstance(i, basestring):
        return i
    out = ''
    for x in i:
        if x:
            out += 'T'
        else:
            out += 'F'
    return out


class Binary_Pattern_Analysis(object):
    """analyzes binary patterns given to it"""

    def __init__(self):
        self.pattern_collection = {}

    def add(self, binary_pattern):  # takes patterns like [True,False,False]
        binary_str = binary_pattern_to_str(binary_pattern)
        if binary_str in self.pattern_collection:
            self.pattern_collection[binary_str] += 1
        else:
            self.pattern_collection[binary_str] = 1

    def count_occurances(self, binary_pattern):
        """ returns the count of the occurances of a binary pattern """
        binary_str = binary_pattern_to_str(binary_pattern)
        if binary_str in self.pattern_collection:
            return self.pattern_collection[binary_str]
        else:
            return 0

    # noinspection PyUnresolvedReferences
    def get_patterns_with(self, binary_pattern):
        """ returns every binary pattern that contains the
        input pattern along with the count of each match """
        out = {}
        binary_str = binary_pattern_to_str(binary_pattern)
        for k in self.pattern_collection:
            if binary_str in k:
                out[k] = self.binary_pattern[k]
        return out

    def count_patterns_at_length(self, l):
        out = 0
        for k in self.pattern_collection:
            if len(k) == l:
                out += 1
        return out

    def fuzzy_matches(self, binary_pattern, fuzziness=0.3):
        """ returns matching patterns based on a certain accuracy """
        binary_pattern = binary_pattern_to_str(binary_pattern)
        out = {}
        for k in self.pattern_collection:
            similarity = calculate_similarity(k, binary_pattern)
            if 1.0 - similarity < fuzziness:
                out[k] = self.pattern_collection[k]
        return out

    def most_common(self):
        """ returns the most common pattern and its count """
        out_count = 0
        out_key = ''
        for k in self.pattern_collection:
            if self.pattern_collection[k] > out_count:
                out_count = self.pattern_collection[k]
                out_key = k
        return {out_key: out_count}

    def most_common_count(self):
        """ extends most_common to just return the count """
        tmp = self.most_common()
        return tmp[tmp.keys()[0]]

    def display_patterns(self):
        """ prints all patterns in descending order of occurance """
        greatest_count = self.most_common_count()
        while greatest_count > 2:
            for k in self.pattern_collection:
                if self.pattern_collection[k] == greatest_count:
                    print '{} : {}'.format(k, self.pattern_collection[k])
            greatest_count -= 1




class Binary_Tangent(object):
    def __init__(self, children=[], parent=None):
        """
            r = child node if its true
            l = child node if its false
        """
        self.r = None
        self.l = None
        if len(children):
            self.val = children.pop(0)
        else:
            self.val = None
        self.parent = parent
        self.child_count = len(children)
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        if len(children):
            if children[0]: # if the next child is True
                self.r = Binary_Tangent(children, self)
            else: # if the next child is False
                self.l = Binary_Tangent(children, self)

    def get_root(self):
        # noinspection PyShadowingNames
        t = self
        while t.parent is not None:
            # noinspection PyShadowingNames
            t = t.parent
        return t

    def get_last_child(self):
        # noinspection PyShadowingNames
        t = self
        while t.has_child():
            # noinspection PyShadowingNames
            t = t.get_child()
        return t

    def has_child(self):
        return self.r is not None or self.l is not None

    def get_child(self):
        if self.has_child():
            if self.r is not None:
                return self.r
            else:
                return self.l
        else:
            return None

    @staticmethod
    def count_nodes(node):
        # noinspection PyShadowingNames
        if node.parent is not None:
            node = node.get_root()
        out = 1
        while True:
            if not node.has_child():
                return out
            out += 1
            node = node.get_child()

    @staticmethod
    def child_patterns(node,min_length,max_length):
        pattern = deque(maxlen=max_length)
        try:
            while True:
                pattern.append(node.val)
                if len(pattern)>=min_length:
                    yield list(pattern)
                node=node.get_child()
        except AttributeError, e:
            pass

    @staticmethod
    def all_children(root_node):
        while root_node.has_child():
            root_node = root_node.get_child()
            yield root_node

    @staticmethod
    def all_child_patterns(root_node,pattern_size_limit):
        min_pattern_depth = 3
        for node in root_node.all_children(root_node):
            for pattern in root_node.child_patterns(node, min_pattern_depth, pattern_size_limit):
                yield pattern

    def find_patterns(self, pattern_size_limit=0):
        root_node = self.get_root()
        analysis = Binary_Pattern_Analysis()
        node_count = self.count_nodes(self)
        if node_count <= pattern_size_limit or pattern_size_limit == 0:
            pattern_size_limit = node_count - 1
        for pattern in self.all_child_patterns(root_node,pattern_size_limit):
            analysis.add(pattern)
        return analysis

    def last_nodes(self, node_count):
        if node_count > self.count_nodes(self):
            node_count = self.count_nodes(self)
        t = self.get_last_child()
        out = []
        while node_count > len(out):
            out.append(t.val)
            t = t.parent
        return out

    def calculate_next(self, nodes_to_consider=6):  # I chose 6 since humans chose 7 to process reliably
        if nodes_to_consider > (self.count_nodes(self) / 2):
            nodes_to_consider = self.count_nodes(self) / 2
        binary_pattern = self.last_nodes(nodes_to_consider)
        bin_str = binary_pattern_to_str(binary_pattern)
        # print 'predicting: {}'.format(bin_str)
        # noinspection PyShadowingNames
        patterns = self.find_patterns(nodes_to_consider * 2)
        matches = patterns.fuzzy_matches(binary_pattern)
        tmp = {}
        for k in matches:
            if len(k) > len(binary_pattern):
                tmp[k] = matches[k]
        predictions = {}
        for k in tmp:
            # find where the match in the pattern is
            # print 'solving: {}'.format(k)
            best_i = -1
            for i in range(len(k) - len(bin_str)):
                current = k[i:len(bin_str) + i]
                similarity = calculate_similarity(current, bin_str)
                if similarity == 1.0:
                    best_i = i
            if best_i != -1 and best_i + len(bin_str) < len(k):
                # print 'found:      {}'.format(k)
                output_key = k[best_i:]
                # print best_i
                output_key = output_key[len(bin_str):]
                if len(output_key):
                    predictions[output_key] = tmp[k]
                    # print 'sig values: {}'.format(output_key)

        # return if there isn't enough data to make a prediction
        if not len(predictions):
            return {
                'confidene_score':0.0,
                'similar_patterns':0,
                'message':'not enough data'
            }
        # if there were any predictions at this point, it would look like this
        # predictions = {'TF': 1, 'TFF': 1, 'T': 2}
        scores = [0.0] * longest_key(predictions)
        datapoints = 0
        for i in range(longest_key(predictions)):
            for k in predictions:
                if len(k) > i:
                    for s in range(predictions[k]):
                        if k[i] == 'T':
                            datapoints += 1
                            scores[i] += 1.0
                        if k[i] == 'F':
                            datapoints += 1
                            scores[i] -= 1.0
        for i in range(len(scores)):
            if i > 0:
                scores[i] += scores[i - 1]
        final_score = (scores[-1] + datapoints) / (datapoints * 2)
        # print 'collected previous conclusions to this moment:\n{}'.format(predictions)
        # print 'score progression: {}'.format(scores)
        # print '========================================================='
        # print 'confidence score: {}'.format(final_score)
        # print 'based on {} patterns in the past'.format(int(list_total(predictions.values())))
        return {
            "confidence_score": final_score,
            "similar_patterns": int(sum(predictions.values()))
        }

    """===================================================================
        Everything below this is crap for rendering the Binary_Tangent
    ==================================================================="""

    @staticmethod
    def root_indent(node):
        """ calculates how far the root node needs to be indented """
        current_indent = 0
        farthest_indent = 0
        node = node.get_root()
        while node.has_child():
            node = node.get_child()
            if node.val:
                current_indent -= 2
            else:
                current_indent += 2
            if current_indent > farthest_indent:
                farthest_indent = current_indent
        return farthest_indent

    @staticmethod
    def indent_from_root(node):
        """ calculates the indent for the current node compared to the root """
        depth = node.depth
        indent = node.root_indent(node)
        node = node.get_root()
        while depth:
            depth -= 1
            node = node.get_child()
            if node.val == True:
                indent += 2
            if node.val == False:
                indent -= 2
        return indent

    @staticmethod
    def get_indent(node):
        """ returns which indent function is correct for the node """
        if node.depth < 1:
            return node.root_indent(node)
        return node.indent_from_root(node)

    def render(self):
        """ recursively renders the entire Binary_Tangent in the CLI """
        if self.val:
            s = "T"
        else:
            s = "F"
        indent = self.get_indent(self)
        print ' ' * indent + s
        brackets = ''
        if self.l is not None:
            brackets += '/ '
        else:
            brackets += '  '
        if self.r is not None:
            brackets += '\\'
        else:
            brackets += ' '
        if indent == 0:
            brackets = brackets[1:]
        if self.child_count > 0:
            print ' ' * (indent - 1) + brackets
        if self.r:
            self.r.render()
        elif self.l:
            self.l.render()

    @staticmethod
    def gen_pattern_tree():
        """ this will convert the Binary_Tangent into a Pattern_Tree """
        pass

def random_binary_pattern(length=16):
    """ returns a list of random binary values to test against """
    out = deque()
    while len(out) < length:
        out.append(randint(0, 1) < 1)
    return list(out)

def line():
    """ just a cleaner way to put dividers in the code's output """
    print '========================================================='


if __name__ == '__main__':
    t = Binary_Tangent(random_binary_pattern(128))
    t.render()
    patterns = t.find_patterns()
    collection = patterns.pattern_collection
    line()
    print 'Collected Patterns:'
    patterns.display_patterns()
    line()
    print 'Calculating a prediction for the next value...'
    print t.calculate_next()
