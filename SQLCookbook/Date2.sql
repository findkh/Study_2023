-- 날짜 산술
-- 9.1 윤년 여부
-- 2월의 마지막 날을 확인
select max(to_char(tmp2.dy+x.id,'DD')) as dy
    from (
            select dy, to_char(dy,'MM') as mth
            from ( 
                    select cast(cast(date_trunc('year',current_date) as date) + interval '1 month' as date) as dy
                    from t1
                 ) tmp1
         ) tmp2, generate_series (0,29) x(id)
where to_char(tmp2.dy+x.id,'MM') = tmp2.mth

select cast(cast(date_trunc('year', current_date) as date) + interval '1 month' as date) as dy
from t1

select dy, to_char(dy, 'MM') as mth
from (
    select cast(cast(date_trunc('year', current_date) as date) + interval '1 month' as date) as dy
    from t1
) as tmp1

select tmp2.dy + x.id as dy, tmp2.mth
from (
        select dy, to_char(dy,'MM') as mth
        from ( 
                select cast(cast(date_trunc('year',current_date) as date) + interval '1 month' as date) as dy
                from t1
             ) tmp1
     ) tmp2, generate_series (0,29) x(id)
where to_char(tmp2.dy + x.id, 'MM') = tmp2.mth

-- 9.2 연도의 날짜 수 알아내기
-- 1. 올해의 첫 날을 찾기
-- 2. 다음 해의 첫날을 알기 위해 1년을 추가
-- 3. 2에서 현재 연도 뺴기
select cast((curr_year + interval '1 year') as date) - curr_year
    from (select cast(date_trunc('year', current_date) as date) as curr_year from t1) x
    
select cast(date_trunc('year', current_date) as date) as curr_year
from t1

-- 9.3 날짜에서 시간 단위 추출하기
select to_number(to_char(current_timestamp, 'hh24'), '99')as hr,
       to_number(to_char(current_timestamp, 'mi'), '99')as min,
       to_number(to_char(current_timestamp, 'ss'), '99')as sec,
       to_number(to_char(current_timestamp, 'dd'), '99')as day,
       to_number(to_char(current_timestamp, 'mm'), '99')as mth,
       to_number(to_char(current_timestamp, 'yyyy'), '9999')as yr
from t1

-- 9.4 월의 첫번째 요일과 마지막 요일 알아내기
select firstday, 
       cast(firstday + interval '1 month' - interval '1 day' as date) as lastday
from (select cast(date_trunc('month', current_date) as date) as firstday 
from t1) x

-- 9.5 연도의 특정 요일의 모든 날짜 알아내기
-- 올해의 금요일 목록 생성
with recursive cal(dy)
as (
    select current_date - (cast(extract(day from current_date) as integer) -1)
    union all
    select dy + 1
    from cal
    where extract(year from dy)=extract(year from (dy+1))
)
select dy, extract(dow from dy) from cal
where cast(extract(dow from dy) as integer) = 5

-- 9.6 월의 특정 요일의 첫 번째 및 마지막 발생일 알아내기
-- 이번달의 첫번쨰 및 마지막 월요일 찾기
select first_monday,
       case to_char(first_monday+28,'mm') when mth then first_monday + 28 else first_monday + 21 end as last_monday
from (
        select case sign(cast(to_char(dy, 'd') as integer) -2)
                when 0 then dy
                when -1 then dy + abs(cast(to_char(dy,'d') as integer)-2)
                when 1 then (7-(cast(to_char(dy,'d') as integer)-2)) + dy
                end as first_monday,
                mth
        from (
            select cast(date_trunc('month',current_date) as date) as dy, to_char(current_date,'mm') as mth
            from t1
        ) x
) y

-- 9.7 이번달 달력 만들기
select  max(case dw when 2 then dm end) as Mo,
        max(case dw when 3 then dm end) as Tu,
        max(case dw when 4 then dm end) as We,
        max(case dw when 5 then dm end) as Th,
        max(case dw when 6 then dm end) as Fr,
        max(case dw when 7 then dm end) as Sa,
        max(case dw when 1 then dm end) as Su
from (
        select *
        from (
                select cast(date_trunc('month',current_date) as date)+x.id, 
                       to_char(cast(date_trunc('month',current_date) as date)+x.id,'iw') as wk,
                       to_char(cast(date_trunc('month',current_date) as date) + x.id,'dd') as dm,
                       cast(to_char(cast(date_trunc('month',current_date)as date) + x.id,'d') as integer) as dw,
                       to_char(cast(date_trunc('month',current_date)as date)+x.id,'mm') as curr_mth,
                       to_char(current_date,'mm') as mth
                from generate_series (0,31) x(id)
        ) x
        where mth = curr_mth
) y
group by wk
order by wk

  
-- 9.8 해당 연도의 분기 시작일 및 종료일 나열
with recursive x (dy,cnt) as (
    select current_date - cast(extract(day from current_date) as integer) +1 dy, id
    from t1
    union all
    select cast(dy  + interval '3 months' as date) , cnt + 1
    from x
    where cnt+1 <= 4
 )
select  cast(dy - interval '3 months' as date) as Q_start, dy-1 as Q_end
from x

--9.9 지정 분기의 시작일 및 종료일
 select date(q_end-(2*interval '1 month')) as q_start,
         date(q_end+interval '1 month'-interval '1 day') as q_end
from (
    select to_date(substr(yrq::varchar,1,4)||mod(yrq,10)*3,'yyyymm') as q_end
    from (
          select 20051 as yrq from t1 union all
          select 20052 as yrq from t1 union all
          select 20053 as yrq from t1 union all
          select 20054 as yrq from t1
    ) x
) y
        
select substr(cast(yrq as varchar), 1, 4) yr, mod(yrq, 10)*3 mth
from(
      select 20051 as yrq from t1 union all
      select 20052 as yrq from t1 union all
      select 20053 as yrq from t1 union all
      select 20054 as yrq from t1
) x

-- 9.10 누락된 날짜 채우기
select distinct extract(year from hiredate) as year from emp

with recursive x (start_date, end_date)
as
(
    select     cast(min(hiredate) - (cast(extract(day from min(hiredate)) as integer) - 1) as date), max(hiredate)
    from emp
    union all
    select cast(start_date + interval '1 month' as date), end_date
    from x
    where start_date < end_date
)

select x.start_date,count(hiredate)
from x left join emp on (extract(month from start_date) = extract(month from emp.hiredate)
        and 
        extract(year from start_date) = extract(year from emp.hiredate))
group by x.start_date
order by 1

-- 9.11 특정 시간 단위 검색
select ename
from emp
where rtrim(to_char(hiredate,'month')) in ('february','december') or rtrim(to_char(hiredate,'day')) = 'tuesday'

-- 9.12 날짜의 특정 부분으로 레코드 비교
select a.ename || ' was hired on the same month and weekday as '|| b.ename as msg 
from emp a, emp b
where to_char(a.hiredate,'DMON') = to_char(b.hiredate,'DMON') and a.empno < b.empno
order by a.ename

-- 9.13 중복 날짜 범위 식별하기
CREATE TABLE public.emp_project (
    empno varchar NULL,
    ename varchar NULL,
    proj_id varchar NULL,
    proj_start date NULL,
    proj_end date NULL
);

INSERT INTO public.emp_project (empno,ename,proj_id,proj_start,proj_end) VALUES
     ('7782','CLARK','1','2005-01-16','2005-01-18'),
     ('7782','CLARK','4','2005-01-19','2005-01-24'),
     ('7782','CLARK','7','2005-01-22','2005-01-25'),
     ('7782','CLARK','10','2005-01-25','2005-01-28'),
     ('7782','CLARK','13','2005-01-28','2005-02-02'),
     ('7839','KING','2','2005-01-17','2005-01-21'),
     ('7839','KING','8','2005-01-23','2005-01-25'),
     ('7839','KING','14','2005-01-19','2005-01-30'),
     ('7839','KING','11','2005-01-26','2005-01-27'),
     ('7839','KING','5','2005-01-20','2005-01-24');
INSERT INTO public.emp_project (empno,ename,proj_id,proj_start,proj_end) VALUES
     ('7934','MILLER','3','2005-01-18','2005-01-22'),
     ('7934','MILLER','12','2005-01-27','2005-01-28'),
     ('7934','MILLER','15','2005-01-30','2005-02-03'),
     ('7934','MILLER','9','2005-01-24','2005-01-27'),
     ('7934','MILLER','6','2005-01-21','2005-01-23');

select * from emp_project

select a.empno,a.ename, 'project '||b.proj_id||' overlaps project '||a.proj_id as msg
from emp_project a, emp_project b
where a.empno = b.empno
    and b.proj_start >= a.proj_start
    and b.proj_start <= a.proj_end
    and a.proj_id != b.proj_id