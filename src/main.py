# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-07-21 08:13:01
# @Last Modified 2016-08-11
# @Last Modified time: 2016-08-11 10:47:11

def longest_key(input_dict):
    longest = 0
    for k in input_dict:
        if len(k)>longest:
            longest=len(k)
    return longest

def list_total(input_list):
    out = 0.0
    for i in input_list:
        out+=i
    return out

class Binary_Pattern_Analysis():
    """analyzes binary patterns given to it"""
    def __init__(self):
        self.pattern_collection={}

    def add(self,binary_pattern): # takes patterns like [True,False,False]
        binary_str = self.binary_pattern_to_str(binary_pattern)
        if binary_str in self.pattern_collection:
            self.pattern_collection[binary_str]+=1
        else:
            self.pattern_collection[binary_str]=1

    def count_occurances(self,binary_pattern):
        """ returns the count of the occurances of a binary pattern """
        binary_str = self.binary_pattern_to_str(binary_pattern)
        if binary_str in self.pattern_collection:
            return self.pattern_collection[binary_str]
        else:
            return 0

    def get_patterns_with(self,binary_pattern):
        """ returns every binary pattern that contains the
        input pattern along with the count of each match """
        out = {}
        binary_str = self.binary_pattern_to_str(binary_pattern)
        for k in self.pattern_collection:
            if binary_str in k:
                out[k]=self.binary_pattern[k]
        return out

    def binary_pattern_to_str(self,i):
        if isinstance(i, basestring):
            return i
        out=''
        for x in i:
            if x:
                out+='T'
            else:
                out+='F'
        return out

    def binary_str_to_pattern(self,i):
        """ returns the opposite of binary_pattern_to_str() """
        if isinstance(i, list):
            return i
        out = []
        for x in i:
            out.append(x.upper() == 'T')
        return out

    def count_patterns_at_length(self,l):
        out = 0
        for k in self.pattern_collection:
            if len(k)==l:
                out+=1
        return out

    def calculate_similarity(self, list_one, list_two):
        best_score=0.0
        if len(list_one)==len(list_two):
            for i in range(len(list_one)):
                if list_one[i]==list_two[i]:
                    best_score+=1.0
        else:
            if len(list_one)<len(list_two):
                # switch the lists if one is bigger than two
                list_one+=list_two
                list_two=list_one[:len(list_one)-len(list_two)]
                list_one=list_one[len(list_two):]
            for x in range(len(list_one)-len(list_two)):
                is_similar=False
                similar = 0.0
                for i in range(len(list_two)):
                    if list_one[i+x] == list_two[i]:
                        similar+=1.0
                if similar > best_score:
                    best_score=similar
        return(best_score/float(len(list_one)))

    def fuzzy_matches(self, binary_pattern, fuzziness = 0.3):
        """ returns matching patterns based on a certain accuracy """
        binary_pattern = self.binary_pattern_to_str(binary_pattern)
        out={}
        tmp = ''
        for k in self.pattern_collection:
            similarity = self.calculate_similarity(k, binary_pattern)
            if 1.0-similarity < fuzziness:
                out[k]=self.pattern_collection[k]
        return out

    def most_common(self):
        """ returns the most common pattern and its count """
        out_count = 0
        out_key = ''
        for k in self.pattern_collection:
            if self.pattern_collection[k]>out_count:
                out_count=self.pattern_collection[k]
                out_key = k
        return {out_key:out_count}

    def most_common_count(self):
        """ extends most_common to just return the count """
        tmp = self.most_common()
        for k in tmp:
            return tmp[k]

    def display_patterns(self):
        """ prints all patterns in decending order of occurance """
        greatest_count = self.most_common_count()
        while greatest_count>2:
            for k in self.pattern_collection:
                if self.pattern_collection[k] == greatest_count:
                    print '{} : {}'.format(k,self.pattern_collection[k])
            greatest_count-=1

class Binary_Tangent():
    def __init__(self,children=[],parent=None):
        self.r=None
        self.l=None
        if len(children):
            self.val=children.pop(0)
        else:
            self.val=None
        self.parent=parent
        self.child_count=len(children)
        if self.parent:
            self.depth=self.parent.depth+1
        else:
            self.depth=0
        if len(children):
            if children[0]:
                self.r=Binary_Tangent(children,self)
            else:
                self.l=Binary_Tangent(children,self)

    def get_root(self):
        t=self
        while t.parent != None:
            t=t.parent
        return t

    def get_last_child(self):
        t=self
        while t.has_child():
            t=t.get_child()
        return t

    def has_child(self):
        return(self.r != None or self.l != None)

    def get_child(self):
        if self.has_child():
            if self.r != None:
                return self.r
            else:
                return self.l
        else:
            return None

    def count_nodes(self):
        t=self.get_root()
        out = 1
        while t.has_child():
            out += 1
            t=t.get_child()
        return out

    def find_patterns(self, pattern_size_limit=0):
        tmp = self.get_root()
        analysis = Binary_Pattern_Analysis()
        node_count = self.count_nodes()
        if node_count<=pattern_size_limit or pattern_size_limit == 0:
            pattern_size_limit = node_count-1
        c=0
        min_pattern_depth = 2
        while c < (node_count - min_pattern_depth):
            c+=1
            current_pattern_range = min_pattern_depth
            try:
                while current_pattern_range<=pattern_size_limit:
                    t = tmp
                    pattern=[]
                    for i in range(current_pattern_range):
                        pattern.append(t.val)
                        t = t.get_child()
                    analysis.add(pattern)
                    current_pattern_range+=1
            except:
                pass
            tmp=tmp.get_child()
        return analysis

    def last_nodes(self,node_count):
        if node_count > self.count_nodes():
            node_count=self.count_nodes()
        t = self.get_last_child()
        out=[]
        while node_count>len(out):
            out.append(t.val)
            t=t.parent
        return out

    def binary_pattern_to_str(self,binary_pattern):
        return Binary_Pattern_Analysis().binary_pattern_to_str(binary_pattern)

    def calculate_next(self,nodes_to_consider=6): # I chose 6 since humans chose 7 to process reliably
        if nodes_to_consider>(self.count_nodes()/2):
            nodes_to_consider=self.count_nodes()/2
        binary_pattern = self.last_nodes(nodes_to_consider)
        bin_str=self.binary_pattern_to_str(binary_pattern)
        #print 'predicting: {}'.format(bin_str)
        patterns = self.find_patterns(nodes_to_consider*2)
        matches = patterns.fuzzy_matches(binary_pattern)
        tmp = {}
        for k in matches:
            if len(k) > len(binary_pattern):
                tmp[k]=matches[k]
        predictions = {}
        for k in tmp:
            # find where the match in the pattern is
            #print 'solving: {}'.format(k)
            best_i = -1
            for i in range(len(k)-len(bin_str)):
                current = k[i:len(bin_str)+i]
                similarity = Binary_Pattern_Analysis().calculate_similarity(k[i:len(bin_str)+i], bin_str)
                if similarity == 1.0:
                    best_i = i
            if best_i != -1 and best_i + len(bin_str) < len(k):
                #print 'found:      {}'.format(k)
                output_key = k[best_i:]
                #print best_i
                output_key = output_key[len(bin_str):]
                if len(output_key):
                    predictions[output_key]=tmp[k]
                #print 'sig values: {}'.format(output_key)

        if not len(predictions):
            return 'not enough data'
        # if there were any predictions at this point, it would look like this
        # predictions = {'TF': 1, 'TFF': 1, 'T': 2}
        scores = [0.0]*longest_key(predictions)
        datapoints = 0
        for i in range(longest_key(predictions)):
            for k in predictions:
                if len(k) > i:
                    for s in range(predictions[k]):
                        if k[i] == 'T':
                            datapoints+=1
                            scores[i]+=1.0
                        if k[i] == 'F':
                            datapoints+=1
                            scores[i]-=1.0
        for i in range(len(scores)):
            if i>0:
                scores[i]+=scores[i-1]
        final_score = (scores[-1]+datapoints)/(datapoints*2)
        # print 'collected previous conclusions to this moment:\n{}'.format(predictions)
        # print 'score progression: {}'.format(scores)
        # print '========================================================='
        # print 'confidence score: {}'.format(final_score)
        # print 'based on {} patterns in the past'.format(int(list_total(predictions.values())))
        return {
            "confidence_score":final_score,
            "similar_patterns":int(list_total(predictions.values()))
        }


    # below is rendering crap.

    def root_indent(self):
        # [True,False,False,True,False,True]
        # calc how far is farthest false
        root=self.get_root()
        current_indent=0
        farthest_indent=0
        t=root
        while t.has_child():
            t=t.get_child()
            if t.val:
                current_indent-=2
            else:
                current_indent+=2
            if current_indent>farthest_indent:
                farthest_indent=current_indent

        return farthest_indent

    def indent_from_root(self):
        depth = self.depth
        indent = self.root_indent()
        t = self.get_root()
        i=0
        while i<depth:
            i+=1
            t=t.get_child()
            if t.val == True:
                indent+=2
            if t.val == False:
                indent-=2
        return indent

    def get_indent(self):
        if self.depth < 1:
            return self.root_indent()
        else:
            indent = self.indent_from_root()
            return indent

    def str(self):
        s=''
        if self.val:
            s="T"
        else:
            s="F"
        indent = self.get_indent()
        print ' '*indent+s
        brackets=''
        if self.l != None:
            brackets+='/ '
        else:
            brackets+='  '
        if self.r != None:
            brackets+='\\'
        else:
            brackets+=' '
        if indent==0:
            brackets=brackets[1:]
        if self.child_count>0:
            print ' '*(indent-1)+brackets
        if self.r:
            self.r.str()
        elif self.l:
            self.l.str()

    def gen_pattern_tree(self):
        print 'self.gen_pattern_tree() is not complete.'
        exit()
        t = self.get_root()


def random_binary_pattern(length=16):
    from random import randint
    out = []
    while len(out) < length:
        out.append(randint(0,1)<1)
    return out

def line():
    print '========================================================='

if __name__ == '__main__':
    t = Binary_Tangent(random_binary_pattern(128))
    t.str()
    patterns=t.find_patterns()
    collection = patterns.pattern_collection
    line()
    print 'Collected Patterns:'
    patterns.display_patterns()
    line()
    print 'Calculating a prediction for the next value...'
    t.calculate_next()

