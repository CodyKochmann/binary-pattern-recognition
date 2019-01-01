
from main import BinaryTangent

print('test 1')
test = [False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 2')
test = [True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 3')
test = [True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 4')
test = [True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 5')
test = [True, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 6')
test = [True, False, False, True, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 7')
test = [False, False, True, False, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 8')
test = [False, False, False, False, True, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 9')
test = [False, True, False, False, True, True, True, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 10')
test = [False, True, False, False, True, True, True, True, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 11')
test = [False, True, True, False, False, False, False, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 12')
test = [True, True, True, True, False, False, True, False, False, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 13')
test = [True, True, False, True, False, True, False, True, False, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 14')
test = [False, True, True, False, True, False, True, False, True, True, True, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 15')
test = [False, False, False, False, True, True, False, False, True, True, True, False, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 16')
test = [False, False, False, False, False, False, False, False, True, False, False, False, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 17')
test = [False, True, True, False, True, False, True, False, False, True, True, True, True, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 18')
test = [False, False, True, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 19')
test = [True, True, True, True, False, True, False, False, False, False, True, True, True, True, True, False, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 20')
test = [False, True, False, True, False, True, True, True, False, True, True, False, False, False, True, False, False, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 21')
test = [False, True, True, True, True, True, False, True, True, True, False, False, False, False, True, False, False, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 22')
test = [True, False, True, False, False, True, True, False, True, False, True, True, False, False, False, False, True, False, False, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 23')
test = [True, True, True, True, False, True, True, False, True, True, True, False, True, False, True, False, False, False, False, False, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 24')
test = [True, True, True, False, False, True, True, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 25')
test = [False, False, False, False, True, True, True, True, True, True, True, True, True, False, True, False, True, False, True, False, True, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 26')
test = [False, True, True, True, True, False, False, True, True, True, False, False, False, True, True, True, False, False, True, False, False, True, False, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 27')
test = [False, True, False, False, False, True, False, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, False, False, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 28')
test = [False, True, False, True, True, True, True, True, True, False, True, True, False, True, True, False, False, False, False, False, True, False, False, True, True, False, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 29')
test = [False, True, False, False, False, False, False, False, True, True, False, False, False, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 30')
test = [False, False, False, True, False, True, True, False, False, False, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 31')
test = [True, False, True, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 32')
test = [True, True, False, True, True, False, False, True, True, True, True, False, False, True, True, True, False, False, True, False, False, True, True, True, False, True, True, False, False, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 33')
test = [False, True, True, False, True, False, True, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, True, True, True, False, False, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 34')
test = [True, False, False, False, False, False, False, True, False, False, True, True, False, False, True, False, False, False, True, False, True, True, False, False, False, True, False, True, False, False, False, True, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 35')
test = [True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 36')
test = [True, True, True, True, True, False, False, True, True, False, True, False, False, False, False, False, True, False, True, False, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 37')
test = [True, False, True, True, False, False, True, False, False, True, True, True, True, False, True, True, False, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, True, True, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 38')
test = [False, False, False, False, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, True, True, False, False, True, True, True, False, False, True, True, True, False, False, False, True, True, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 39')
test = [False, False, True, False, False, False, True, False, False, False, True, False, True, True, True, False, False, False, False, True, False, True, False, True, True, True, False, True, True, False, True, True, True, False, True, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 40')
test = [True, True, False, False, True, False, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, False, True, False, False, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 41')
test = [False, True, False, False, True, True, False, True, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, False, False, False, False, False, True, False, False, False, True, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 42')
test = [False, True, False, True, False, True, True, True, False, True, True, True, False, True, True, True, True, False, False, True, True, True, False, False, False, True, True, False, False, False, False, True, False, True, True, False, True, True, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 43')
test = [False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, True, False, True, False, True, True, False, True, True, False, True, True, False, False, False, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 44')
test = [False, False, True, True, True, True, True, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, True, True, False, True, True, True, True, True, True, True, False, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 45')
test = [True, False, True, True, False, False, False, True, False, False, False, True, False, True, False, False, True, False, True, False, False, False, False, True, False, True, False, True, True, True, False, True, True, True, False, True, False, True, True, False, False, True, False, False, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 46')
test = [True, True, True, False, False, True, True, False, True, True, False, False, False, False, False, False, True, False, True, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, False, True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 47')
test = [False, False, True, True, False, True, True, True, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, False, True, True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 48')
test = [False, False, True, True, False, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, False, False, True, True, False, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True, False, False, True, True, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 49')
test = [True, False, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, True, True, True, False, True, True, True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 50')
test = [False, True, False, True, False, False, True, True, False, True, False, False, False, True, True, False, True, True, True, True, True, False, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, True, False, True, True, False, True, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 51')
test = [True, False, True, True, True, False, True, False, True, True, False, True, True, False, True, True, False, True, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, True, True, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 52')
test = [False, True, False, True, True, False, True, True, True, False, False, False, True, False, True, False, True, False, False, True, True, True, True, False, True, True, True, True, True, True, True, False, False, False, True, True, True, True, False, True, True, False, False, False, True, False, False, True, False, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 53')
test = [True, True, True, False, True, True, False, True, False, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, True, False, False, True, False, False, True, True, True, False, True, False, False, True, False, False, False, True, False, True, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 54')
test = [True, False, False, False, False, False, True, True, True, True, False, True, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, True, False, True, True, False, False, True, True, False, False, False, False, False, True, True, False, True, True, False, True, False, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 55')
test = [True, False, False, True, False, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, True, True, True, False, True, False, False, False, True, True, False, True, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, False, False, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 56')
test = [True, False, True, False, False, True, False, True, True, False, True, True, True, False, True, True, False, False, True, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, False, False, False, False, True, False, True, False, True, True, True, False, True, False, True, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 57')
test = [True, False, False, False, True, False, True, True, False, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, True, False, False, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, True, False, False, True, True, False, True, True, True, False, False, True, True, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 58')
test = [True, True, True, False, False, False, False, True, True, True, False, False, True, False, False, True, False, True, False, True, True, False, False, True, True, True, False, False, True, False, False, False, True, True, False, False, True, False, True, True, True, True, True, True, False, True, True, True, False, False, True, True, False, False, False, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 59')
test = [True, False, True, True, False, False, False, True, False, True, True, True, True, True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, False, False, False, False, True, False, True, False, True, True, True, True, False, False, True, False, True, False, True, False, False, False, True, False, True, True, True, True, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 60')
test = [True, False, False, False, False, True, False, False, True, True, True, False, False, True, False, True, False, True, False, False, True, False, True, True, True, True, True, False, True, False, True, True, False, False, True, True, False, True, True, True, True, True, False, True, False, False, True, False, True, True, False, False, True, False, True, False, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 61')
test = [True, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, True, False, True, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, True, False, True, False, True, True, False, False, True, False, False, True, False, False, False, True, True, False, False, True, True, False, False, True, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 62')
test = [False, False, False, True, False, True, True, False, False, False, True, True, False, True, True, True, False, False, True, False, True, True, False, True, False, False, True, True, False, False, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, False, False, False, True, False, True, True, True, False, False, False, True, False, False, True, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 63')
test = [False, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, False, True, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, False, True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 64')
test = [True, True, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, True, True, True, False, True, True, True, True, True, False, False, False, False, True, False, True, False, False, True, True, True, False, False, False, True, True, False, False, True, False, False, False, False, True, True, True, False, False, False, True, True, False, False, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 65')
test = [False, False, True, True, True, True, False, False, False, True, True, False, False, False, True, True, True, True, True, True, True, False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, False, False, True, True, False, False, True, False, False, False, True, False, False, True, True, True, False, False, False, True, False, True, True, True, True, False, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 66')
test = [True, False, False, False, False, True, True, True, True, False, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, False, True, True, True, True, True, True, False, False, False, True, False, False, False, False, True, False, True, True, False, False, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 67')
test = [False, False, False, True, False, False, True, True, True, False, False, False, False, True, False, False, False, True, False, False, True, False, True, True, True, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 68')
test = [True, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, True, True, False, False, False, True, False, True, True, False, True, True, False, False, True, False, True, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, False, True, False, True, True, False, True, False, False, False, False, True, True, False, True, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 69')
test = [True, False, True, False, True, True, True, True, True, True, False, False, True, True, True, False, False, True, False, True, False, False, True, False, False, True, False, True, True, True, True, False, False, False, True, True, True, False, True, True, True, True, True, False, True, False, False, True, False, True, False, False, True, False, False, False, True, True, False, True, False, True, False, False, True, True, True, True, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 70')
test = [True, False, True, True, True, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, False, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, True, False, True, False, False, False, False, True, False, False, False, True, False, True, False, True, False, True, True, False, False, False, True, True, False, False]
expected_confidence = (6004799503160661, 36028797018963968)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 71')
test = [True, False, False, True, True, True, False, False, True, False, True, True, False, True, True, False, True, True, False, False, False, True, True, False, False, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, False, True, True, False, True, True, True, True, True, True, False, False, False, True, True, False, True, False, True, False, True, False, False, True, True, True, False, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 72')
test = [True, False, True, True, False, True, False, True, False, True, True, True, False, True, True, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, False, False, True, False, False, True, True, True, True, False, False, True, True, False, True, True, True, False, True, True, True, False, False, False, False, True, False, True, False, False, False, True, True, False, False, True, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 73')
test = [True, False, True, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, False, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, True, True, False, True, True, False, True, True, True, False, True, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 74')
test = [True, True, False, False, True, True, False, True, True, True, False, True, False, False, True, False, False, True, False, True, True, True, True, True, True, True, False, False, True, True, False, True, True, False, True, False, True, False, False, False, False, False, True, False, False, False, False, True, True, True, False, False, True, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, False, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 75')
test = [True, False, True, True, False, False, False, False, True, False, False, True, True, True, True, False, False, False, False, False, True, True, True, True, False, False, True, False, True, False, True, False, False, False, True, False, True, True, False, False, False, True, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, True, True, True, False, True, True, False, False, False, False, False, True, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 76')
test = [True, False, False, True, False, False, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, False, False, True, False, False, False, True, True, True, True, False, False, False, True, True, False, False, False, False, True, False, True, False, False, True, False, False, True, False, True, True, True, False, False, False, False, False, True, False, False, True, True, False, False, False, False, True, False, False, False, True, False]
expected_confidence = (7720456504063707, 18014398509481984)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 77')
test = [True, False, True, True, True, False, True, False, True, False, False, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, True, True, True, True, True, False, False, False, True, True, True, True, False, False, False, True, False, True, True, False, False, False, True, False, False, True, False, False, True, False, False, True, True, True, True, True, False, True, False, False, True, False, True, True, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 78')
test = [False, False, True, True, True, True, False, True, False, False, False, True, True, True, False, True, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, False, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False, False, False, False, False, True, True, True, True, True, True, False, True, False, False, True, False, True, False, True, True, True, False, False, False, False, False, False, False, True]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 79')
test = [True, False, True, True, True, False, True, False, False, True, True, True, True, True, True, False, False, False, True, False, True, False, False, False, False, False, True, True, False, True, True, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, True, False, True, True, True, False, False, False, False, True, False, True, False, False, True, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 80')
test = [False, False, True, False, False, True, False, True, True, False, True, False, True, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, False, False, False, True, False, False, True, True, False, False, True, False, False, True, True, False, False, False, True, False, True, True, False, False, False, False, False, True, False, True, False, False, True, False, True, False, True, True, False, True, False, True, False, True, True, True, True, False, False, True, False, False]
expected_confidence = (5404319552844595, 9007199254740992)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 81')
test = [False, True, False, True, True, False, False, False, True, True, True, True, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, False, False, True, False, True, False, False, False, True, True, True, False, False, True, False, True, False, True, False, False, False, False, True, True, True, True, False, False, False, False, False, True, False, True, False, False, True, False, False, True, False, False, False, True, True, False, False, True, True, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 82')
test = [True, False, False, False, True, True, True, True, True, False, False, True, True, True, False, True, False, False, False, True, True, False, True, False, True, True, True, False, False, True, False, True, False, False, True, True, False, True, True, False, True, True, False, True, True, False, False, False, False, False, True, True, True, False, True, False, False, True, True, False, True, True, False, False, False, True, False, False, True, False, False, True, True, True, True, True, True, True, True, True, False, False]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 83')
test = [False, False, False, True, False, True, False, False, True, False, True, True, False, True, True, True, False, False, True, False, False, False, False, True, True, True, False, False, False, False, True, True, True, False, False, True, False, False, True, False, False, True, False, True, False, False, True, True, True, False, False, True, False, True, True, False, False, True, True, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, True, False, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 84')
test = [False, False, True, True, True, False, False, False, False, False, True, False, True, True, True, False, True, False, False, False, True, False, True, True, False, True, False, True, False, False, False, False, True, True, False, True, False, True, False, True, True, True, True, False, True, False, False, True, False, True, False, False, True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False, False, False, True, False, True, True, True, False, True, False, True, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 85')
test = [False, False, True, True, True, False, True, False, False, True, False, True, False, True, True, False, True, True, True, False, False, False, True, False, True, False, True, True, True, False, True, False, False, True, False, False, False, True, True, True, True, False, False, True, True, True, False, False, False, True, True, True, False, True, True, True, True, True, False, True, True, False, False, False, True, False, False, True, False, True, True, True, False, True, False, True, True, False, False, False, False, True, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 86')
test = [False, False, False, True, True, False, False, True, True, True, True, False, False, False, False, True, True, True, True, False, True, False, True, False, True, True, False, True, False, False, False, False, True, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, False, False, True, True, False, True, True, False, True, False, False, True, True, False, False, True, False, True, True, True, False, False, False, False, True, True, False, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 87')
test = [True, False, False, False, False, False, False, False, True, True, True, False, False, True, False, False, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, False, False, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, False, True, True, True, False, False, True, False, False, True, True, True, False, True, False, True, False, True, True, False, False, True, True, True, True, True, True, False, False, True, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 88')
test = [True, True, False, False, True, False, True, True, False, False, True, False, False, True, True, True, True, False, False, False, False, True, False, False, True, True, True, True, True, True, False, False, False, True, False, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, True, False, True, True, True, False, True, False, False, True, False, True, True, True, True, True, False, True, False, True, True, True, True, False, False, True, True, True, False, False, True, True, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 89')
test = [True, False, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, True, False, True, True, False, True, True, True, True, False, False, False, True, True, False, False, False, False, True, True, True, False, False, True, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 90')
test = [False, True, True, False, True, True, False, True, True, True, True, False, False, False, True, True, True, True, False, False, True, False, True, True, False, False, True, False, True, False, False, True, False, False, False, True, False, True, False, True, True, False, True, False, False, False, False, False, True, True, True, False, False, False, True, False, True, True, True, False, True, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, True, False, False, False, False, False, False, True, False, True, True, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 91')
test = [True, False, True, True, True, False, True, True, False, True, True, True, True, False, False, False, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, False, True, False, False, False, True, True, True, False, True, True, True, True, False, True, True, True, False, False, False, False, False, False, True, True, True, True, False, False, False, True, True, True, True, True, False, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 92')
test = [False, True, True, False, True, True, True, False, True, False, True, False, False, True, False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, True, True, True, True, True, False, False, True, False, False, True, False, False, False, False, True, True, False, True, True, False, False, False, True, False, False, True, True, False, True, True, False, False, True, True, True, True, True, False, True, True, False, False, False, True, False, True, False, True, False, False, True, False, False, True, True, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 93')
test = [False, False, True, True, False, False, True, True, True, True, False, True, False, True, False, True, True, True, True, True, False, False, False, True, True, False, False, False, True, True, True, False, False, False, False, True, False, True, True, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, False, True, False, False, False, True, False, False, False, True, True, True, True, True, True, False, False, True, True, True, True, False, True, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 94')
test = [False, True, True, True, False, True, False, False, True, True, False, False, False, False, False, False, False, False, True, True, False, True, False, False, True, False, False, True, True, False, True, True, True, False, False, False, False, True, True, False, False, True, False, True, False, False, False, True, False, True, True, True, True, False, False, True, False, False, False, True, True, True, True, False, False, False, True, True, True, False, False, False, True, True, True, True, False, True, False, False, False, False, True, False, True, False, True, True, False, False, True, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 95')
test = [True, False, False, True, False, True, True, True, False, False, False, True, False, False, False, True, True, False, True, False, True, False, True, False, False, False, True, True, True, True, True, False, True, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, True, True, False, False, True, False, False, True, True, True, False, True, True, True]
expected_confidence = (1, 2)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 96')
test = [False, True, True, False, True, True, False, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, False, True, False, True, True, True, True, False, True, True, False, False, True, False, False, True, True, False, False, True, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 97')
test = [True, False, False, True, True, False, True, False, True, False, False, False, True, False, True, True, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, False, True, False, True, False, False, True, True, False, False, False, False, False, True, False, False, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, True, False, True, True, True, True, True, True, False, False, False, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 98')
test = [True, True, True, False, False, True, True, True, False, False, False, True, False, True, False, False, True, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, False, False, False, True, False, True, True, False, True, True, True, True, True, False, False, True, True, True, False, False, False, True, True, True, True, True, True, True, False, True, True, True, True, False, False, True, False, False, False, False, False, False, False, False, True, False, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 99')
test = [True, False, False, True, True, False, True, True, False, False, True, True, True, True, True, True, False, False, False, True, False, False, False, True, True, True, False, True, True, True, False, False, True, False, True, True, False, False, True, False, True, True, False, True, True, False, False, True, False, True, False, False, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, True, False, True, True, False, False, True, False, True, False, True, True, True, False, False, False, False, False, True, False, False, True, False, True, True, False, False, False, False, True, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 100')
test = [True, True, True, True, False, False, False, True, True, False, False, False, True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, False, True, True, False, True, True, True, True, False, False, True, True, False, False, False, True, True, False, True, True, False, False, False, False, False, True, False, False, True, False, True, True, False, False, True, False, False, False, True, True, True, True, True, True, False, True, False, False, True, False, True, True, False, True, False, False, True, False, False, True, True, True, True, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 101')
test = [False, True, True, True, False, False, False, True, False, True, False, True, True, False, True, True, True, False, False, False, True, False, False, True, True, False, False, False, True, True, True, True, False, False, False, True, False, False, True, True, False, False, True, True, False, False, True, False, True, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True, False, False, True, True, False, False, False, False, True, False, True, False, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, True, False, False, True, True, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 102')
test = [False, False, False, False, False, True, True, True, False, True, False, False, True, True, True, True, False, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, True, True, True, False, True, True, False, False, True, False, False, False, True, False, False, False, False, True, False, False, True, True, False, True, True, True, True, False, True, True, True, False, False, False, False, False, True, True, False, True, True, False, True, True, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 103')
test = [False, False, False, True, False, False, True, False, True, True, True, True, True, False, False, False, False, False, True, False, True, False, False, True, False, False, True, True, True, False, True, False, True, False, True, False, False, False, True, False, False, True, False, False, True, False, True, False, True, False, True, True, False, True, True, True, False, False, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, True, True, True, True, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 104')
test = [False, False, True, True, True, True, False, True, True, True, False, True, False, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, False, False, False, False, False, True, False, True, True, False, False, True, True, False, True, True, True, True, False, True, True, True, True, False, True, False, False, False, True, False, True, True, False, False, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, False, False, False, True, False, True, False, True]
expected_confidence = (7505999378950827, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 105')
test = [True, True, False, True, False, False, False, False, False, False, False, False, False, True, True, True, False, False, True, False, True, False, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, True, False, True, False, True, False, False, False, True, True, False, True, True, False, True, True, False, False, False, True, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, False, True, False, False, True, False, True, False, True, False, False, True, True, True, False, True, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 106')
test = [True, False, False, True, False, False, True, False, True, False, True, False, True, True, True, False, True, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, True, True, False, True, True, False, True, False, False, True, False, False, True, False, True, False, True, False, True, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False, True, False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True]
expected_confidence = (5404319552844595, 18014398509481984)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 107')
test = [False, True, True, True, False, False, True, True, False, False, False, True, False, False, True, False, False, True, False, True, False, False, True, True, False, True, False, True, True, False, True, False, False, True, False, False, True, True, True, True, True, False, False, True, True, True, False, False, True, False, False, False, True, False, False, False, True, True, False, True, True, False, False, False, False, False, False, False, True, True, True, True, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False, True, True, False, False, True, False, False, True, False, False, False, False, True, True, True, False, True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 108')
test = [False, True, True, False, False, True, True, False, True, False, True, False, False, False, False, True, True, False, True, True, False, True, False, True, True, True, True, False, False, True, False, True, True, False, False, False, True, True, True, False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, True, True, False, False, False, False, True, False, True, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, True, True, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 109')
test = [False, True, False, False, True, True, False, True, False, False, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, False, False, False, False, False, True, True, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, False, False, False, False, True, True, False, True, False, False, False, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, False, False, False, True, True, True, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 110')
test = [False, True, False, True, False, True, True, True, False, False, True, True, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, False, True, False, True, True, True, False, False, True, False, False, True, False, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, False, True, True, True, False, False, True, False, False, False, False, False, False, True, False, True, True, True, True, False, True, True, False, True, True, False, False, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 111')
test = [True, True, True, False, False, False, True, False, True, False, True, False, False, True, False, False, True, False, False, True, True, False, True, False, True, True, True, False, True, False, False, False, False, True, False, True, False, True, False, True, True, False, True, True, True, False, True, False, False, False, False, True, False, True, True, True, True, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True, False, False, False, True, True, False, False, False, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 112')
test = [False, True, False, True, True, True, False, True, True, True, True, False, True, False, False, True, True, False, False, True, True, True, False, True, True, False, True, False, False, False, False, False, True, True, True, True, False, False, True, True, True, True, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, True, True, False, True, False, True, False, True, True, True, True, True, False, False, True, False, False, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, True, False, True, False, False, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 113')
test = [True, False, True, False, True, True, True, True, False, False, True, False, False, False, False, False, True, True, True, False, False, True, True, False, False, False, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, True, True, False, True, True, True, True, False, False, False, False, False, False, True, False, True, False, True, True, False, True, True, False, True, True, False, False, False, False, True, True, False, False, False, False, True, False, True, True, False, False, True, True, False, True, True, True, False, False, True, False, True, False, True, False, False, False, False, True, False, False, False, False, True, True, True, False, True, True, False, True, True]
expected_confidence = (5, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 114')
test = [True, True, True, False, True, True, False, False, True, True, False, False, False, False, False, False, False, True, True, False, False, True, True, True, False, True, True, True, False, True, False, False, True, False, True, False, False, False, True, True, False, True, True, True, False, True, True, True, True, False, False, False, False, True, True, True, True, False, False, False, True, True, False, True, True, False, False, False, False, True, True, False, False, False, False, True, False, True, False, True, True, True, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, True, False, False, True, False, False, True, False, False, False, False, True, True, True]
expected_confidence = (2001599834386887, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 115')
test = [True, True, True, False, False, False, True, False, True, False, False, False, False, True, False, True, False, True, False, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, False, False, False, False, True, False, True, True, False, True, True, False, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, True, False, False, False, False, False, False, True, False, True, True, False, True, False, True, False, False, True, False, True, True, True, False, True]
expected_confidence = (1, 1)
expected_similar_patterns = 1
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 116')
test = [False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, True, True, False, True, False, False, True, False, False, True, True, False, True, False, False, False, True, False, True, False, False, False, True, True, False, False, True, True, False, True, True, False, False, False, False, False, True, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, True, False, True, False, True, False, False, False, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, False, False, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 117')
test = [False, False, False, True, False, False, True, True, False, False, True, True, True, True, False, True, True, True, False, False, True, True, False, False, False, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, False, False, False, True, False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, False, True, True, True, True, False, False, True, True, True, True, True, False, False, False, False, False, True, False, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, False, True, False, False, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 118')
test = [True, False, True, True, False, True, True, True, True, False, False, True, False, False, False, True, False, True, False, False, True, False, False, False, False, False, True, False, False, False, True, True, True, True, False, True, False, True, False, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True, False, False, True, True, True, True, False, True, True, False, True, True, True, True, False, False, True, False, True, True, True, False, False, False, True, True, True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, True, False, True, True, False, False, True, False, True, False, True, False, True, False, True, True, False, True, False, False, True, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 119')
test = [False, True, True, False, True, False, False, False, False, True, True, False, True, False, False, True, True, False, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, True, False, False, True, False, True, False, True, False, True, True, False, False, False, False, True, False, True, True, False, False, True, False, False, True, True, False, True, True, True, False, True, False, True, False, True, True, False, False, True, False, False, True, True, False, False, True, True, False, False, True, False, True, True, False, False, False, False, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, True, True, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 120')
test = [True, True, True, True, False, False, True, False, True, True, False, True, True, True, True, False, True, False, True, True, False, False, True, False, True, True, True, True, False, False, False, True, True, False, True, True, True, False, True, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, True, False, False, True, True, True, True, False, False, True, False, False, True, False, False, True, True, False, False, False, True, True, True, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, True, True, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 121')
test = [True, True, False, False, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, True, True, False, False, True, False, False, True, False, False, False, True, False, True, False, True, True, True, False, False, True, True, False, False, False, True, True, False, True, True, False, False, True, False, True, False, True, False, False, True, False, False, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, False, False, True, True, True, False, False, False, False, True, False, True, False, True, False, True, False, False, True, False, False, True, False, True, False, False, False, False, True, False, False, True, False, True, True, False, False, False, False, True, False, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 122')
test = [False, True, True, True, True, False, False, False, True, True, False, False, True, True, True, False, False, True, True, True, True, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True, True, True, True, True, False, False, False, False, True, True, True, False, True, False, True, True, False, True, False, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False, True, False, False, True, True, False, True, False, False, True, False, True, True, False, False, True, True, False, True, False, True, False, True, True, True, True, True, True, True, False, True, True, False, False, True, True, True, False, False, False, False, True, False, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 123')
test = [True, True, False, False, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, False, False, False, True, True, False, True, True, True, True, True, True, True, False, False, True, False, True, False, False, False, False, False, True, False, True, False, True, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, False, True, True, False, True, True, False, True, False, False, True, True, False, False, False, False, False, False, False, True, False, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, True, True, True, False, False, True, False, False, False, True, False, False, True, True, False, True, True, True, False, True, True, True, True]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 124')
test = [True, False, True, True, False, True, True, False, False, False, True, True, True, False, True, True, False, True, True, True, True, True, False, True, True, False, False, False, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, False, False, False, True, True, False, False, True, False, True, True, False, False, False, True, True, False, True, True, False, False, True, False, False, True, True, True, True, False, True, False, False, True, False, False, False, False, False, False, True, True, False, False, False, False, True, True, True, True, False, False, True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, True, True, True, False, False, True, True, False, False, True, False, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 125')
test = [True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True, True, True, False, True, False, False, False, False, True, False, True, True, True, True, False, True, False, True, False, True, False, True, False, False, True, True, True, True, False, True, True, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, True, False, False, True, False, False, True, True, True, False, True, True, False, True, True, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, True, False, True, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 126')
test = [False, False, True, False, True, True, False, False, True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, True, False, True, True, False, False, True, False, False, False, False, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, True, True, False, False, True, True, False, False, True, True, True, True, False, False, True, False, False, False, False, False, True, False, True, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, True, False, False, False, False, False, True, True, False, True, False, True, False, True, False, True, False, False, True, False, False, True]
expected_confidence = (2573485501354569, 18014398509481984)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 127')
test = [True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, True, True, True, True, True, True, False, True, False, False, False, True, True, False, True, True, True, False, True, True, False, True, True, False, False, True, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, False, False, True, False, False, True, False, False, False, True, False, True, False, True, False, True, False, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 128')
test = [True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, True, False, False, True, False, True, False, False, True, False, True, True, False, True, True, True, False, True, True, True, False, True, True, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, True, True, False, True, False, False, True, True, False, True, True, False, False, False, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, True, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, True, True, True, True, True, False, True, True, False, True, False, False, True, False, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 129')
test = [True, True, False, True, False, False, True, True, False, True, True, True, True, True, False, True, False, True, False, False, False, True, False, True, True, True, False, False, True, False, False, False, False, True, True, False, True, False, False, True, True, False, True, True, False, False, True, True, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, True, False, True, False, True, True, True, True, False, True, True, True, False, False, True, False, True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, False, True, True, False, True, True, True, True, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 130')
test = [False, True, True, True, False, False, False, False, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, True, False, True, True, False, True, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, True, False, True, True, True, False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, True, True, False, False, True, False, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, True, False, False, True, True, False, False, True, False, True, True, True, True, False, True, False, True, True, True, False, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, False, True, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 131')
test = [False, True, True, False, True, False, True, False, True, True, False, False, True, False, True, True, True, False, False, True, False, False, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, False, False, True, True, True, True, True, False, False, False, True, False, False, True, True, False, True, True, False, True, False, True, True, True, True, True, False, True, False, True, True, False, False, True, True, False, False, False, False, False, False, True, False, False, False, True, True, False, True, True, False, True, True, True, True, False, True, False, True, False, True, True, True, True, False, True, True, True, True, False, False, False, True, True, True, True, False, True, False, True, False, True, False, True, True, False, False, False, False, False, False, False, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 132')
test = [False, False, True, True, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, False, False, True, False, True, True, False, False, False, True, True, True, False, True, True, True, False, True, False, True, False, True, False, False, False, True, False, True, True, False, True, False, True, False, True, False, True, True, True, True, False, True, True, True, False, False, False, True, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, True, False, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, True, False, True, True, True, False, False, False, True, True, True, True, False, False, True, False, True]
expected_confidence = (3602879701896397, 9007199254740992)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 133')
test = [True, False, True, False, True, False, False, False, True, False, False, True, True, False, True, True, True, False, False, False, False, False, True, False, False, True, True, True, True, False, False, True, True, False, True, False, False, True, False, True, True, False, False, True, True, False, True, True, True, True, True, False, True, True, False, True, False, False, True, True, False, False, True, False, False, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, False, False, True, True, True, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, True, True, False, True, False, True, False, True, True, False, True, False, False, False, True, True, True, False, True, False, False, False, True, False, True, False, True, True, False]
expected_confidence = (7, 16)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 134')
test = [False, True, False, False, False, False, False, False, False, False, False, True, True, True, False, False, True, True, False, False, False, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, False, True, False, True, False, False, True, True, False, False, True, False, False, False, True, False, False, True, False, True, True, False, False, False, True, True, True, False, True, False, False, True, False, True, True, False, True, False, True, True, False, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, True, True, False, False, True, False, True, True, True, False, False, True, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, True, True, True, False]
expected_confidence = (6004799503160661, 36028797018963968)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 135')
test = [True, False, True, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, False, True, False, True, True, True, True, False, False, True, False, True, False, False, True, True, False, True, True, False, True, True, True, True, False, False, True, False, False, True, True, False, False, False, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, False, True, True, True, False, False, True, False, True, False, True, False, True, False, True, False, False, True, False, False, True, False, True, False, True, False, True, True, True, False, False, False, True, True, True, True, True, False, False, True, True, False, True, False, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, False, False, False, False, False]
expected_confidence = (3602879701896397, 18014398509481984)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 136')
test = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, False, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, False, False, False, False, True, False, False, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, False, False, False, True, True, True, False, True, True, False, False, False, True, True, False, False, True, True, False, True, True, False, False, False, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, True, False, True, False, True, True, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 137')
test = [False, False, True, True, False, False, True, True, True, True, False, False, True, False, False, True, True, False, False, True, False, False, False, True, True, False, False, False, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, True, True, True, True, True, True, False, False, True, False, False, False, True, False, True, True, False, True, False, False, True, True, False, False, False, False, False, True, False, True, False, True, False, True, False, False, True, True, False, False, True, True, True, False, False, False, True, True, False, True, False, True, False, False, False, False, True, False, False, True, True, True, True, False, False, True, False, False, True, True, True, True, True, False, False, False, True, False, True, True, True, False, True, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 138')
test = [False, True, False, True, True, False, True, False, True, False, True, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, True, True, True, False, False, True, False, True, True, True, True, True, False, True, False, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, False, False, True, False, True, False, False, False, True, False, True, True, False, False, False, True, False, False, True, True, False, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, False, False, False, True, True, False, False, False, True, False, True, False, False, False, False, True, True, False, True, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 139')
test = [True, False, False, True, True, True, False, False, True, False, True, True, False, True, True, False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, False, True, False, True, True, True, False, False, True, False, False, False, False, False, False, True, False, True, True, True, True, True, False, False, False, False, True, False, False, False, True, False, True, True, False, True, False, False, False, False, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, True, True, True, False, True, False, False, True, True, True, True, False, False, True, False, True, False, True, True, False, True, True, False, False, False, False, True, False, False, False, False, False, False, True]
expected_confidence = (3275345183542179, 9007199254740992)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 140')
test = [False, True, False, False, False, False, False, True, False, True, True, True, False, True, False, True, False, False, True, True, True, False, False, True, False, True, True, False, True, True, False, True, True, True, False, True, True, True, False, True, True, False, False, False, True, False, True, True, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, False, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, True, False, False, True, True, False, True, True, False, True, False, True, False, True, False, True, True, False, True, True, True, True, False, True, False, True, True, True, False, True, True, False, False, True, True, True, False, False, False, False, True, True, True, True, False, False, False, True, True, False, False, True, False, True, False, True, True, False]
expected_confidence = (2501999792983609, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 141')
test = [False, False, False, True, True, False, False, True, True, True, False, False, True, True, True, False, False, False, True, True, True, True, False, False, True, True, False, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, False, True, True, False, False, False, True, True, False, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, False, False, True, False, False, False, True, True, True, False, True, True, False, True, False, False, False, False, True, True, True, True, True, False, False, False, True, True, False, True, True, False, False, False, True, False, True, False, False, False, True, False, True, True, True, False, True, False, False, True, False, False, True, True, False, True, False, False, True, True, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 142')
test = [True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, False, False, True, False, True, True, True, True, True, True, True, True, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, True, True, True, True, True, True, False, True, False, True, False, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, True, True, True, False, True, False, True, True, True, False, True, False, True, True, False, False, True, True, True, True, True, False, True, False, True, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, False, True, True, True, True, False, False, False, True, False, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, True, True]
expected_confidence = (2001599834386887, 2251799813685248)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 143')
test = [True, False, True, True, False, True, True, False, True, False, False, True, False, False, True, True, True, False, False, True, False, True, False, True, False, False, True, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, True, True, True, False, False, False, True, False, False, True, True, True, False, False, False, False, False, True, False, False, True, False, False, True, False, True, True, True, False, True, False, True, False, False, False, False, False, False, False, True, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 144')
test = [True, True, False, False, False, False, False, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, True, True, False, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, False, True, True, False, True, True, False, True, True, False, True, False, True, True, True, False, False, False, False, False, True, True, False, False, False, False, True, True, False, False, True, True, False, True, False, True, False, False, True, False, True, False, True, True, True, True, True, True, False, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, True, True, False, False, True, True, True, False, True, True, True, True, True, False, False, False, True, True, False, False, True, True, True, False, False, False, False, True, True, True, True, True, True, False]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 145')
test = [True, True, True, True, False, False, False, True, True, True, True, False, True, True, True, False, True, False, True, False, True, False, False, False, False, True, True, True, False, False, False, True, True, False, True, False, False, True, True, False, True, False, True, True, False, False, True, False, True, False, True, False, True, True, False, False, True, False, False, True, False, True, True, True, True, False, True, False, False, False, False, True, True, True, True, False, True, True, True, True, True, False, False, False, False, True, False, True, True, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, False, False, False, True, True, False, True, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, True, True, False, False, True, False, False, False, False, True, True, True, False, True, False, True, True, False]
expected_confidence = (2001599834386887, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 146')
test = [False, False, True, True, True, False, True, True, True, False, False, True, False, False, True, True, True, False, True, True, True, False, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, True, True, True, True, False, True, False, False, False, True, True, True, False, True, False, True, False, False, True, True, False, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, False, True, True, True, False, False, True, False, False, True, True, True, True, False, False, False, False, True, True, True, True, True, False, False, False, False, True, True, True, True, False, True, False, True, True, False, False, True, False, False, True, False, True, False, True, False, False, True, True, True, False, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 147')
test = [True, False, False, True, False, False, True, True, True, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, True, True, False, True, False, False, True, False, True, True, True, True, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, True, False, True, True, True, True, True, False, False, False, True, True, False, False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, True, False, False, True, False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, True, True, False, True, True, True, True, False, False, False, True, False, True]
expected_confidence = (1, 1)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 148')
test = [True, True, True, False, False, True, False, True, True, True, False, True, True, False, False, True, False, True, True, True, True, False, False, False, True, True, True, False, False, True, False, True, True, False, True, False, False, False, True, True, False, True, True, False, True, True, True, False, True, True, False, False, True, True, False, False, False, False, False, True, True, False, True, True, True, True, True, False, False, False, True, False, True, False, True, True, False, True, False, True, True, True, False, False, False, True, True, False, True, True, True, True, False, False, False, False, True, False, True, True, False, True, True, True, True, False, True, True, True, True, False, True, True, True, True, False, True, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, True, False, False, False, True, False, True, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 149')
test = [False, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, False, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, False, True, True, True, True, True, False, True, False, False, True, True, True, True, True, False, True, True, True, False, True, True, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, True, True, False, True, False, False, True, True, False, True, True, True, True, False, False, False, True, False, False, True, True, False, True, False, False, False, False, False, False, False, True, False, True, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False]
expected_confidence = (3152519739159347, 4503599627370496)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 150')
test = [True, False, False, True, False, True, True, True, False, True, True, False, True, True, False, True, False, False, False, True, True, False, False, True, True, False, False, False, True, False, False, True, False, True, True, True, False, True, True, True, True, False, True, False, True, True, True, True, False, False, True, False, False, True, True, False, False, True, True, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, True, False, True, False, True, False, False, True, False, True, False, True, True, False, True, False, True, False, False, True, False, False, True, True, False, False, False, True, False, True, True, False, True, False, False, True, True, True, True, True, True, False, False, False, True, False, False, True, False, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 151')
test = [False, False, True, True, False, False, False, True, True, True, False, False, True, False, True, False, True, False, True, False, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True, False, False, True, True, True, False, False, False, True, False, False, True, False, False, True, True, True, True, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, True, False, False, True, True, True, True, False, False, True, False, False, True, True, False, True, False, False, True, False, True, True, True, True, True, True, True, True, False, False, True, False, True, False, True, False, False, False, False, False, False, True, False, False, False, True, True, True, False, True, False, True, True, False, False, False, False, True, True, False, False, False, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 152')
test = [False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, False, False, False, True, True, False, False, False, False, True, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, False, True, True, False, False, False, True, False, False, True, False, True, False, True, False, False, False, False, True, True, False, True, True, False, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, False, False, False, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, False, True, True, True, False, False, True, True, True, False, False, False, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 153')
test = [False, True, True, False, True, False, True, False, False, True, False, True, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, False, True, True, False, True, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, False, True, True, False, True, True, False, True, False, False, True, False, False, True, False, True, False, False, False, True, True, False, True, True, False, True, False, False, True, True, False, False, True, False, False, True, False, True, False, True, False, True, False, False, False, True, True, False, False, True, False, False, False, True, True, True, True, True, False, False, True, False, True, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, False, False, False, False, True, False, False, True, True, True, True, True, True, False, False, False, True, True, False, True, True, True, True, False]
expected_confidence = (2001599834386887, 2251799813685248)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 154')
test = [True, True, True, True, True, True, False, True, True, True, False, False, True, False, True, False, False, False, True, True, True, True, False, True, True, False, True, False, True, False, False, False, False, True, True, False, True, True, False, True, False, False, True, True, True, True, True, False, True, True, False, True, True, False, False, False, True, False, True, True, True, False, True, False, True, True, False, False, False, False, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, False, False, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, False, False, False, True, False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, True, True, False, False]
expected_confidence = (5404319552844595, 9007199254740992)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 155')
test = [True, False, True, True, False, True, False, False, True, True, False, True, False, True, True, False, False, True, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, False, True, True, True, True, False, True, True, True, False, True, True, True, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, True, False, False, True, True, True, False, True, True, False, True, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, True, False, True, False, True, True, True, True, True, True, False, False, True, False, True, False, False, True, False, True, True, True, False, True, True, False, False, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, False, True, False, False, False, True, True, False, False, True, False, False, False, True, True, True, True, False, True, False, True, False, False, True, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 156')
test = [True, True, False, False, True, True, False, False, False, True, False, True, False, False, False, True, True, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, False, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, True, False, True, True, False, False, False, False, True, True, True, False, True, False, True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, True, False, True, True, False, True, False, False, False, False, True, True, False, False, False, False, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, True, False, True, True, False, True, True, True, True, False, False, True, False, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 157')
test = [True, True, True, False, False, False, True, False, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, False, False, True, False, True, False, True, False, False, True, True, False, True, False, True, False, False, False, False, True, False, True, False, True, True, True, False, True, True, False, True, True, True, True, False, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, True, True, True, True, False, False, True, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, False, False, True, False, True, False, True, True, True, False, False, False, False, False, True, True, True, True, False, True, False, True, False, False, True, False, True, True, True, True, True, False, False, True, True, True, False, False, False, True, True, False, True, True, False, True, True, False, False, True, False, True, False, False, False, False, True, False, True, True, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 158')
test = [False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, True, True, False, True, False, False, False, True, True, False, False, False, True, True, True, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, True, True, True, False, True, True, False, True, False, True, False, False, False, True, False, False, False, True, False, False, True, True, True, False, True, True, True, False, True, False, False, False, False, True, True, True, True, False, False, False, True, True, True, False, False, True, True, True, True, True, True, False, False, False, True, True, False, True, False, False, True, True, False, False, True, True, True, False, True, False, False, False, False, True, True, True, False, False, False, True, False, True, True, True, False, False, False, False, False, True, False, True, False, False, True, False, False]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 159')
test = [False, True, False, False, False, True, True, False, False, True, False, True, True, False, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, False, True, True, True, False, False, True, False, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True, True, False, False, True, False, True, True, False, False, False, False, False, True, False, True, True, False, False, False, True, True, True, True, False, True, False, False, False, True, True, True, True, True, False, True, False, False, True, False, True, True, False, True, True, True, False, True, False, False, False, True, False, True, True, True, False, False, True, False, True, False, True, True, False, True, True, True, False, False, False, True, False, True, True, True, False, True, False, True, True, False, True, False, False]
expected_confidence = (948126237341157, 2251799813685248)
expected_similar_patterns = 11
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 160')
test = [True, True, False, False, True, True, True, False, True, False, True, True, True, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, True, False, True, False, True, False, False, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, True, False, False, True, False, True, True, False, True, False, True, False, True, True, False, False, False, False, False, False, True, False, False, True, False, True, False, True, False, False, True, False, True, False, True, True, True, False, False, True, True, False, True, True, False, False, True, False, False, False, False, False, True, False, True, True, True, True, True, True, True, True, False, False, True, False, False, False, False, True, False, True, True, True]
expected_confidence = (1, 1)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 161')
test = [True, False, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, False, False, False, False, True, True, False, True, False, False, True, False, True, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, True, False, False, True, False, True, True, True, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, True, True, True, False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, True, False, True, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, False, True, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 162')
test = [False, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, True, False, False, False, True, True, True, False, True, True, False, True, True, False, False, False, False, True, False, True, False, False, True, True, True, True, True, False, False, True, False, True, False, True, False, True, False, False, True, True, True, False, True, False, False, False, False, False, False, True, True, True, False, False, True, True, False, True, False, True, True, False, False, True, True, True, True, False, False, False, False, True, True, False, True, False, True, False, False, False, False, True, True, False, True, True, True, False, True, True, True, True, True, False, True, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 163')
test = [False, False, True, False, True, True, False, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, False, False, False, False, True, False, True, False, True, False, True, True, False, True, True, True, True, False, True, True, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False, True, True, True, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, True, False, True, True, False, True, True, False, False, False, True, True, False, False, True, False, False, True, True, True, False, True, True, True, True, False, False, True, False, False, True, True, True, False, False, True, True, False, False, True, True, True, True, False, False, True, True, True, False, False, True, False, True, False, True, True, True, False, True, False, True, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 164')
test = [False, True, True, False, False, False, False, False, False, True, True, True, False, False, False, False, True, False, True, True, False, False, False, True, True, False, False, False, True, False, False, False, True, True, True, True, True, True, True, False, True, True, False, False, True, True, False, True, True, True, False, True, False, True, False, False, False, False, True, True, True, False, True, True, True, True, False, False, False, True, False, False, False, False, False, False, True, True, True, True, True, True, False, True, False, True, False, False, False, True, True, False, False, True, True, False, True, False, True, True, True, False, False, True, False, False, False, True, True, True, True, True, True, False, True, False, True, True, False, False, False, True, True, True, True, False, True, False, True, True, False, True, False, False, False, True, True, True, False, False, False, False, True, True, True, False, False, False, False, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 165')
test = [False, True, False, True, True, True, True, False, False, False, False, True, False, False, True, True, True, True, True, True, True, False, True, False, False, True, False, False, True, True, True, True, False, False, False, False, True, True, True, True, True, True, True, False, True, True, False, False, True, False, False, False, True, False, False, True, False, True, True, False, False, True, True, True, True, True, False, False, False, False, False, False, True, False, True, True, True, False, False, True, True, True, False, False, True, False, False, False, False, False, True, False, True, True, False, False, False, True, True, False, False, False, False, True, False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False, True, True, False, False, False, False, False, True, True, True, False, True, False, False, False, False, False, False, True, False, False, True, True, False, True, True, False, False, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 166')
test = [True, False, False, True, False, True, True, False, False, True, True, False, True, False, True, False, False, False, False, False, False, True, True, False, False, True, False, False, False, False, True, True, True, False, True, False, False, True, True, False, False, False, False, True, False, True, True, True, False, True, True, False, False, False, True, False, True, True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, False, True, True, True, True, True, False, True, False, True, True, True, False, True, False, True, False, False, True, True, False, True, True, True, True, False, True, False, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, False, False, False, False, True, True, False, True, True, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 9
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 167')
test = [True, True, True, False, False, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, True, False, True, False, True, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, False, True, False, False, True, True, True, False, False, False, True, True, False, True, True, True, True, False, False, True, False, True, False, False, True, False, False, False, False, False, True, True, True, False, True, True, True, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, True, False, True, False, True, False, False, False, False, True, False, True, False, True, True, False, True, True, False, True, False, False, True, False, True, False, True, True, False, False, True, False, True, False, False, True, False, True, True, True, True, True, False, False, True, True, False, True, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 168')
test = [False, False, True, False, False, True, False, True, True, False, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, True, True, True, True, True, False, False, False, False, False, False, True, True, True, False, True, True, False, True, True, False, False, False, False, True, True, False, True, False, True, True, False, True, False, True, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, False, True, True, False, False, True, True, False, True, True, True, False, True, False, True, False, False, False, True, True, True, True, False, False, False, False, True, False, False, True, False, True, False, False, True, False, True, False, True, False, False, True, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, True, False, False, True, True, False, False, False, True, True, False, False, True, False, False, True, True, False, True, False, True, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 169')
test = [False, True, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, True, False, True, True, False, True, True, False, False, True, False, False, True, False, True, False, True, False, False, True, False, False, True, True, False, True, True, False, True, True, False, True, False, True, True, False, True, True, True, False, False, True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, False, True, True, False, False, False, True, False, False, True, False, True, True, False, True, False, False, True, True, True, False, True, True, False, False, True, False, True, False, False, False, True, True, True, True, False, True, True, False, False, False, False, True, False, False, True, True, False, False, True, True, False, False, False, True, False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True, False, True, False, False, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 170')
test = [True, True, True, False, True, False, True, False, False, True, False, False, False, True, False, True, True, True, True, False, True, True, True, False, True, True, True, False, True, False, False, True, False, True, False, True, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, False, False, True, True, True, True, False, False, True, True, True, True, False, True, True, False, True, False, True, False, True, False, True, True, False, False, False, False, True, True, False, True, False, True, False, True, False, True, False, False, False, True, True, False, True, False, True, True, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, True, False, True, False, True, True, True, True, True, False, False, True, True, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, True, True, False, True, False, False, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, False, True, False, True]
expected_confidence = (5298352502788819, 9007199254740992)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 171')
test = [False, False, False, True, True, True, True, True, True, False, False, True, False, False, False, False, True, False, False, True, False, True, True, False, False, True, True, True, True, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, False, True, True, True, False, False, False, False, True, True, False, False, True, False, False, True, True, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, True, False, True, False, False, True, True, False, True, False, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, True, True, True, True, True, True, False, True, True, True, False, False, False, False, True, True, False, True, True, False, False, True, False, False, True, False, False, False, True, False, False, False, False, False, True, False, True, True, False, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, False, True, False, True, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 172')
test = [True, False, True, True, False, False, True, False, True, True, False, True, True, True, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, True, False, True, True, True, False, True, False, False, False, True, False, True, False, True, True, False, True, True, True, True, False, False, False, False, True, True, False, True, True, True, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, False, False, False, False, True, False, True, True, True, True, False, True, False, False, True, True, False, False, True, False, False, False, True, False, True, False, True, True, True, False, False, False, False, True, True, True, False, False, True, False, True, True, False, True, False, False, False, True, True, True, False, False, False, False, True, True, False, True, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, True, False, True, True, True, True, True, False, True, False, False, False, True, True, True, False, False, False, True, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 173')
test = [False, False, False, False, True, False, False, False, False, True, False, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, False, True, True, False, False, False, False, False, True, True, True, True, True, True, True, False, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, True, False, False, True, True, True, False, True, False, True, True, False, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, False, False, False, False, False, True, True, False, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, True, True, False, False, True, False, False, False, False, False, True, False, True, True, True, True, True, True, True, False, True, True, True, False, False, True, True, False, True, True, True, False, False, False, True, False, False, True, True, True, True, True, True, True, True, True, True, False]
expected_confidence = (1, 1)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 174')
test = [False, False, True, True, True, False, True, True, False, True, False, True, False, False, False, False, True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, True, False, False, False, True, True, False, True, True, False, False, True, False, True, False, True, False, True, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, False, False, False, True, False, False, True, False, True, False, False, True, True, True, True, False, True, True, False, True, True, False, False, True, True, False, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, False, True, False, True, True, True, False, True, True, True, False, False, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 175')
test = [True, True, False, False, True, False, False, True, True, True, False, False, False, True, True, True, True, False, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, True, False, False, True, True, True, False, True, True, False, True, True, False, False, False, True, True, False, False, True, False, False, False, True, False, True, False, True, True, True, True, False, True, False, False, True, False, True, False, True, True, False, True, False, False, False, True, True, False, True, False, False, True, False, False, True, False, False, False, False, True, True, False, True, False, False, False, True, False, False, True, True, True, True, False, True, False, True, False, False, False, False, False, False, True, False, False, True, True, False, True, False, True, False, True, True, True, False, True, True, True, True, True, True, False, False, True, True, False, True, False, False, False, False, True, False, False, True, True, True, True, True, True, True]
expected_confidence = (1, 4)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 176')
test = [True, True, False, True, True, True, False, False, True, False, False, False, False, True, True, False, True, False, False, True, True, True, True, False, True, True, False, True, True, False, False, False, True, True, True, True, False, False, True, True, True, True, False, False, True, True, True, False, True, False, True, False, False, True, False, False, True, True, False, True, False, False, False, True, True, True, True, False, False, False, True, False, False, True, True, False, True, False, False, True, True, True, False, False, True, True, True, True, True, True, False, True, False, False, False, True, False, False, False, False, False, True, True, True, True, True, False, True, False, True, True, False, True, False, True, False, True, True, True, False, False, True, True, True, False, True, False, True, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, True, False, True, False, False, False, True, False, False, True, True, True, True, False, False, True, True, False, True, False, False, True, True, False, True, False, False, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 177')
test = [False, True, True, True, True, False, False, True, False, True, False, True, False, True, True, False, False, True, True, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, True, True, True, False, True, False, True, False, False, False, False, False, False, True, True, False, False, False, True, True, True, False, False, True, False, False, True, True, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True, True, False, True, True, True, True, False, True, False, False, True, False, True, True, False, False, True, False, True, False, False, False, True, False, True, True, True, True, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, True, True, False, False, False, True, False, False, True, True, False, False, False, False, True, True, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, False, False, False, True, True, False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 178')
test = [True, True, True, False, True, True, False, False, True, True, True, True, False, False, False, True, True, True, True, False, False, False, False, True, False, False, False, True, True, True, False, False, True, False, False, False, False, True, True, False, False, False, True, False, True, False, True, True, True, True, False, True, True, True, False, True, True, True, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, True, True, False, False, False, True, False, True, False, False, True, False, False, True, False, False, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, False, True, True, False, False, True, False, True, False, False, False, True, True, False, True, False, False, False, False, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, True, False, True, False, True, True, False, False, False, False, False, False, True, False, False, False, True, False, False, False]
expected_confidence = (6928614811339225, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 179')
test = [True, False, True, False, False, True, True, False, True, False, False, True, True, False, False, False, False, True, False, True, True, True, False, False, False, False, True, False, False, True, False, True, True, True, True, False, True, True, True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, True, False, True, True, False, True, False, True, False, False, False, True, False, False, False, True, True, False, False, False, True, True, True, True, False, True, False, False, True, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, True, True, False, True, False, False, True, False, True, False, False, True, True, True, True, False, False, False, False, False, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, True, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, True, True, True, True, True, False, False, True, False, False, False, False]
expected_confidence = (3117876665102651, 4503599627370496)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 180')
test = [True, False, False, False, False, False, False, False, True, True, True, True, False, True, False, True, False, False, False, True, True, False, True, False, True, False, False, True, True, True, False, True, True, False, False, True, False, False, True, False, True, True, True, True, True, True, True, True, False, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, True, True, False, True, True, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, True, True, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, True, False, True, False, False, True, True, False, False, True, True, False, False, True, False, True, True, False, True, True, False, False, True, False, False, False, False, True, True, True, True, True, False]
expected_confidence = (5, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 181')
test = [False, False, True, True, False, True, False, True, False, True, False, False, False, False, False, True, True, False, True, False, True, False, True, False, True, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, True, False, True, True, True, False, True, False, False, True, False, True, True, False, True, True, True, True, False, True, False, True, True, False, True, False, True, True, True, True, True, True, False, False, False, True, False, False, True, False, True, False, True, True, False, False, False, False, False, False, False, True, True, False, False, False, True, True, True, False, True, False, False, False, False, True, True, True, False, True, True, True, False, True, False, False, True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, True, True, False, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, False, False, True, True, True, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 182')
test = [True, False, False, True, False, False, False, True, False, False, True, False, False, True, False, True, True, True, True, True, False, True, False, True, True, True, True, False, False, False, False, False, True, False, True, True, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, True, False, False, False, False, True, True, False, False, True, False, False, True, True, True, False, False, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, False, True, False, False, True, True, False, True, True, False, True, False, False, True, False, True, True, True, False, True, True, True, False, True, True, True, True, False, True, False, False, False, False, True, True, True, True, False, False, True, True, False, True, True, True, False, False, True, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, False, False, True, True, True, True, False]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 183')
test = [True, True, False, False, True, False, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, False, True, False, True, False, False, True, False, True, True, False, False, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, True, False, False, True, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, True, True, False, False, False, True, False, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, True, True, True, True, True, False, False, True, False, True, True, False, True, True, True, True, False, False, True, False, False, False, True, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, True, False, True, False, True, False, True, True, False, True, False, True]
expected_confidence = (3275345183542179, 9007199254740992)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 184')
test = [False, False, True, True, True, False, True, True, True, False, True, False, True, True, True, False, False, True, True, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, False, False, False, True, True, False, False, True, True, True, True, False, True, False, False, True, False, True, True, True, False, True, False, True, True, False, False, False, False, False, False, False, True, False, False, False, True, True, True, True, False, False, False, False, True, True, False, False, False, True, True, False, False, True, False, True, True, False, False, False, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, False, True, False, False, False, True, False, False, True, False, False, True, True, False, True, True, False, False, False, True, True, False, False, True, False, False, True, True, True, False, True, False, True, True, True, True, False, False, False, False, True, True, True, False, True, True, False, False, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 185')
test = [False, False, False, False, False, True, False, True, False, True, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, False, True, True, True, True, True, False, True, True, False, True, True, True, False, True, True, True, True, False, False, True, True, False, True, False, False, False, False, False, False, True, False, True, True, True, False, True, True, False, True, True, False, True, False, False, True, True, False, True, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, False, False, False, True, True, False, False, True, True, True, False, True, False, True, False, False, False, True, False, True, True, True, True, False, True, True, False, True, True, False, False, False, False, False, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, True, False, True, True, True, True, False, True, True, False, True, True, False, False, True, False, False, True, True, False, True, True, True, False, False]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 186')
test = [False, True, True, False, False, True, True, True, False, True, False, False, True, False, True, False, False, True, True, False, True, True, False, False, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, False, True, False, False, False, False, True, True, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, True, False, True, True, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, True, True, False, False, False, True, False, False, True, True, False, True, False, True, True, False, True, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, True, False, True, True, True, False, False, False, True, False, True, True, False, True, True, True, False, True, True, True, False, True, False, False, True, False, True, False, False, True, True, True, False, True, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, False, False, True, False, False, True, False, True, False, True, False, False, True, False, False]
expected_confidence = (7505999378950827, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 187')
test = [False, False, True, False, False, False, False, True, True, True, True, True, False, True, False, False, False, True, False, False, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True, False, False, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, False, False, False, False, False, False, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, True, True, False, False, False, False, True, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, True, True, True, True, False, False, False, False, True, False, False, True, False, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, True, True, True, True, False, False, False, False, True, False, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, False, False, False, True, False, True, True, True]
expected_confidence = (1228254443828317, 2251799813685248)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 188')
test = [False, False, True, True, True, True, False, False, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, True, False, True, False, False, False, False, True, True, True, True, True, True, False, True, True, True, False, False, True, True, True, False, False, True, False, False, False, True, False, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, False, True, True, False, True, False, True, True, True, False, False, True, False, True, False, False, True, True, True, False, False, True, True, False, True, False, True, False, True, True, True, False, False, True, False, False, True, True, False, False, True, False, True, True, True, True, True, True, True, False, True, False, False, True, False, True, False, False, False, False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, False, False, False, True, True, True, True, False, False, False, True, False, False, False, True, True, False, False, False, False, True, True, True, False, True, False, False]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 189')
test = [True, True, True, False, True, False, True, True, True, True, True, False, False, True, False, True, False, False, False, False, True, False, False, True, True, False, True, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True, True, False, True, True, True, False, True, True, False, False, True, False, False, False, False, False, True, True, True, True, True, False, True, True, True, False, False, True, False, False, True, True, True, False, False, False, False, False, True, True, True, False, False, False, True, False, False, True, True, False, True, False, True, True, True, False, False, False, False, False, False, True, False, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, True, False, False, False, False, False, False, False, True, True, True, True, False, True, True, True, True, False, False, False, True, False, False, True, True, False, False, True, False, True, False, True, False, True, True, False, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, False, True, False, False, True, False, True, False, True, False]
expected_confidence = (7720456504063707, 18014398509481984)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 190')
test = [False, False, True, False, True, False, False, True, False, True, True, False, True, False, True, False, False, False, True, False, False, True, False, False, False, False, True, True, True, True, True, False, False, False, True, True, True, False, False, False, False, True, True, False, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, False, True, False, True, False, True, True, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, False, True, True, True, True, True, True, False, False, False, True, True, True, False, True, False, False, False, False, False, False, True, True, False, True, True, False, False, False, True, False, False, True, False, False, False, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, True, False, False, False, True, True, False, True, True, False, True, False, True, False, False, True, True, True, True, True, True, True, False, True, False, True, True, True, True, False, False, False, False, True, False, True, False, False, False, True, False, True, True, False, True, False, True, True, True, False, False, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 191')
test = [True, True, True, False, False, True, True, True, False, True, True, False, False, True, False, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, True, True, False, True, True, True, False, False, True, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, False, True, False, False, False, True, True, True, False, True, True, False, False, True, False, False, True, False, False, False, False, True, True, False, False, True, False, True, False, True, True, False, True, False, False, False, True, False, False, True, True, False, False, False, True, False, True, True, True, False, True, True, False, True, True, True, False, False, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, False, True, False, False, True, True, False, False, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, False, True, True, False, False, False, False, True, True, False, False, False, True, True, True, False, False, True, True, False, True, False, False, False, False, False, False, True, False, True, False, True, True, True, True, True, False, True]
expected_confidence = (2501999792983609, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 192')
test = [False, True, False, False, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, False, False, True, False, True, True, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, True, False, True, False, True, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, False, False, False, False, False, True, True, False, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, False, False, True, False, False, False, False, False, True, False, True, False, True, True, True, False, False, False, True, False, False, False, True, True, False, False, True, True, False, False, True, True, True, True, False, True, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False, False, False, False, False, True, True, False, True, False, False, False, True, False, True, True, False]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 193')
test = [True, False, True, True, False, True, True, True, True, True, False, False, False, True, False, True, False, True, False, False, True, False, True, False, True, False, False, False, True, False, True, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, False, True, False, True, False, True, True, False, False, True, True, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, True, False, True, True, True, False, True, False, True, False, False, False, False, False, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, True, False, True, True, True, False, False, True, True, False, True, True, True, False, False, False, True, False, False, True, False, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 194')
test = [False, False, True, False, True, False, True, False, False, True, False, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, True, True, False, True, True, False, False, False, True, False, False, False, True, False, False, True, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, True, False, True, False, True, True, False, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, True, False, True, False, True, True, False, True, True, True, False, False, True, False, True, False, True, False, True, False, False, True, False, False, False, True, True, True, False, True, True, True, False, False, False, False, False, False, True, False, True, False, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True, True, True, False, True, False, True, True, False]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 195')
test = [False, True, True, False, False, True, False, False, True, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, True, True, True, False, False, True, True, True, False, True, True, False, True, True, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, True, False, True, True, True, True, False, False, True, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, True, False, False, True, True, False, True, False, True, True, True, True, False, False, False, True, False, True, False, False, True, False, True, False, False, False, False, True, False, True, False, True, False, False, True, False, True, True, False, True, False, False, False, True, False, False, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, True, True, False, False, True, False, True, True, True, True, False, True, True, False, False, False, True, True, False, True, False, True, False, False, True, True]
expected_confidence = (1385722962267845, 2251799813685248)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 196')
test = [False, False, False, True, False, False, True, False, False, False, True, True, False, True, False, True, True, False, False, False, False, True, False, True, True, False, True, True, True, True, False, False, True, True, False, True, True, False, False, True, True, False, False, False, True, False, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, True, False, False, False, False, False, False, True, True, False, False, False, False, False, True, True, False, True, True, False, True, False, False, False, True, False, False, False, False, True, False, True, False, True, False, False, False, True, True, True, True, True, True, True, False, False, False, True, True, False, False, True, False, False, False, False, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, False, False, True, False, False, False, True, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, True, True, False, False, True, False, False, False, True, True, False, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, False, True, False, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 197')
test = [False, False, True, True, True, False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, True, True, True, True, False, True, False, False, False, True, False, True, True, False, True, True, True, False, True, True, False, True, True, False, True, True, False, False, False, False, True, False, True, True, True, True, True, False, False, True, True, False, True, True, False, False, False, False, True, True, True, False, True, True, True, True, True, False, False, False, True, True, True, True, False, False, False, True, True, True, True, False, True, True, True, False, False, False, False, True, False, True, True, False, True, True, True, True, False, False, True, False, False, False, False, True, False, True, True, True, True, True, True, True, False, False, True, False, True, False, True, False, True, True, False, True, False, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, False, False, True, False, True, False, False, False, True, False, False, True, True, False, False, False, False, True, True, True, False, True, True, False, True, True, False, True, True, True, False, True, True, False, False, False, True, False, False, True, True, False, False, True]
expected_confidence = (2001599834386887, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 198')
test = [False, False, True, True, True, True, True, True, False, False, False, False, True, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, True, False, False, False, False, False, True, False, False, True, False, False, True, True, True, False, False, True, True, True, True, True, True, False, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, True, False, False, True, True, True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False, False, True, True, False, True, False, False, True, True, True, False, True, True, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, False, True, True, True, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, False, True, True, False, False, True, True, True, True, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, True, True, True, False, True, True, False, False, True, True, False, True, True, True, False, True, True, False, False, False, True, False, False, False, False]
expected_confidence = (8188362958855447, 18014398509481984)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 199')
test = [True, False, False, False, True, True, False, False, False, False, True, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, True, True, True, False, True, True, True, True, False, False, False, False, True, True, False, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, True, False, True, False, False, False, True, False, False, False, True, True, True, False, False, False, False, True, False, True, True, True, False, False, True, True, False, True, True, False, True, True, False, False, False, False, False, False, False, True, False, True, True, True, True, False, True, False, False, False, False, False, False, False, True, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, False, False, True, True, True, False, True, True, False, False, True, False, True, False, False, True, True, True, False, False, False, True, True, True, True, True, False, False, True, True, False, False]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 200')
test = [True, False, True, False, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, True, True, True, False, True, False, True, False, False, True, True, False, False, False, False, True, False, True, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, False, True, False, False, True, True, False, False, True, True, False, False, True, False, False, True, True, False, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, False, True, False, True, True, True, False, True, False, True, True, True, False, False, True, False, True, True, True, True, False, True, True, False, True, True, False, True, True, False, False, True, True, True, False, False, False, True, False, True, True, False, True, True, False, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, False, True, True, True, True, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 201')
test = [False, True, True, True, True, False, True, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, False, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, True, True, False, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, False, False, True, True, False, False, True, False, True, False, False, False, True, True, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, False, False, False, False, True, False, True, True, True, True, False, False, False, False, True, True, False, False, True, True, True, True, False, False, True, True, True, True, False, False, False, True, False, True, True, False, True, True, False, False, False, True, False, True, False, True, True, False, False, False, True, True, True, False, False, False, True, True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, False, True, False, True, False, False, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 202')
test = [False, True, False, True, False, True, True, False, True, False, True, False, True, True, False, True, True, True, True, False, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, False, False, True, False, True, False, False, False, False, False, False, False, True, True, True, True, False, True, True, True, False, False, False, False, False, True, False, True, True, True, False, True, True, False, True, False, True, True, True, False, False, True, False, True, True, True, False, False, False, True, False, False, True, True, True, False, False, False, True, False, True, False, False, False, True, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, False, True, True, True, True, True, True, True, False, True, True, False, False, False, False, False, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, False, False, False, True, False, False, False, False, False, False, False, True, False, True, True, False, False, True, False, True, True, False, False, True, False, True, False, False, False, False]
expected_confidence = (7005599420354105, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 203')
test = [False, False, False, True, True, True, True, False, False, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, True, True, True, True, False, True, True, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False, False, False, True, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, False, True, True, False, True, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, True, True, False, True, False, False, True, False, True, True, True, False, False, True, False, True, True, True, False, True, False, False, True, True, True, True, False, True, False, True, True, False, False, False, False, True, True, False, False, False, True, True, False, True, False, False, False, False, True, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, True, False, False, False, False, True, False, False, True, True, False, True, False, False, False, False, True, False, True, False, True, False, False, False]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 204')
test = [False, True, False, False, True, False, True, True, False, False, True, False, False, True, False, True, False, True, False, True, True, True, True, True, True, True, False, False, True, False, True, False, True, True, False, True, False, False, True, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, True, False, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, False, False, True, False, True, False, False, False, True, True, False, True, True, False, True, False, False, False, False, False, False, False, True, False, False, True, False, False, True, True, False, False, True, False, False, False, True, False, True, True, True, False, True, True, True, True, False, False, True, True, False, False, True, True, True, False, False, True, False, True, True, False, False, True, True, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, False, True, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, False, True, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 205')
test = [True, True, True, True, False, False, False, True, False, True, True, True, True, False, True, True, True, False, False, True, True, False, True, False, True, False, True, True, False, False, False, False, True, False, True, True, False, True, False, True, False, False, True, False, True, False, False, True, False, False, False, False, False, False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, False, False, True, True, True, True, False, True, True, False, True, False, True, False, False, False, False, False, True, False, False, True, False, False, True, False, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, True, True, True, True, False, True, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, True, False, False, True, True, True, True, True, True, False, False, True, True, True, True, True, False, False, True, False, False, True, True, False, False, True, False, False, True, True, True, False, True, True, False, False, True, True, True, True, False, True]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 206')
test = [False, False, False, True, False, False, True, True, False, True, False, True, False, False, False, False, True, False, True, True, False, True, False, False, True, True, False, True, False, True, True, False, False, True, False, True, False, False, True, False, False, True, True, False, False, False, True, True, False, True, True, True, False, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, True, True, False, True, True, True, True, True, True, False, False, True, False, True, True, False, False, False, False, True, True, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, False, True, False, False, True, False, False, True, True, False, False, False, True, True, True, False, False, False, True, True, False, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, True, False, True, False, False, False, True, False, False, False, True, False, True, True, True, True, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, True, True, True, True, False, False, False, False, True, False, True, True]
expected_confidence = (3, 4)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 207')
test = [True, True, True, True, True, True, False, False, False, True, False, False, False, True, False, False, True, True, False, False, True, False, True, False, False, False, False, True, True, True, False, False, True, True, True, True, False, True, False, True, True, True, True, True, True, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True, True, True, True, False, False, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, True, True, False, True, False, False, True, True, True, True, False, True, False, False, True, False, True, False, False, False, False, False, False, True, True, True, True, False, False, False, True, False, True, False, False, False, False, True, False, True, True, True, True, True, True, False, False, False, True, False, True, True, False, True, True, False, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, True, False, True, False, True, False, False, True, False, True, True, False, False, False, False, False, True, True, True, False, False, True, False, True, True, True, True, True, True, False, True, True, True, True, False, False, False, False, False, True, False, True, False, False, False, True, False, True, True, False, False, False, False, False, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 208')
test = [True, False, True, False, False, True, True, True, True, False, True, True, False, True, True, False, False, False, False, True, True, False, True, False, False, True, True, True, True, False, True, True, False, True, True, True, True, False, True, True, True, True, False, False, False, False, True, False, False, False, True, True, False, True, False, True, True, False, False, True, True, True, True, False, False, True, True, True, True, True, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, False, True, False, False, False, False, False, False, True, False, False, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, False, True, False, True, True, True, True, True, False, False, True, False, True, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, True, True, False, True, True, False, False, True, True, False, True, False, False, False, True, False, False, False, True, False, False, True, False, True, True, True, False, True, True, True, True, True, True, True, False, True, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 209')
test = [True, True, False, False, True, True, True, True, True, True, False, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, False, True, False, True, False, True, True, True, True, True, True, True, False, False, False, False, False, True, False, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, True, False, True, True, True, False, True, True, True, False, True, False, False, True, False, True, True, True, False, False, False, False, True, True, True, True, True, True, False, True, False, True, True, True, True, False, True, False, True, True, True, True, True, False, False, False, False, True, False, True, True, False, False, False, True, False, True, False, True, True, True, True, False, False, True, True, False, True, True, False, True, False, False, True, True, False, True, False, False, False, True, False, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 210')
test = [False, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False, False, True, True, False, False, False, True, False, False, True, False, False, False, True, False, True, True, True, True, False, True, False, False, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, False, True, True, True, False, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, False, False, False, False, True, False, True, False, False, False, False, True, True, False, False, True, True, True, True, False, True, False, False, False, True, False, False, False, True, True, True, True, False, False, False, False, False, False, False, True, True, False, True, True, True, False, True, False, True, False, False, True, True, True, False, False, False, False, False, True, False, False, True, True, True, False, False, True, False, False, True, False, True, False, False, True, True, False, True, True, False, False, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True, True, True, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, False, False, False, True, True, True, False, False, True, False, False, False, True, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 211')
test = [True, True, False, True, True, True, True, False, False, False, False, False, False, True, True, True, True, False, False, True, False, False, False, False, False, True, True, False, False, True, True, True, False, False, True, False, False, False, True, False, True, False, True, False, False, True, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, True, False, False, True, True, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, False, True, False, False, False, True, True, True, False, True, True, True, True, False, True, False, True, False, True, True, True, False, True, True, False, False, True, True, True, True, True, True, False, False, False, True, False, True, True, False, False, False, False, True, False, False, False, True, False, True, False, False, True, True, True, False, True, False, False, False, True, True, True, False, False, False, False, True, True, False, False, True, False, False, True, False, True, True, True, False, False, True, False, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, False, True, True]
expected_confidence = (5, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 212')
test = [False, True, True, False, False, True, True, False, True, True, False, True, True, True, False, False, True, False, True, False, False, True, True, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, True, False, False, False, True, False, False, True, True, True, False, False, True, False, False, False, True, False, False, True, False, True, False, True, False, False, False, False, True, False, True, True, True, True, False, False, True, True, True, True, True, False, False, False, False, False, False, True, False, False, False, True, True, True, False, True, False, True, False, False, False, True, False, True, True, True, True, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True, False, True, True, True, True, True, False, True, True, False, False, True, False, True, False, False, False, True, False, False, False, True, False, False, True, True, True, True, False, False, False, True, False, False, True, True, True, True, False, True, True, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, False, False, False, True, False, True, True, False, False, False, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 213')
test = [False, True, False, True, False, True, False, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, True, True, True, False, True, True, False, True, False, True, False, False, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, True, True, True, False, True, False, False, True, False, True, False, True, False, False, True, False, True, False, True, False, True, True, True, False, False, False, False, False, True, True, False, False, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, True, True, True, False, False, True, False, True, False, False, True, True, False, False, False, False, True, True, True, False, True, True, True, False, True, True, True, False, False, False, True, False, True, False, False, False, False, True, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, False, False, True, False, False, True, True, False, False, True, False, True, True, False, False, True, True, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 214')
test = [False, True, True, False, False, False, False, False, True, True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, False, False, True, False, True, False, False, True, True, True, True, False, False, True, True, False, True, True, True, True, True, False, True, True, False, False, True, False, False, True, False, True, True, False, True, True, True, False, False, False, True, True, False, False, True, False, False, False, False, True, False, False, True, False, False, False, True, False, True, True, False, True, False, True, False, False, False, True, True, True, False, False, True, True, False, True, False, True, False, False, False, True, False, True, True, False, False, True, True, False, True, True, True, True, False, False, False, True, False, False, True, False, True, False, True, True, False, False, False, True, False, False, True, False, True, False, False, False, True, True, True, False, False, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, False, True, True, True, False, False, False, True, False, False, True, True, True, True, False, True, True, True, False, False, True, False, True, False, False, True, True]
expected_confidence = (3602879701896397, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 215')
test = [True, False, True, True, False, True, False, True, True, False, False, True, False, True, True, True, True, True, False, False, True, True, False, False, False, True, True, True, False, True, False, True, False, False, True, False, False, True, False, False, True, False, True, True, True, True, False, True, False, True, False, False, True, True, True, False, True, False, False, False, True, False, False, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, False, True, True, False, True, False, True, False, True, True, False, True, False, False, False, True, True, True, False, False, True, False, False, False, True, False, True, True, False, True, False, False, False, True, True, True, False, True, True, True, True, False, False, True, False, False, False, False, False, True, False, False, True, False, True, False, False, True, False, True, False, False, False, False, False, True, True, True, True, False, True, True, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False, False, False, True, True, False, False, False, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, True, True, True, True, False, False, False, True, False, True, True, False, True, True, False, False, True, False, True, True, False, False, False, False, True, False, True, False]
expected_confidence = (1, 2)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 216')
test = [False, True, True, False, True, False, True, False, True, True, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, True, True, True, False, True, False, True, True, True, True, False, True, False, True, False, True, True, False, False, True, True, False, True, False, True, False, True, False, True, False, False, True, True, False, True, False, True, True, True, False, True, True, False, False, False, False, False, True, True, True, True, False, True, True, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, True, True, True, False, True, True, False, False, True, False, True, True, False, True, False, False, True, False, False, True, True, False, False, True, False, True, False, False, False, True, False, True, False, True, True, True, True, True, False, False, False, False, True, False, True, True, False, False, True, False, False, True, True, True, True, False, False, True, True, False, True, False, False, True, False, True, True, False, False, False, False, False, False, True, True, True, True, False, False, True, True, True]
expected_confidence = (3, 4)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 217')
test = [False, False, False, True, True, True, True, False, True, True, True, True, True, False, True, True, True, False, False, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, False, False, False, True, False, True, False, False, False, False, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, True, False, True, True, False, False, True, False, True, True, False, True, True, True, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, True, False, True, False, True, True, False, False, False, True, True, False, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, False, False, True, False, True, False, False, True, True, True, True, False, True, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, True, False, True, True, True, False, True, False, True, True, False, True, True, True, False, False, True, False, False, True, True, True, False, False, True, False, False, True, True, False, True, True, True, False, True, True, True, False, False, False, True, True, True, True, False, True]
expected_confidence = (2501999792983609, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 218')
test = [False, True, True, False, False, False, False, True, False, False, True, False, True, True, True, False, True, False, False, True, True, True, True, False, True, True, False, False, True, True, True, False, True, True, False, True, False, True, False, True, False, False, True, True, True, True, False, True, False, False, False, False, True, True, True, True, False, False, False, False, False, True, False, False, True, False, True, False, True, False, True, False, False, True, True, False, False, False, True, True, True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, True, False, True, False, False, False, False, True, True, False, True, True, True, False, False, False, True, False, False, False, False, True, False, True, True, True, False, True, False, False, False, False, True, True, False, False, True, True, True, True, True, True, True, False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, True, False, True, True, True, True, False, False, False, False, True, False, False, True, True, True, False, True, False, False, False, True, False, True, False, False, True, True, True, False, True, False, True, False, True, False, False, True, False, False, True, False, False, False, False, False, True, True]
expected_confidence = (4157168886803535, 9007199254740992)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 219')
test = [False, False, True, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, True, True, True, True, True, True, False, False, False, True, False, True, True, False, True, False, False, False, True, False, False, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, False, True, False, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, False, False, False, True, True, False, True, False, False, True, False, True, False, False, False, False, False, True, False, False, False, False, True, True, True, True, True, True, False, True, False, False, True, False, False, False, True, False, True, True, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, True, True, False, False, True, False, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, True, True, True, False, False, True, True, True, True, True, True, False, False, True, True, True, True, True, False, False, True, False, False, False, True, False, False, True, False, True, False, False, False, True, True, True, True, True, False]
expected_confidence = (2001599834386887, 4503599627370496)
expected_similar_patterns = 11
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 220')
test = [True, False, True, False, False, False, True, False, False, True, False, False, False, False, True, False, False, True, False, True, False, False, True, False, True, True, True, False, True, True, False, True, False, False, False, False, True, False, True, False, True, False, True, True, True, False, False, True, False, True, False, False, False, True, False, False, False, True, True, False, True, False, False, True, True, True, False, False, True, True, True, False, True, False, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True, True, True, True, False, False, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, True, True, False, False, False, False, False, True, True, True, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, True, False, False, True, False, True, True, False, True, False, True, True, False, True, False, True, True, False, False, True, False, True, True, False, False, False, True, True, True, True, True, False, False, True, False, False, True, True, True, True, False, True, True, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 221')
test = [True, False, False, True, False, True, True, False, True, False, False, True, False, False, True, False, True, True, True, False, True, False, False, True, False, False, False, True, True, False, True, True, True, True, True, True, True, False, True, False, False, False, True, True, False, True, True, True, True, True, False, False, False, False, True, True, False, False, True, True, False, True, True, False, False, True, True, False, False, False, False, True, True, True, False, True, False, False, False, False, True, True, True, False, False, True, True, True, True, False, True, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, True, True, True, True, False, True, False, True, True, True, True, True, False, False, True, False, False, True, False, True, True, True, False, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, True, False, True, False, False, True, True, False, False, True, False, True, False, False, True, True, True, False, True, True, True, False, False, True, False, True, False, False, True, False, False, False, False, True, False, False, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, False, True, True, False, True, True, False, False, False, True, False, True, False, False, False, False, False, True]
expected_confidence = (1, 4)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 222')
test = [False, False, False, True, False, False, False, True, True, False, False, False, True, False, False, True, True, True, True, False, False, False, True, False, True, True, True, True, True, False, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, False, False, False, False, True, True, False, True, False, False, False, True, True, True, False, False, True, True, True, False, True, False, False, True, True, False, False, False, True, True, False, True, True, False, True, True, False, False, False, False, False, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True, False, False, True, True, True, False, False, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, True, False, False, False, False, True, True, False, True, False, False, False, True, True, False, True, True, True, False, False, True, False, True, False, False, True, False, False, False, True, True, True, True, False, True, True, True, False, False, False, True, True, False, True, False, False, True, False, True, False, True, True, True, False, False, False, True, True, False, False, True, False, True, True, False, True, True, True, False, True, True, True, True, False, True, False, False, True, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False]
expected_confidence = (3117876665102651, 4503599627370496)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 223')
test = [False, False, True, True, False, False, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, False, False, True, False, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, True, True, False, False, True, False, False, True, True, True, False, True, False, False, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, True, True, False, True, False, False, False, False, True, False, True, False, True, True, True, True, False, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, False, True, False, True, False, True, False, True, False, False, True, False, True, True, False, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, True, True, False, True, True, True, True, True, False, False, True, True, False, True, True, False, False, True, True, True, False, True, False, False, False, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, True, True, True, True, True, True, False, False, True, True, False, False, False, False, True, False, False, True, False, True, False, True, True, False, False, True]
expected_confidence = (7505999378950827, 18014398509481984)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 224')
test = [True, True, True, True, True, False, False, True, True, False, False, False, True, True, True, True, False, False, True, True, False, True, True, False, True, False, False, True, False, False, False, True, False, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, False, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, False, True, False, False, False, True, False, True, True, False, True, True, True, False, False, True, False, True, True, True, True, True, True, False, False, False, True, False, True, False, False, True, False, True, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, False, False, True, False, False, True, True, True, True, False, True, False, False, True, True, True, False, False, True, False, False, True, True, False, True, True, False, True, False, True, False, False, True, False, False, False, True, False, False, True, True, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, False, False, False, True, False, True, True, True, True, True, False, False, True, True, True, True, True, True, False, True, True, True, False, True, False, False, False, False, True, True, True, False, False, False, True, False, False, True, False, True, False, True, False, True, True]
expected_confidence = (0, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 225')
test = [True, True, False, True, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, True, True, True, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, False, False, True, False, True, False, False, True, True, False, False, True, True, False, True, False, False, True, True, False, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, False, False, True, False, True, False, False, False, True, True, True, True, True, False, False, True, True, False, True, True, False, True, False, False, True, False, True, False, True, False, False, False, False, False, True, True, True, True, True, True, True, False, True, True, False, True, True, True, False, False, True, False, True, False, False, True, False, False, True, True, False, True, True, True, False, False, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, False, True]
expected_confidence = (3602879701896397, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 226')
test = [True, True, True, True, True, True, False, True, False, False, True, False, True, True, False, True, False, True, False, False, True, False, False, False, False, True, False, True, True, False, False, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, True, False, True, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, True, True, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, False, False, True, True, True, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, False, False, True, False, False, True, True, False, True, False, True, True, True, False, True, False, False, True, False, False, False, False, True, False, True, True, False, False, False, True, False, False, False, False, True, False, True, False, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, True, False, True, False, True, True, True, False, True, False, True, False, False, True, False, True, False, True, True, False, False, True, True, True, True, False, True, False, True, True, True, True, False, False, True, False, True, False, True, True, False, False, False, False, False, False, False, True, False, True, False, True, True, False, False, True, False, False, True, False, True, True, True]
expected_confidence = (5254199565265579, 9007199254740992)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 227')
test = [True, True, True, True, False, True, False, True, False, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, True, True, True, False, False, True, True, False, False, False, True, False, True, True, False, False, False, False, True, False, True, False, True, False, True, True, True, True, False, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, True, False, True, True, False, False, False, True, True, True, False, False, False, False, False, True, True, True, True, False, True, False, True, True, True, True, False, True, True, False, True, True, True, False, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, True, False, True, True, True, False, False, False, True, True, True, True, True, True, False, True, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, True, True, True, True, True, True, False, False, False, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, False, True, False, False, False, True, False, False, True, False, False, True, True, True, False, True, True, True, False, True, False, False, True, False, False, False, True, True, True, True, False, True, True, False, False, False, False, False, False, False, True, False, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 228')
test = [False, True, True, False, False, False, True, True, True, True, False, False, True, False, True, False, False, False, False, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, True, True, False, True, False, False, False, False, True, False, False, False, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, True, True, True, True, True, True, False, True, True, True, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, True, False, False, True, False, True, False, True, True, False, True, True, False, False, False, True, True, False, True, False, False, True, True, False, False, True, False, False, True, True, True, True, True, True, True, False, False, False, False, False, True, False, False, False, True, True, True, False, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, True, False, True, True, True, False, False, True, False, True, True, True, False, False, False, False, True, False, True]
expected_confidence = (6928614811339225, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 229')
test = [False, True, False, True, True, True, False, True, True, True, False, False, True, False, False, True, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, True, False, False, True, True, True, True, False, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, False, True, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, False, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, True, False, False, True, True, True, True, True, False, True, True, True, False, True, False, False, False, True, True, True, False, False, False, True, True, True, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, True, True, False, True, True, True, True, True, True, False, False, False, True, False, False, True, True, False, False, False, False, True, True, True, False, True, False, True, True, False, True, True, False, False, False, False, True, True, False, False, True, True, False, True, True, False, True, True, True, False, True, False, True, False, False, True, True, False, True, False, True, False, False, True, False, False, True, False, False, False, False, True, False, True, False, True, False, False, True, False, True, False, True, True, True, True, True, False, False, True, True, False, False, False, False, False, False]
expected_confidence = (0, 1)
expected_similar_patterns = 0
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 230')
test = [True, True, True, False, True, False, True, False, True, True, False, True, True, False, True, False, True, True, False, False, False, False, False, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, True, False, True, False, True, True, True, True, False, True, True, False, False, True, True, True, False, True, False, False, False, True, True, False, False, True, True, True, False, True, False, False, False, True, True, True, False, False, True, False, True, True, False, True, True, True, True, False, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, False, True, False, True, True, False, True, False, True, True, False, False, True, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False, False, True, True, False, True, True, True, True, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, True, True, True, False, True, False, True, False, True, True, True, False, True]
expected_confidence = (1, 2)
expected_similar_patterns = 4
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 231')
test = [True, True, False, True, True, False, True, True, False, False, False, False, True, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, True, False, True, True, False, True, True, True, True, False, False, True, True, False, False, False, True, True, False, False, False, False, False, True, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, True, True, False, False, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, False, True, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, False, False, False, True, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, True, False, False, True, True, False, True, False, True, True, False, True, True, True, True, False, False, False, True, False, True, True, False, True, True, False, False, False, True, False, False, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, True, False, True, False, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True]
expected_confidence = (3275345183542179, 4503599627370496)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 232')
test = [False, True, False, True, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, False, True, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, False, False, False, False, True, True, True, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, True, False, False, False, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, False, True, False, False, True, True, True, True, False, True, False, True, True, False, True, True, True, False, True, False, False, True, False, True, False, False, False, True, True, True, True, False, True, True, True, False, True, False, False, False, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, False, False, True, True, True, False, True, False, True, True, True, False, True, False, False, True, True, True, False, False, False, False, True, True, True, False, False, False, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, True, False, True, False, True, True, True, False, True, True, True]
expected_confidence = (5731854071198813, 9007199254740992)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 233')
test = [True, False, False, False, True, True, False, True, True, True, True, True, False, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, False, False, False, True, False, False, True, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False, False, True, True, True, False, True, True, True, False, False, True, False, True, False, True, False, False, True, True, False, False, False, True, False, True, True, False, True, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, False, False, True, False, True, True, False, False, True, False, False, False, True, False, True, True, False, False, True, True, False, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, True, False, True, True, True, True, False, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, False, True, False, False, True, True, True, True, True, True, True, True, False, False, True, False, False, False, True, False, True, False, False, True, False, True, False, False, True, True, False, False, False, True, False, True, True, False, False, False, True, False, False, False, True]
expected_confidence = (5828187753067701, 9007199254740992)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 234')
test = [False, False, True, False, True, True, False, False, True, True, True, True, True, False, True, False, True, True, True, True, True, False, False, False, True, True, True, True, True, False, False, True, True, False, False, False, False, True, False, False, True, False, True, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, False, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, True, True, False, False, False, False, True, True, True, True, False, False, False, True, True, False, False, False, True, False, False, True, True, True, True, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False, True, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, False, False, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True, True, False, True, False, False, True, False, True, False, False, False, True, True, False, True, False, True, False, False, False, False, False, True, False, False]
expected_confidence = (6004799503160661, 9007199254740992)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 235')
test = [False, True, True, True, False, False, True, True, True, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, True, False, False, False, True, False, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, False, False, True, True, True, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, True, False, False, True, False, True, True, False, False, True, False, True, True, True, False, False, True, True, True, False, True, False, True, True, True, False, False, True, False, True, False, True, False, True, False, False, True, False, False, True, True, False, True, False, True, True, False, True, True, True, False, False, False, False, False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, False, False, True, True, True, False, True, False, False, True, True, False, True, True, False, False, True, True, False, True, True, False, False, True, False, False, False, False, False, True, True, True, False, True, True, False, False, True, True, False, False, False, True, False, True, False, False, False, False, True, True, True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, True, False, False, False, True, True, False, True, False, False, True, True, False, False, False, True, False, False, True, True, True]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 236')
test = [True, False, True, False, True, True, True, False, False, False, True, False, False, True, True, False, True, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, False, False, True, True, True, False, False, False, False, False, True, False, True, True, False, True, True, True, False, True, False, False, False, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, False, True, True, True, False, False, True, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, False, True, False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, True, False, True, True, True, False, True, False, True, True, True, False, True, True, False, True, False, False, False, False, True, True, False, False, True, False, False, False, True, True, False, False, True, False, True, True, False, True, False, True, True, True, True, False, False, True, False, False, True, False, False, True, True, True, False, False, False, False, False, True, True, False, False, True, True, False, False, False, True, True, True, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, False, True, False, True, False, True, True, True, False]
expected_confidence = (7505999378950827, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 237')
test = [True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, True, False, False, False, False, False, True, False, True, True, False, True, False, True, True, False, False, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, True, False, False, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, False, False, False, True, True, False, True, False, False, True, True, False, False, True, True, False, False, False, True, True, False, True, True, True, True, True, True, False, False, False, True, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, True, True, False, True, False, False, False, False, False, True, False, True, True, True, True, False, False, True, True, False, True, False, False, False, False, False, True, False, True, True, False, True, True, False, True, True, False, False, False, True, True, True, True, False, True, False, True, True, True, False, False, False, False, False, True, True, True, True, False, True, True, True, True, True, True, False, False, False, False, True, False, False, True, True, True, False, False, False, False, True, True, True, False, False, True, True, False, False, True, False, False, True, False, True, True, False, True, False, True, True, True, False, True, True, True, False, False, False, True, True, True, False, True]
expected_confidence = (3, 8)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 238')
test = [True, False, True, False, False, True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, True, False, True, True, False, True, False, True, False, True, True, True, False, False, True, False, True, False, True, False, True, True, True, True, True, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, False, False, True, False, True, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, False, True, True, False, False, False, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, True, False, True, False, False, False, True, False, False, True, False, True, True, True, False, True, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, True, True, False, False, False, True, False, True, False, False, True, True, False, False, True, False, True, False, False, False, True, True, True, True, False, True, False, True, True, True, True, True, False, False, False, False]
expected_confidence = (3275345183542179, 36028797018963968)
expected_similar_patterns = 7
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 239')
test = [False, False, True, True, True, True, True, False, True, False, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, True, True, True, False, True, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, False, True, False, True, True, True, False, False, True, False, False, True, True, False, False, False, True, False, True, True, True, False, False, False, True, True, True, False, False, True, True, False, True, False, True, True, True, False, False, True, True, False, False, True, False, False, True, True, True, True, True, True, False, False, True, False, True, False, True, True, False, False, True, False, True, True, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, False, True, False, False, True, True, False, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, False, False, False, True, True, False, False, False, True, False, False, True, False, False, True, False, True, False, False, False, True, True, False, True, False, True, True, False, False, True, True, True, False, True, True, False, True, True, True, False, False, False, True, True, True, True, False, False]
expected_confidence = (2501999792983609, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 240')
test = [False, True, True, True, True, False, False, False, False, False, False, True, True, True, False, False, False, False, True, False, False, True, False, False, True, False, False, True, True, False, True, True, True, False, False, True, True, False, False, True, True, True, True, False, True, False, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, False, True, True, False, True, False, True, True, False, False, False, True, False, False, True, True, False, False, False, False, True, False, True, True, True, False, False, False, True, True, False, True, True, True, False, False, False, False, False, True, True, False, False, False, False, True, False, True, True, False, True, False, False, False, True, True, False, False, False, False, True, True, False, True, False, False, False, True, True, True, False, True, True, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, True, True, False, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, True, False, False, False, False, False, True, True, False, True, True, True, False, True, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, True, False, True, False, True, False, True, False, True, True, True, True, True, True, False, False, True, False, True, False, False, False, True, True]
expected_confidence = (1, 2)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 241')
test = [True, True, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, False, True, False, True, False, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, False, True, False, False, False, True, False, True, False, False, True, False, True, True, False, False, False, False, False, True, True, False, False, True, True, False, False, True, False, True, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, True, True, True, False, True, False, False, False, False, True, False, True, True, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, True, True, False, False, True, True, True, False, True, False, False, True, False, False, False, True, True, True, True, True, True, True, True, False, True, True, False, True, False, True, False, False, False, True, True, True, False, False, True, True, True, True, True, False, False, False, False, True, False, False, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, True, True, True, True, True, True, False, True, False, True, True, True, True, True, True, False, False, True, True, True, True, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, False, False, False, False, False, False, True, False, False, False, True, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 242')
test = [False, True, False, True, True, False, True, True, False, False, True, False, True, False, False, True, True, True, False, True, False, True, True, False, True, True, False, True, True, True, False, True, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, True, True, False, False, True, False, False, False, True, False, True, True, True, False, False, False, False, True, True, True, True, False, False, False, False, False, True, True, False, True, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, False, True, False, False, True, True, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, True, True, False, True, True, False, True, False, True, True, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, True, False, True, False, False, True, True, False, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True, False, False, False, False, True, False, True, True, True, False, False, True, False, False, False, True, True, True, True, False, True, False, False, True, False, True, True, True, True, False, False, True, False, True, False, False, True, False, False, True, False, False, True, True, True, True, True, True, True, True]
expected_confidence = (1, 2)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 243')
test = [False, True, False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, False, True, True, False, False, True, True, True, False, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, False, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, False, True, False, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, False, False, False, True, False, True, False, True, False, False, False, True, True, True, True, True, True, False, False, True, True, False, True, False, True, False, False, False, False, True, False, True, True, False, True, False, True, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, True, True, True, False, False, True, False, False, True, False, False, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, True, False, True, False, False, False, False, True, True, False, True, True, True, False, False, True, False, False, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, True, True, True, True, True, True, False, False, True, False, False, True, True, False, False, False, True, False, False, True]
expected_confidence = (6928614811339225, 18014398509481984)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 244')
test = [False, False, True, False, False, True, True, True, False, True, False, False, False, False, False, False, True, False, True, True, False, True, True, True, True, False, True, True, True, False, True, True, True, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, False, True, False, True, True, False, True, True, True, True, False, True, True, True, True, False, False, True, True, True, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, False, True, False, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False, True, True, False, False, False, False, True, False, False, True, True, False, True, False, True, False, False, False, False, False, True, True, True, False, False, False, False, False, False, True, True, True, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, True, True, False, False, True, False, False, True, False, False, True, True, False, False, True, True, True, True, False, False, False, False, False, True, False, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, False, True, False, False, False, False, False, True, False, False, True, False, True, False, True, True, False, True, False, False, True, True]
expected_confidence = (2001599834386887, 9007199254740992)
expected_similar_patterns = 5
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 245')
test = [False, False, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True, False, False, True, False, True, True, False, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, True, False, False, False, True, False, False, True, False, False, False, True, True, True, True, False, True, False, False, True, True, False, True, True, False, True, True, False, True, False, False, False, False, False, True, False, True, False, True, False, True, False, True, False, True, True, True, False, True, False, False, False, False, False, True, False, True, True, True, True, False, False, True, False, True, True, False, True, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False, True, False, True, True, True, True, False, True, False, True, True, True, True, True, False, False, True, False, False, True, True, True, True, False, False, False, True, True, True, True, False, False, False, False, False, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, False, False, True, True, False, False, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, False, True, True, False, True, False, False, True, False, True, False, True, True, True, False, False, False, False, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 9
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 246')
test = [True, True, False, False, True, True, False, True, True, True, False, False, True, False, False, True, False, True, True, True, True, True, True, True, False, False, True, False, False, True, False, True, True, True, False, False, False, True, False, False, False, True, False, False, False, True, True, False, False, False, True, True, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, True, True, True, True, False, True, True, False, False, True, False, True, False, True, True, True, False, True, False, False, True, True, True, True, True, False, True, True, True, False, True, False, False, True, False, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, True, False, True, True, True, True, False, False, False, True, False, True, False, False, False, False, True, False, True, True, False, True, False, False, True, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, True, False, True, False, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, True, False, True, False, False, False, True, False, True, True, True, True, True, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, True, True]
expected_confidence = (4768517252509937, 9007199254740992)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 247')
test = [False, False, False, True, False, False, False, False, True, False, True, False, False, False, True, True, False, True, True, False, False, True, False, True, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, False, False, False, True, True, True, False, True, False, False, True, True, True, False, False, True, True, True, True, True, True, False, False, True, False, False, True, True, False, False, True, False, False, True, True, False, False, True, True, False, True, False, False, True, True, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, False, False, False, False, True, True, True, True, True, False, False, True, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, True, True, False, False, False, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, False, False, True, False, True, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, True, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, False, False, True, False, False, True, False, False, False, False, False, True, True, True, True, False, False, True, True, False, False, False, True, False, False, True, False, True, False, True]
expected_confidence = (1, 1)
expected_similar_patterns = 2
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 248')
test = [True, False, False, False, True, False, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False, True, True, False, True, False, False, False, True, True, True, True, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False, False, True, False, True, False, False, True, True, True, False, False, True, True, True, False, True, False, False, True, False, True, False, True, True, True, True, True, False, False, False, True, True, True, False, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False, False, True, False, True, False, True, False, True, True, True, False, True, False, True, True, False, True, True, True, False, True, False, False, True, True, False, True, False, True, False, True, True, False, True, False, False, True, True, False, True, False, True, False, True, False, True, False, False, False, True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, False, True, False, False, False, True, False, True, True, False, True, False, True, False, True, True, False, True, True, True, True, True, True, False, True, True, False, False, True, False, True, True, False, True, True, True, False, True, True, True, False, False, True, True, True, True, True, False, False, False, True, False, True, True, True, False, False, False, True, False, False, True, False, False, True, True, True, True]
expected_confidence = (2001599834386887, 4503599627370496)
expected_similar_patterns = 6
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 249')
test = [False, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, False, True, False, True, True, True, False, True, False, True, False, False, False, False, True, False, True, False, False, False, False, True, True, True, False, False, True, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, False, False, False, False, False, False, True, False, True, True, True, True, False, False, False, False, False, False, True, True, False, True, False, False, False, False, True, False, True, True, True, True, True, True, True, False, False, True, False, False, False, True, True, False, True, True, True, False, False, True, True, True, False, False, True, True, True, False, True, True, True, True, False, True, False, False, True, False, False, True, False, False, False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, False, False, True, False, True, True, False, False, True, False, True, False, True, True, False, True, False, True, True, False, False, True, True, True, True, True, True, True, True, True, False, True, True, True, False, False, False, False, True, True, False, True, True, False, False, False, False, True, True, True, False, True, False, True, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True, False, True, True, True, True, False, True, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 250')
test = [True, True, False, False, False, False, True, True, True, False, False, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, True, True, True, False, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, False, True, True, False, False, False, False, True, False, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, True, False, False, True, True, False, True, True, False, False, True, True, False, True, True, True, True, False, False, False, True, False, False, True, False, True, True, True, False, False, False, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True, True, False, True, True, True, False, False, True, False, False, False, False, True, True, False, True, False, True, True, False, True, True, True, False, True, True, True, False, False, True, False, True, False, False, False, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, False, False]
expected_confidence = (3602879701896397, 4503599627370496)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 251')
test = [False, False, False, False, True, True, False, True, True, False, False, True, True, False, True, True, False, False, True, True, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, True, True, False, False, False, True, True, True, True, True, True, False, False, False, True, True, True, False, True, False, True, False, True, False, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, False, False, True, False, True, False, False, False, False, True, True, True, True, True, False, True, False, True, False, False, False, False, True, True, False, True, True, False, True, False, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, True, False, False, True, True, False, False, False, True, True, True, False, False, False, False, False, True, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, True, True, False, True, True, False, False, False, False, True, False, True, False, False, True, True, False, True, False, True, True, False, False, True, True, False, False, False, True, True, False, True, False, True, True, False, False, True, True, False, True, True, True, True, False, True, True, True]
expected_confidence = (1, 4)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 252')
test = [True, True, True, False, False, True, False, False, True, False, True, False, True, True, False, False, False, False, False, False, False, True, False, False, True, True, True, True, False, True, True, True, False, False, False, True, True, True, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, True, False, False, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, False, True, True, False, False, True, False, False, True, False, False, True, True, False, True, True, False, True, False, False, False, True, True, False, True, True, True, False, True, False, False, False, False, False, False, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, False, False, True, True, True, True, False, True, True, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, False, True, False, False, False, False, False, True, False, False, True, False, False, False, True, True, True, True, False, False, False, True, False, False, True, True, False, True, True, True, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, False, False, False, True, True, False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, True, False, False, False, False, False, True, True, False, True, False, True, True, False, False, False, True, False, False, True, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, True, False, True]
expected_confidence = (6004799503160661, 18014398509481984)
expected_similar_patterns = 11
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 253')
test = [False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, False, False, True, False, True, False, False, True, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, True, False, False, False, True, True, True, False, True, False, False, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True, False, False, True, False, False, True, False, True, True, False, False, False, True, False, False, False, False, True, False, True, True, False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, True, False, True, True, False, False, True, True, False, True, False, False, False, True, False, False, False, True, True, True, False, False, False, True, False, True, False, False, False, False, True, False, True, True, False, False, True, False, True, True, True, False, False, False, True, True, False, True, False, False, True, False, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, True, False, False, False, False, True, False, True, True, False, False, True, True, False, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, False, True, False, True, False, False, True, False, True, True, False, False, True, False]
expected_confidence = (3602879701896397, 18014398509481984)
expected_similar_patterns = 3
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 254')
test = [False, True, True, True, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, False, False, True, True, True, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, False, False, True, False, True, False, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, True, True, False, True, True, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, True, True, False, False, False, False, False, True, True, True, True, True, False, False, True, True, False, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, True, False, True, True, True, False, False, False, False, False, True, False, False, True, False, True, True, False, True, False, True, False, False, True, False, False, True, False, False, True, False, True, True, True, False, False, False, False, True, True, True, False, True, True, False, False, True, False, False, True, False, False]
expected_confidence = (3, 16)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 255')
test = [True, False, True, True, True, False, False, False, False, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, False, True, False, True, False, False, False, True, True, False, False, False, False, False, True, True, True, True, True, True, False, True, False, True, True, True, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, False, True, True, False, True, False, True, True, True, True, False, True, False, True, False, True, False, False, True, True, False, False, True, True, True, False, False, False, True, False, True, False, False, False, True, False, True, False, True, False, True, False, False, True, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False, True, True, True, False, False, False, True, True, True, False, True, True, False, False, False, False, False, False, False, True, False, False, True, False, True, True, False, True, False, False, False, False, False, False, True, False, False, True, True, True, False, True, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, True, False, False, False, False, False, False, True, True, True, True, False, True, False, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, True, False, True, False, False, True, True, False, True, False, False, False, True, True, False, False, False, False, False, False, True, False, True, False, True, False, False]
expected_confidence = (1385722962267845, 4503599627370496)
expected_similar_patterns = 8
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]

print('test 256')
test = [False, True, False, False, True, True, False, True, False, True, False, True, True, False, True, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, False, True, False, True, False, False, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, False, True, True, True, False, True, True, True, True, True, False, False, True, False, True, True, True, True, False, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True, True, False, True, False, True, True, False, False, True, False, True, True, False, False, True, True, True, True, True, False, True, False, True, True, True, False, True, True, True, True, False, True, False, True, True, False, False, True, True, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, False, False, False, False, False, True, False, True, True, True, False, False, True, False, False, True, False, False, True, True, True, True, False, True, True, False, True, True, True, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, False, True, True, True, True, True, False, False, True, False, True, True, False, False, True, True, False, False, False, False, True, False, True, False, True, False, True, True, False, False, True, True, False, False, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, False, True, True]
expected_confidence = (5828187753067701, 9007199254740992)
expected_similar_patterns = 10
prediction = BinaryTangent(test).calculate_next()
assert prediction['confidence_score'].as_integer_ratio() == expected_confidence, [prediction['confidence_score'], expected_confidence]
assert prediction['similar_patterns'] == expected_similar_patterns, [prediction['similar_patterns'], expected_similar_patterns]
