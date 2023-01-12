def add(a, b):
    print(f'{a + b} imported from {__name__}')
    
## 모든 add 함수를 다 불러옴
# add(4,6)

'''
- if __name__ == '__main__':  사용 이유

import 했을 때, 그 모듈 안에 모든 코드들이 그대로 실행되는 것을 막기 위해 사용한다.
'''
# if __name__=='__main__':
#     add(4, 6)