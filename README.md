# Sentiment-analysis

## 1. DataSet 

NSMC의 ratings_train.txt ratings_test.txt (https://github.com/e9t/nsmc)

### Dataset 구조
ex)

6825595	지루하지는 않은데 완전 막장임... 돈주고 보기에는....	0

6723715	3D만 아니었어도 별 다섯 개 줬을텐데.. 왜 3D로 나와서 제 심기를 불편하게 하죠??	0

7898805	음악이 주가 된, 최고의 음악영화	1

긍정 => 1 , 부정 => 0

## 2. Data Preprocessing

### Okt를 이용하여 형태소와 품사 분석

from konlpy.tag import Okt 
okt = Okt()

okt.pos(doc, norm=True, stem=True)

=> input : 아버지가방에들어가신다
   output : ['아버지/Noun', '가방/Noun', '에/Josa', '들어가다/Verb']
   
### nltk를 이용한 전처리

import nltk
text = nltk.Text(tokens, name='NMSC')

### Data vectorization

used CountVectorizer
=> 단어들의 카운트로 여러문서를 벡터화

## 3. Data Modeling

### Layer

Dense, unit=64, 활성화함수=relu
Dense, unit=64, 활성화함수=relu
Dense, 활성화함수 = sigmoid

### Compile

손실함수=binary_crossentropy , RMSprop optimizer를 통한 경사하강법

### fit

epochs=10, batch_size=512

### result

loss = 0.41581645607948303
binary_accuracyv = 0.8514800071716309

## 4. Test

진짜 영화 왜 이모양이냐 ==> 부정 (98%)
한 번보는걸로 만족이 안됨 ==> 긍정 (71%)
