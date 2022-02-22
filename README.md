# DataMining_project

뉴스 기사 분석 프로젝트를 위한 data mining 과정

## 필요성

* 딱! 필요한 정보(통계정보, 인터뷰 자료 등)을 찾는데 걸리는 시간이 너무 김
  * 부정, 긍정적인 요소가 추가되었으면 하는 바람
    ex) 메타버스에 대한 부정적 의견이 있는 기사
* 검색 페이지를 15개를 넘겨도 원하는 정보가 없는 경우를 방지
* 중복 기사, 광고성 기사 제거

## 구성
### 뉴스 기사
1. 키워드 입력
  > 서강대학교, 진학률, 취업률, 취업 유지율
  > 
  > 대기업, 코딩테스트, 경쟁률

2. 정확도 설정(사용자 지정)
  * 만약 딥러닝(RNN류)를 사용한다면 더욱 의미가 있을듯

3. 추천 키워드(체크박스) or 긍정, 부정, 중립적 성격 체크

4. 기사 서칭 후 해당 내용 체크해서 제시

5. 만약 원하는 기사를 찾았다면 출처 제시 및 시각자료 제공

### 논문
1. 1~4 까지는 뉴스기사와 동일한 방법

2. 무료로 공개된 논문일 경우 다운로드 링크 제공
  * 아닌 경우는 초록에서 적합한 정보 제시

3. 사용한다면 출처 제시 및 시가자료 제공


## 추가 가능한 기능
* 각 언론사별 주관적 언어 사용 기준 비교(데스크 마다 다른 단어 사용)
  * 혹은 단어 사용의 규칙성, 자주 사용하는 단어, 언어 비교
* 나라별 주요 트랜드 분석
* 분석한 자료의 시각화?

### re Module (정규식)

  [1. re 모듈 기초](https://github.com/Cho-Jh98/DataMining_project/blob/master/1.%20DataMining_reModule.md)

  [2. meta character 1](https://github.com/Cho-Jh98/DataMining_project/blob/master/2.%20Datamining_MetaCharacter(1).md)
  
  [3. meta character 2](https://github.com/Cho-Jh98/DataMining_project/blob/master/3.%20Datamining_MetaCharacter(2).md)
  
  4. 정규식으로 한문장씩 자르기
    거기에 키워드 포함한 문장을 곁들인.

### Crawling

### KoNPLy

