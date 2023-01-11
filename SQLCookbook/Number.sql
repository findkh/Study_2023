-- 7.1 평균 계산하기
select *
from emp

select avg(sal) as avg_sal
from emp

select deptno, avg(sal) as avg_sal
from emp
group by deptno
order by 1, 2

create table t2(sal integer)
insert into t2 values(10)
insert into t2 values(20)
insert into t2 values(null)

select avg(sal) from t2
select distinct 30/2 from t2

select avg(coalesce(sal, 10)) from t2
select distinct 30/3 from t2

select avg(sal) from emp group by deptno

-- 7.2 열에서 최댓값, 최솟값
select min(sal) as min_sal, max(sal) as max_sal from emp

select deptno, min(sal) as min_sal, max(sal) as max_sal from emp group by deptno order by deptno

select deptno, comm from emp where deptno in (10, 30) order by 1

select min(comm), max(comm) from emp

select deptno, min(comm), max(comm) from emp group by deptno order by 1

select min(comm), max(comm) from emp group by deptno 

-- 7.3 열의 값 집계
select sum(sal) from emp

select deptno, sum(sal) as total_for_dept from emp group by deptno order by deptno

select deptno, comm from emp where deptno in (10, 30) order by 1
select sum(comm) from emp
select deptno, sum(comm) from emp where deptno in (10, 30) group by deptno

--7.4 테이블의 행 수 계산
select count(*) from emp

select deptno, count(*) from emp group by deptno order by 1

select count(*), count(deptno), count(comm), count('hello') from emp

select deptno, count(*), count(comm), count('hello') from emp group by deptno

select count(*) from emp group by deptno

--7.5 열의 값 세어보기
select count(comm) from emp

--7.6 누계 생성
select ename, sal, sum(sal) over (order by sal, empno) as running_total
from emp
order by 2

select empno, sal,
       sum(sal) over(order by sal, empno) as running_total1,
       sum(sal) over(order by sal) as running_total2
from emp
order by 2

-- 7.7 누적곱
select empno, ename, sal, exp(sum(ln(sal)) over (order by sal, empno)) as running_prod
from emp
where deptno = 10

-- 7.8 일련의 값 평활화하기
-- 7.9 최빈값 계산
select sal from emp where deptno = 20 order by sal

select sal
from (select sal, dense_rank() over(order by cnt desc) as rnk
      from(select sal, count(*) as cnt
           from emp 
           where deptno = 20
           group by sal
           ) as x
     ) as y
where rnk = 1

-- 7.10 중앙값 계산하기
select sal from emp where deptno = 20 order by sal

select percentile_cont(0.5) within group (order by sal)
from emp 
where deptno = 20

-- 7.11 총계에서 백분율 알아내기
select (sum(case when deptno = 10 then sal end)::numeric / sum(sal)) * 100 as pct 
from emp

select (cast(sum(case when deptno = 10 then sal end) as decimal) / sum(sal)) * 100 as pct
from emp

-- 7.12 null 허용 열 집계하기
select ename, comm
from emp
where deptno = 30
order by comm desc

-- 집계 함수 작업할 때 null은 무시된다. coalesce 함수로 null 처리 해준후에 집계해야 한다.
select avg(comm) from emp where deptno = 30

select avg(coalesce(comm, 0)) from emp where deptno = 30

-- 7.13 최댓값과 최솟값을 배제한 평균 계산
select avg(sal) 
from emp e 
where sal not in ((select min(sal) from emp), (select max(sal) from emp))

select (sum(sal) - min(sal) - max(sal)) / (count(*) - 2)
from emp

-- 7.14 영숫자 문자열을 숫자로 변환하기
-- paul123f321 -> 123321 반환
select cast(
       replace(
       translate('paul123f321', 'abcdefghijklmnopqrstuvwxyz', rpad('#', 26, '#')), '#', '') as integer ) as num
from t1

-- 7.15 누계에서 값 변경하기
create view v8(id, amt, trx)
as 
    select 1, 100, 'PR' from t1 union all
    select 2, 100, 'PR' from t1 union all
    select 3,  50, 'PY' from t1 union all
    select 4, 100, 'PR' from t1 union all
    select 5, 200, 'PY' from t1 union all
    select 6,  50, 'PY' from t1
    
select * from v8

select case when trx = 'PY' then 'PAYMENT' else 'PURCHASE' end trx_type, amt,
                 sum( case when trx = 'PY' then -amt else amt end) over (order by id,amt) as balance
from v8

-- 7.16 중위절대편차로 특잇값 찾기 : 결과가 안나옴
--with median(median) as (select percentile_cont(0.5) within group(order by sal) from emp),
--devtab(deviation) as (select abs(sal-median) from emp join median),
--MedAbsDeviation(MAD) as (select percentile_cont (0.5) within group(order by deviation) from devtab) 
--
--select abs(sal- median)/MAD, sal, ename, job
--FROM MedAbsDeviation join emp

-- 7.17 벤포드의 법칙으로 이상 징후 찾기 : 결과가 안나옴
--with FirstDigits (FirstDigit) as (select left(cast(SAL as CHAR),1) as FirstDigit from emp),
--TotalCount (Total) as (select count(*) from emp),
--ExpectedBenford (Digit,Expected) as (select ID,(log10(ID + 1) - log10(ID)) as expected from t10 where ID < 10)
--
--select count(FirstDigit), Digit, coalesce(count(*)/Total,0) as ActualProportion, Expected
--from FirstDigits
--join TotalCount
--right join ExpectedBenford on FirstDigits.FirstDigit=ExpectedBenford.Digit
--group by Digit
--order by Digit
