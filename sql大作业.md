```sql
CREATE TABLE IF NOT EXISTS movie(
    movieId INT primary key,
    title VARCHAR(500),
    genres VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS rating(
    userId INT,
    movieId INT,
    rating FLOAT,
    timestamp VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS tag(
    userId INT,
    movieId INT,
    tag VARCHAR(500),
    timestamp VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS link(
    movieId INT primary key,
    imdbId VARCHAR(500),
    tmbdId VARCHAR(500),
    FOREIGN KEY (movieId) REFERENCES movie(movieId)
);

CREATE TABLE IF NOT EXISTS genome_tags(
    tagId INT primary key,
    tag VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS genome_scores(
    movieId INT,
    tagId INT,
    relevance VARCHAR(500),
    FOREIGN KEY (movieId) REFERENCES movie(movieId),
    FOREIGN KEY (tagId) REFERENCES genome_tag(tagId)
);


alter table movielens.tag DROP FOREIGN KEY tag_ibfk_1;
alter table movielens.genome_score DROP FOREIGN KEY genome_score_ibfk_1;
alter table movielens.genome_score DROP FOREIGN KEY genome_score_ibfk_2;


LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/movies.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/links.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/ratings.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/tags.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/genome-tags.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/Peipengyu/Desktop/ml-25m/genome-scores.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

/* 4. 将外键依赖恢复 */
alter table movielens.link ADD CONSTRAINT link_ibfk_1 FOREIGN KEY (movieId) REFERENCES movie(movieId);
alter table movielens.genome_score ADD CONSTRAINT genome_score_ibfk_1 FOREIGN KEY (movieId) REFERENCES movie(movieId);
alter table movielens.genome_score ADD CONSTRAINT genome_score_ibfk_2 FOREIGN KEY (tagId) REFERENCES genome_tag(tagId);

/* 5. 建立索引 */
CREATE INDEX index_1 ON movie (movieId);
CREATE INDEX index_2 ON rating (userId);
CREATE INDEX index_3 ON tag (userId, movieId);
CREATE INDEX index_4 ON link (movieId);
CREATE INDEX index_5 ON genome_tag (tagId);

/* 1. 一共有多少不同的用户 */
select count(1) from (select userId  from tag union select userId from rating) k;
/* 2. 一共有多少不同的电影 */
select count(1) from (select movieid from movie group by movieid) k;
/* 3. 一共有多少不同的电影 */
select count(distinct(t)) from (select regexp_split_to_table(REPLACE(genres,'|',','),',') t from movie) k;
/* 4. 一共有多少电影没有外部链接 */
SELECT count(1) from (select movieId from movie EXCEPT select movieId from link) t;
/* 5. 2018年一共有多少人进行过电影评分 */
select count(distinct(userId)) from rating where timestamp between '1514736000' and '1546271999';
/* 6. 2018年评分5分以上的电影及其对应的标签 */
select t1.movieid,t1.sc,t2.tag from (select movieid,avg(rating) sc from rating  where timestamp between '1514736000' and '1546271999' group by movieid having avg(rating) >= 5) t1 left join (select movieid,string_agg(tag, '|') tag from tag  where timestamp between '1514736000' and '1546271999' group by movieid) t2 on t1.movieid = t2.movieid;





```

