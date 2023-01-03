-- 2.1 지정한 순서대로 쿼리 결과 반환
-- 부서 10에 속한 사원명, 직책 및 급여를 
-- 최저에서 최고 급여 순서로 표시
select ename, job, sal
from emp
where deptno = 10
order by sal asc

-- 2.2 다중 필드로 정렬
-- emp 테이블에서 deptno 기준 오름차순으로 행을 정렬한 다음
-- 급여 내림차순으로 정렬
select empno, deptno, sal, ename, job
from emp
order by deptno asc, sal desc

-- 2.3 부분 문자열로 정렬
-- emp 테이블에서 사원명과 직급을 반환,
-- job 열의 마지막 두 문자를 기준으로 정렬
select ename, job, substr(job, length(job)-1) 
from emp
order by substr(job, length(job)-1) desc

-- 2.4 혼합 영숫자 데이터 정렬
create view v
as 
	select ename || ' ' || deptno as data
	from emp
	
select * from v

-- REPLACE 및 TRANSLATE 함수를 사용하여 정렬한 문자열을 수정한다.

-- DATANO로 정렬
select data
from v
order by replace(data,
		 replace(
		 	translate(data, '0123456789', '#########'),'#',''),'')
		 	
-- ENAME으로 정렬
select data
from v
order by replace(
		 	translate(data, '0123456789', '#########'),'#','')
		 	
-- TRANSLATE 및 REPLACE 함수는 각 행에서 숫자나 문자를 제거한다.
select data,
		replace(data,
			replace(
			translate(data, '0123456789', '#########'), '#', ''), '') nums,
		replace(
			translate(data, '0123456789', '#########'), '#', '') chars
from v

-- 2.5 정렬할 때 null 처리
-- null을 마지막에 정렬할지를 지정하는 방법
select ename, sal, comm
from emp
order by 3 desc

-- null이 아닌 comm을 오름차순 정렬하고, 모든 null은 마지막에 나타냄
select ename, sal, comm
from (
	select ename, sal, comm, case when comm is null then 0 else 1 end as is_null
	from emp
)as x
order by is_null desc, comm

-- null이 아닌 comm을 내림차순 정렬하고, 모든 null은 마지막에 나타냄
select ename, sal, comm
from (
	select ename, sal, comm, case when comm is null then 0 else 1 end as is_null
	from emp
)as x
order by is_null desc, comm desc

-- null을 처음에 나타낸 후 null이 아닌 comm은 오름차순 정렬
select ename, sal, comm
from (
	select ename, sal, comm, case when comm is null then 0 else 1 end as is_null
	from emp
)as x
order by is_null, comm

-- null을 처음에 나타낸 후 null이 아닌 comm은 내림차순 정렬
select ename, sal, comm
from (
	select ename, sal, comm, case when comm is null then 0 else 1 end as is_null
	from emp
)as x
order by is_null, comm desc

-- 데이터 종속 키 기준으로 정렬
-- job이 SALESMAN이면 comm기준으로 정렬하고, 그렇지 않으면 sal 기준으로 정렬
select ename, sal, job, comm
from emp
order by case when job='SALESMAN' then comm 
			  else sal 
		 end

select ename, sal, job, comm, case when job = 'SALESMAN' then comm else sal end
from emp
order by 5

		