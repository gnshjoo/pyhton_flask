# pyhton_flask

###1. flask, mysql, docker, docker-compose 사용

###2. 구현
 docker compose up -d 실행 후 localhost:5000으로 요청하시면 됩니다.

#### 기업명 검색
```
 GET /company/search?words=[검색명]
    Response
    {
        "msg" : [{
        "id": 1,
        "company_ko": "원티드랩",
        "company_en": "Wantedlab",
        "company_ja": "",
        "tag_ja": "タグ_4|タグ_20|タグ_16",
        "tag_en": "tag_4|tag_20|tag_16",
        "tag_ko": "태그_4|태그_20|태그_16"
        }]
    }
 
```

#### 태그명으로 회사검색
```
 GET /company/search?tags=[검색명]
    Response
    {
        "msg" : [{
        "id": 1,
        "company_ko": "원티드랩",
        "company_en": "Wantedlab",
        "company_ja": "",
        "tag_ja": "タグ_4|タグ_20|タグ_16",
        "tag_en": "tag_4|tag_20|tag_16",
        "tag_ko": "태그_4|태그_20|태그_16"
        }]
    }
 
```

#### 태그 정보 추가

```
 POST /tag
    Body
    {
        company: "원티드랩", ## 회사명 풀네임으로 입력
        type : "ko", ## 검색 언어 (ko | ja | en )
        tag : "111" ## 태그 뒤 숫자 입력
    }
    
    Response
    {
        "msg" : [{
        "id": 1,
        "company_ko": "원티드랩",
        "company_en": "Wantedlab",
        "company_ja": "",
        "tag_ja": "タグ_4|タグ_20|タグ_16|タグ_111",
        "tag_en": "tag_4|tag_20|tag_16|tag_111",
        "tag_ko": "태그_4|태그_20|태그_16|태그_111"
        }]
    }
 
```

#### 태그 정보 삭제
```
 DELETE /tag
    Body
    {
        company: "원티드랩", ## 회사명 풀네임으로 입력
        type : "ko", ## 검색 언어 (ko | ja | en )
        tag : "111" ## 태그 뒤 숫자 입력
    }
    
    Response
    {
        "msg" : [{
        "id": 1,
        "company_ko": "원티드랩",
        "company_en": "Wantedlab",
        "company_ja": "",
        "tag_ja": "タグ_4|タグ_20|タグ_16",
        "tag_en": "tag_4|tag_20|tag_16",
        "tag_ko": "태그_4|태그_20|태그_16"
        }]
    }
 
```