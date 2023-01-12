# Toy_Project3



## 1. 프로젝트 구조

```
src/
 ┗━ app/
     ┣━ batch/
     ┃   ┃ ┗━ celery/
     ┃   ┃      ┗━ tasks/  (수행 함수 모음)
     ┃   ┃           ┗━ calculator.py
     ┃   ┗━ cli/ (개별 cli 관리)
     ┃        ┗━ calculator.py
     ┃
     ┣━ cli.py (Nesting Commands tutorial)
     ┣━ group.py (Command and Group)
     ┣━ hello.py (Quick Start)
     ┗━ main.py (main.py에서 cli 통합관리 )
 
README
```

cli.py
```
실행
python cli.py initdb
python cli.py dropdb
```

group.py
```
실행
python group.py greet
```

hello.py
```
python hello.py name
or
ex)
python hello.py name --count 3
```


