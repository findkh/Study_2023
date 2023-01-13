-- 날짜 산술
-- 8.1 일, 월, 연도 가감하기
select hiredate - interval '5 day'   as hd_minus_5D,
       hiredate + interval '5 day'   as hd_plus_5D,
       hiredate - interval '5 month' as hd_minus_5M,
       hiredate + interval '5 month' as hd_plus_5M,
       hiredate - interval '5 year'  as hd_minus_5Y,
       hiredate + interval '5 year'  as hd_plus_5Y
from emp
where deptno = 10

-- 8.2 두 날짜 사이의 일수 알아내기
select ward_hd - allen_hd
from (select hiredate as ward_hd from emp where ename = 'WARD') x,
     (select hiredate as allen_hd from emp where ename = 'ALLEN') y

--T500 테이블에 insert
INSERT INTO T500
WITH RECURSIVE numbers AS
(
    SELECT 1 AS n
    
    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 500
)
SELECT n
FROM numbers;
    
-- 8.3 두 날짜 사이의 영업일수 알아내기
-- BLAKE와 JONES의 HIREDATE 사이의 영업일수 찾기
select sum(case when trim(to_char(jones_hd+t500.id-1,'DAY')) in ( 'SATURDAY','SUNDAY' ) then 0 else 1 end) as days
from (
    select max(case when ename = 'BLAKE' then hiredate end) as blake_hd,
           max(case when ename = 'JONES' then hiredate end) as jones_hd
    from emp
    where ename in ( 'BLAKE','JONES') 
) x, t500
where t500.id <= blake_hd-jones_hd+1


-- 8.4 두 날짜 사이의 월 또는 년 수 알아내기 : 안나옴
select min(hiredate) as min_hd, max(hiredate) as max_hd
from emp

--select year(max_hd) as max_yr, year(min_hd) as min_yr, month(max_hd) as max_mon, month(min_hd) as min_mon
--from(
--    select min(hiredate) as min_hd, max(hiredate) as max_hd from emp
--)x

-- 8.5 두 날짜 사이의 시,분,초 알아내기
select dy * 24 as hr, dy * 24 * 60 as min, dy * 24 * 60 * 60 as sec
from (
    select (max(case when ename = 'WARD' then hiredate end) - max(case when ename = 'ALLEN' then hiredate end)) as dy
    from emp
) x

-- 8.6 1년 중 평일 발생 횟수 계산
select to_char(cast(date_trunc('year', current_date) as date) + gs.id-1, 'DAY'), count(*)
from generate_series(1,366) gs(id)
where gs.id <= (cast( date_trunc('year', current_date) + interval '12 month' as date) - cast(date_trunc('year', current_date) as date))
group by to_char(cast(date_trunc('year', current_date) as date) + gs.id-1,'DAY')

select cast(date_trunc('year', current_date) as date) as start_date 
from t1

select cast( date_trunc('year',current_date) as date) + gs.id-1 as start_date
from generate_series (1,366) gs(id)
where gs.id <= (cast(date_trunc('year', current_date) + interval '12 month' as date) - cast(date_trunc('year', current_date) as date))

select to_char(cast(date_trunc('year', current_date) as date) + gs.id-1,'DAY') as start_dates, count(*)
from generate_series(1,366) gs(id)
where gs.id <= (cast(date_trunc('year', current_date) + interval '12 month' as date) - cast(date_trunc('year', current_date) as date))
group by to_char(cast(date_trunc('year', current_date) as date) + gs.id-1,'DAY')

--8.7 현재 레코드와 다음 레코드 간의 날짜 차이
select x.*, x.next_hd - x.hiredate as diff 
from (
    select e.deptno, e.ename, e.hiredate, lead(hiredate)over(order by hiredate) as next_hd
    from emp e
    where e.deptno = 10
) x