# import json
# import oracledb
# import pandas as pd

# url = "https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
# params = {
#     "key": "99d405adf342a6d214111aaa15c3a0f5",
#     "itemPerPage": 100,
#     "curPage":1,
# }

# response = requests.get(url,params=params,timeout=10)
# response.raise_for_status()
# data = response.json()

# movies = data["movieListResult"]['movieList'][:100]

# rows = []

# for m in movies:
#     rows.append({
#     "movieCd" : m.get("movieCd",''),
#     "movieNm":m.get("movieNm",''),
#     "movie_Nm_En" : m.get("movie_Nm_En",''),
#     "prdt_year": m.get("prdt_year",''),
#     "open_Dt" : m.get("open_Dt",''),
#     "type_nm": m.get("typeNm", ""),
#     "prdt_stat_nm": m.get("prdtStatNm", ""),
#     "nation_alt": m.get("nationAlt", ""),
#     "genre_alt": m.get("genreAlt", ""),
#     "rep_nation_nm": m.get("repNationNm", ""),
#     "rep_genre_nm": m.get("rep_genre_nm", "") or m.get("repGenreNm", ""),
#     })

# df = pd.DataFrame(rows)

import pandas as pd

# 파일읽어오기
df = pd.read_json('db/searchMovieList.json')
print(df.head(2))


# 파일저장
df.to_csv('searchMovie.csv',encoding='utf-8-sig')
print('완료')