def run_test():
    """ this runs a test over a majority of the code to test it. """
    tangent = BinaryTangent(random_binary_pattern(256))
    tangent.render()
    patterns = tangent.find_patterns()
    line()
    print('Collected Patterns:')
    patterns.display_patterns()
    line()
    print(random_binary_pattern(16))
    print('Calculating a prediction for the next value...')
    print(tangent.calculate_next())


from main import random_binary_pattern, BinaryTangent

template = '''
print('test {}')
test = {}
expected_confidence = {}
expected_similar_patterns = {}
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]
'''.format
f = open('test.py', 'w')
f.write('''
from main import BinaryTangent
''')
for i in range(1,257):
    print(i)
    test=random_binary_pattern(i)
    _test = list(test)
    tangent = BinaryTangent(test)
    prediction = tangent.calculate_next()

    f.write(template(i, repr(_test), prediction['confidence_score'].as_integer_ratio(), prediction['similar_patterns']))
