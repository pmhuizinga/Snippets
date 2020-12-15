import pandas as pd

df = pd.DataFrame({'colA': [1, 2, 3], 'colB': [4, 5, 6]})

def test_B(func):
    def wrapper(*args):
        print('before {}'.format(df.shape[0]))
        df['test'] = 0
        out = func(*args)
        print('after {}'.format(out.shape[0]))
        return out
    return wrapper

@test_B
def test_A(df, testval):
    print(df.shape[0])
    print(testval)
    return df

test_A(df,'testv')
