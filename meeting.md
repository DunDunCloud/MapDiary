# 회의록 19

## 기능 구체화 & API 선정



### 기본적으로 **여행 플래너**

: 자신이 희망하는 여행코스를 짤 수 있고, 다녀온 여행지를 기록할 수 잇는 앱



### 필요한 구체적인 기능 리스트

- 최단거리 계산
- 사진 저장 (comment 추가)
- 별점 기능
- 위치 저장 (사진 유무 확인 후 저장) ( 가고 싶은 곳/좋아하는 곳)
- 장소 검색
- 친구에게 공유하기(public, private)
- 지도 시각화
- 위치 검색 자동완성



### 타서비스 분석

- 아이폰 사진 앱

  - 기본적으로 장소마다 사진을 볼 수 있다.

  - 사진을 클릭시 위치를 `서울중구` 로 표시한다

    ⇒ 우리 서비스는 식당이름, 장소명(서울대공원)처럼 장소명을 구체적으로 보여줄수 있도록?합시다!

- 구글맵

  https://www.google.co.kr/maps

- Triple(트리플) https://triple-corp.com/

- 카카오맵 https://map.kakao.com/

  - 장소별 후기작성할땐 사진첨부가능
  - 개인 즐겨찾기는 텍스트만 가능

- seesaw (지도 기반 사진정리) https://m.blog.naver.com/PostView.nhn?blogId=kindrice&logNo=220417030868&proxyReferer=https:%2F%2Fwww.google.com%2F

- Zenly (지도기반)

  [2.1.6.](https://namu.wiki/w/Zenly?from=젠리#toc) 탐험률[[편집\]](https://namu.wiki/edit/Zenly?section=9)

  오른쪽 위의 왕관 모양 버튼을 누르면 확인할 수 있다. 방문했던 곳이 하얀색으로 표시되며, 시/군/구 단위로 몇 %를 방문했는지 볼 수 있다. 친구들간 랭킹도 만들어지며, 만약 자신이 그 지역의 탐험률 순위 1등이라면 그 지역의 지도 위에 왕관 모양이 생긴다.

  

### 지도 API 선정

- 구글지도 api

  위치 검색 자동완성 기능 가능

  주소를 한글-영어 번역으로 인해 부정확

  지도 검색, 위치 경로 검색 **유료**

- 카카오 지도 api

  위치 검색 자동완성 기능 불가능

  사용 가이드가 친절함

- 네이버 지도 api

  **유료**로 전환

⇒ 카카오 지도 api로 결정

https://apis.map.kakao.com/web/guide/



### 기술적으로 필요한 부분

- 구글지도 api 사용예제 한글- 유료라서 안된다...

  https://iftraveler.tistory.com/37?category=878123

- 위치 검색 자동완성 (Google Places Autocomplete API_지역 정보 자동 완성)

  https://www.apistore.co.kr/generalApi/generalApiView.do?general_service_seq=49

- 오버레이로 경로 시각화 (카카오 api)

  https://apis.map.kakao.com/android/guide/#overlay



# 회의록 22



## 기능 정의 & 사용자 시나리오



### 필요한 구체적인 기능 리스트

- 최단거리 계산
- 사진 저장 (comment 추가)
- 별점 기능
- 위치 저장 (사진 유무 확인 후 저장) ( 가고 싶은 곳/좋아하는 곳)
- 장소 검색
- 친구에게 공유하기(public, private)
- 지도 시각화

SPA 구성하는 방향으로....

1. 기능묶음
   - 메인페이지: 지도 시각화 + 장소 검색 (+친구의 장소도 함께 보기)
     - 웹에서 볼때 지도 확대/축소 버튼 넣기
   - 작성페이지 : 위치 저장 + 사진 저장 + 친구에게 공유 여부(Y/N) + 별점 기능
   - 최적의 코스 제공 (대중교통, 자차, 자전거? 등)
   - 친구 관리
     - 소셜 로그인의 친구 중 선택해서 추가 + 초대 기능
     - 상대방이 친구 승낙
     - 구글 로그인의 경우 (친구없을 수 있음) - 친구 아이디로 추가/검색
   - 로그인/로그아웃
     - 소셜 로그인 - 구글/카카오
   - 회원가입 (+주요기능 완성 시 추가)



※ 구글맵 api 가격표

https://cloud.google.com/maps-platform/pricing?hl=ko

### 지도, 경로, 장소 혼합사용 시 1000건당 $12~15불 예상

**⇒ 크게 걱정거리 아님**





# 회의록 23



## 개발환경 선정 & 서비스 기획



# 개발환경 선정

- 지도 API : 구글 맵 API

  https://cloud.google.com/maps-platform/pricing?hl=ko

  - 월 $200의 크레딧은 대부분의 사용자가 필요로 하는 기능을 이용하기에 충분합니다. 일일 할당량을 설정하면 예상치 못한 사용량 증가를 방지할 수도 있습니다.

- Framework

  - server side: Django REST framework (Python)
  - front side: Vue.js (javascript library)

- DB: DynamoDB (AWS)

- 배포: ElasticBeanstock (AWS 새 계정 생성 - 프로젝트 용)



# 회의록 28



## 역할분담 & WBS 작성



1. 기능묶음

   - 메인페이지: 지도 시각화 + 장소 검색 (+친구의 장소도 함께 보기)
     - 웹에서 볼때 지도 확대/축소 버튼 넣기
   - 작성페이지 : 위치 저장 + 사진 저장 + 친구에게 공유 여부(Y/N) + 별점 기능
   - 최적의 코스 제공 (대중교통, 자차, 자전거? 등)
   - 친구 관리
     - 소셜 로그인의 친구 중 선택해서 추가 + 초대 기능
     - 상대방이 친구 승낙
     - 구글 로그인의 경우 (친구없을 수 있음) - 친구 아이디로 추가/검색
   - 로그인/로그아웃
     - 소셜 로그인 - 구글/카카오
   - 회원가입 (+주요기능 완성 시 추가)

   

### 역할분담

- API 구성 (GOOGLE map API, authorization API) ⇒ 찬영, 방부들
- 람다 함수 + API gateway + SNS + 로그 관리 ⇒ 굘굘맨
- DB - MongoDB(NoSQL) , DynamoDB(과금 가능성 농후함!) ⇒ 훈남
- library - Vue.js(Node.js) ⇒ 방부들
- aws 프리티어 계정 생성 후 IAM 사용자 만들고 권한 부여(AWS 계정은 다중 사용자 환경) ⇒ 훈남
- WBS 작성 및 수정 ⇒ 팀원 전체

여찬진: AWS 계정 및 사용자 권한 관리, DB 구현

강륜화: 배포 및 단위 테스트

방진실: 경로 탐색, 소셜 로그인 구현

유찬영: 지도 시각화, 개발 환경 구축



### AWS 에서 지원하는 서버리스 아키텍처 서비스

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/199298d7-25f7-4364-b60a-a07eaaa8d26f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/199298d7-25f7-4364-b60a-a07eaaa8d26f/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc04a049-bc44-4583-86e0-ad4dd8e69835/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc04a049-bc44-4583-86e0-ad4dd8e69835/Untitled.png)

→ 첫 달에 한해 무료 체험 가능



### WBS 작성

⇒ Microsoft Project Manager solution 활용





# 회의록 29



### 장소에 정보 저장하는 방법

- 장소 저장 팝업창 내용

  - 게시글 작성

    - 게시글이 없을 경우: 게시글 작성 버튼
    - 게시글이 있을 경우: 게시글 리스트

  - 장소 상세 정보

    상세 주소, 장소명

  - 별점 ⇒ 좋아요로 단순화

  

### 친구 장소 공유

- 왼쪽 navbar에서 친구 리스트 중, 특정 친구 선택 ⇒ 지도에 친구가 좋아하는 장소와 내가 좋아하는 장소 마커로 보여주기 (**2명의 장소들만**)
- 친구 선택하면 친구 전용 페이지로 이동, 해당 친구의 장소만 보여주기
- 

## WBS 방향

- 대분류: 분석 설계 개발 배포 통합테스트
- 소분류: 기능별로
- 단위: front/back/단위테스트



# 회의록 30



## 프로젝트 주제

여행을 설계하고 기록하고 공유하는 지도 기반 여행 플랫폼

# **기획 의도**

대부분의 지도 서비스는 다녀온 곳에 대한 기록을 남길 수 있는 서비스를 제공하고 있다. 하지만 그것은 주로 '후기'의 개념일 뿐, 개인적인 감상이나 특별한 경험 기록과는 거리가 멀다. 여행을 사랑하는 우리 조원들은 이와 다르게 나만의 일기 같은 지도 서비스를 만들고자 한다. 또한, 우리의 웹사이트가 다른 여행가들과의 교류의 장이 되어 서로 도움을 얻어갔으면 한다.



**# 시장 분석**

- 아이폰 사진 App

  지도에서 특정 위치에서 촬영한 사진과 사진의 개수를 한 눈에 볼 수 있다.

  사진을 클릭 시 위치/장소를 '서울 중구'로 표시한다.

- 구글맵

  지도에서 특정 장소를 검색하면 장소의 대표 사진들과 평점, 리뷰 등 상세정보를 확인할 수 있다.

  사용자가 선택한 장소를 즐겨찾기 저장할 수 있다.

  특정 장소에 간단한 메모를 남길 수 있다.

- 카카오 맵

  장소별 후기를 작성할 때 사진 첨부가 가능하다.

  즐겨찾기에 추가한 장소에 메모를 남길 수 있다.

  출발지와 도착지, 경유지를 선택해 최적의 이동 방법을 제공한다.

- 네이버 지도

  특정 장소에 좋아요를 누를 수 있지만, 사용자가 좋아요를 표시한 장소들을 목록으로 조회할 수 없다.

  출발지, 도착지를 입력해 이동 방법을 제공한다.

**# 프로젝트 목표**

- 내가 좋아하는 장소를 기록하고 친구와 공유하자 (사진 + 글)
- 내가 가고 싶은 장소를 저장하고 최적 경로(최단시간)를 탐색하자

**# 프로젝트 활용 방안**

- 친구와 함께 여행 계획을 세울 수 있다.
- 특정 장소에 대한 정보를 기록할 수 있다.



## 기능

- 회원가입/로그인

  구글, 카카오, 페이스북 SNS 로그인으로 회원가입하고 서비스를 이용할 수 있다.

  카카오, 페이스북의 친구 목록으로 [친구와 장소 공유] 기능을 이용할 수 있다.

- 장소 검색

  장소 이름, 키워드 등으로 장소를 검색할 수 있다.

- 내가 좋아하는 장소 기록

  특정 장소에 글과 사진을 남기고 친구와 공유할 수 있다.

- 친구와 장소 공유

  친구와 내가 좋아하는 장소와 그에 대한 사진, 글을 공유할 수 있다.

  

### 역할 분담

여찬진: AWS 계정 및 사용자 권한 관리, DB 구현

강륜화: 배포 및 단위 테스트

방진실: 경로 탐색, 소셜 로그인 구현

유찬영: 지도 시각화, 개발 환경 구축



## 프로젝트 개발 환경

- 지도 API: Google Maps API

- 배포: AWS

- 통합 인증 서비스: Auth0 활용

  카카오, 구글, 페이스북 SNS 로그인 API

- DB: MongoDB

- 개발 언어: Python HTML5 CSS3 Vue.js




# 회의록 2

### 역할 분담

- 찬진: DB(MongoDB 구축)  → EC2 인스턴스에 MongoDB 구축
- 륜화: 구글 지도 마커 구현
- 진실: read.me 회의록 추가, 카카오오븐 ui 설계
- 찬영: 지도 띄우기




# 회의록 3

### 역할 분담
- 찬진: EC2 인스턴스에 MongoDB 재 구축(버지니아) 및 연동
- 륜화: 카카오오븐 ui 설계
- 진실: navbar 기능 구현, 카카오오븐 ui 설계
- 찬영: 지도 크기 조절, Auth0

### 완료된 항목
- ui 설계




# 회의록 4

### 역할 분담
- 찬진: DB 테이블 구성, 연동
- 륜화: 지도 마커 구현
- 진실: side-bar 기본 틀 생성
- 찬영: Auth0마무리, 로그인/로그아웃, 현재 위치 기반 지도표시

### 완료된 항목
- 로그인/로그아웃
- 회원 프로필 보여주기
- DB AWS와 연동




# 회의록 5

### 역할 분담
- 찬진: DB 테이블 구성,
- 륜화: 지도 마커 구현
- 진실: side-bar 기본 틀 생성
- 찬영: nav-bar 생성

### 이슈 사항
[이슈](https://github.com/DunDunCloud/MapYourDiary/issues/7)
- 로그인 후 세션 유지
- sidebar 아이콘 적용 실패
    - [사용하고자 했던 sidebar](https://vuejsexamples.com/a-vue-js-sidebar-menu-component/)
    - [bootstrap-vue](https://bootstrap-vue.org/docs) 의 navbar와 slider로 대체 [commit](https://github.com/DunDunCloud/MapYourDiary/commit/b768e7a8ed5bbabf3ddee8ee44233e90e91aa77f)
    - ```npm install vue bootstrap-vue bootstrap```
- slider와 navbar가 겹침.
- 마커 구현
    - 현재 에러와 진행상황을 확인하기 어려움.
- serverless 구조 이해 필요



# 회의록 6

### 역할 분담
- 찬진: Vue 공부, Navbar 마무리
- 륜화: 지도의 현재위치 마커 생성과 이동
- 진실: 지도 스타일 변경, 마커 생성
- 찬영: sidebar 높이 조절

### 완료된 항목
- 지도 스타일 변경
- 지도의 현재 위치 마커 생성과 이동

### 이슈 사항
- 지도 크기를 브라우저 크기에 따라 조절 필요
- 지도에서 클릭한 지점에 마커 생성
- vue 이해와 디자인
- Django를 활용한 serverless 개발

### 회의 결과
- serverless framework와 Django를 연결하여 사용해야 한다.
![구조](./img/시스템구조.png)



<<<<<<< HEAD
- # 회의록 9

  ### 역할 분담

  - 찬진: serverless Framework, DB연동(MongoDB - Vue)
=======
# 회의록 9

### 역할 분담
>>>>>>> 44dc0c9b48a81b4eeb5e4d575ab02f9a8a990b61

- 찬진: Vue 공부, Navbar 마무리

- 륜화: 마커 생성/삭제

- 찬영: 정적 모달 구현

    
### 완료된 항목

- 정적 모달 구현

    
### 이슈 사항

  - 지도 크기를 브라우저 크기에 따라 조절 필요
  - vue 이해와 디자인
  - Django를 활용한 serverless 개발 -> serverless framework 활용
  - 장소 검색/조회를 위한 장소 API 적용




# 회의록 10



## 역할 분담

- 찬진: serverless Framework 설치 & lambda 함수 생성, DB연동(MongoDB - Vue)
- 륜화:
- 진실: 장소 & 친구 목록 front-end, 좋아요 기능
- 찬영:



### 오늘 완료한 일정

- 로컬 DB 연동
- 장소 & 친구 목록 front-end



### 참고 자료

- 친구 & 장소 목록에 사용한 vuetify 소스

    [https://vuetifyjs.com/en/components/floating-action-buttons/#small-variant](https://vuetifyjs.com/en/components/floating-action-buttons/#small-variant)

    - vue for문으로 이벤트 처리 예시

        method에 매개변수로 data를 전달해서 활용 가능

    ```javascript
    <template>
    	<v-list-item
    	  v-for="place in places"
    	  :key="place.id"
    		:place="place"
    		@click="test(place)"
    	>
    		:
    	</v-list-item
    </template>

    <script>
    export default {
      name: 'PlaceCard',
      data () {
    		return {
          places: [
            { id:0, name: '경복궁' },
            { id:1, name: '창경궁' },
    							:
          ],
        }
      },
      methods: {
        test(place) {
    			console.log(place.name);
        }
      }
    }
    </script>

    ```

    - image 동적으로 호출하는 방법

        import로 이미지를 가져오고, data에서 return 해준 후, src를 bind해서 사용

    ```javascript
    <template>
    	<img :src="like">
    </template>

    <script>
    import heart from '@/assets/img/heart.png'

    export default {
      name: 'PlaceCard',
      data () {
        return {
          like: heart
    				:
    		}
    	},
    	:
    </script>
    ```



# 회의록 12



## 역할 분담

- 찬진: serverless Framework 설치 & lambda 함수 생성, DB연동(MongoDB - Vue)
- 륜화: 장소 검색
- 진실: vue에서 DB 조회
- 찬영: 모달에서 DB에 데이터 추가



### 오늘 완료한 일정

- DB와 django 연동



### 참고 자료

### python manage.py migrate 에서 decode error 났을 때

sqlparser나 djongo의 버전이 낮아서 [해결링크](https://github.com/nesdis/djongo/issues/156)

```
$ pip install --upgrade sqlparse
$ pip install --upgrade djongo
```



### vue에서 DB 조회하는 방법

- data에서 vue template에서 사용할 변수들을 선언
- axios로 DB와 통신하는 method 작성
- created() 에서 조회하는 method 실행

```
import axios from "axios";

export default {
  name: 'PlaceCard',
  data () {
    return {
      like: heart,
      dislike: heartNo,
      places: [],
    }
  },
  methods: {
    getPost (){
            axios.get("http://127.0.0.1:8000/api/map", {auth: {
                username: "admin",
                password: "admin",

            }})
            .then(response => {
                console.log(response.data);
                this.places=response.data;
            })
            .catch(error => {
                console.log(error)
            });
        },
  },
  created() {
      this.getPost();
    }
}
```

- vue template에서 data사용할 때

`{{ place.title }}` 이런식으로 중괄호 두개로 사용가능

