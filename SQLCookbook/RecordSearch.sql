-- 레코드 검색
-- 1.1 테이블의 모든 행과 열 검색
select * from emp 

-- 1.2 테이블에서 행의 하위 집합 검색
-- 부서 번호가 10에 속한 모든 사원
select * from emp where deptno = 10

-- 1.3 여러 조건을 충족하는 행 찾기
-- 부서 번호 10의 모든 사원,
-- 커미션을 받는 사원, 
-- 최대 2000달러를 받는 부서 번호 20의 사원을 찾아라
select * from emp 
where 
	deptno = 10
	or comm is not null 
	or (sal <= 2000 and deptno = 20)
	
-- 1.4 테이블에서 열의 하위 집합 검색
select ename, deptno, sal from emp

-- 1.5 열에 의미있는 이름 지정
select sal as salary, comm as commission
from emp

-- 1.6 where절에서 별칭이 지정된 열 참조
--select sal as salary, comm as commision
--from emp 
--where salary < 5000
-- 쿼리를 인라인 뷰로 감싸서 별칭이 지정된 열을 참조할 수 있다.
select *
from (
	select sal as salary, comm as commision
	from emp
) as x
where salary < 5000
-- where 절은 select 절을 실행하기 전에 판단되므로 별칭이 존재하지 않는다. 따라소 where절 처리가 완료될 때까지 적용할 수 없다.
-- from 절은 where 절보다 먼저 평가되므로 인라인 뷰에 배치한다.

-- 1.7 열 값 이어 붙이기
-- 데이터 셋 만들기
-- CLARK WORKS AS A MANAGER
-- KING WORKS AS A PRESIDENT
-- MILLER WORKS AS A CLERK
select ename, job
from emp
where deptno = 10

-- 내장 함수를 사용
-- 이중 수직선(||)을 연결 연산자로 사용
select ename || ' WORK AS A ' || job as msg
from emp
where deptno = 10

-- 1.8 select 문에서 조건식 사용
-- select 문의 값에 대해 if-else 연산을 수행
-- 사원이 2000달러 이하의 급여  status = UNDERPAID
-- 사원이 2000달러 초과 4000달러 미만의 급여  status = OK
-- 사원이 4000달러 이상의 급여  status = OVERPAID
select ename, sal, 
	case 
		when sal <= 2000 then 'UNDERPAID'
		when sal >= 4000 then 'OVERPAID'
		else 'OK'
	end as status
from emp

-- 1.9 반환되는 행 수 제한하기
-- 쿼리에서 반환되는 행 수를 제한 순서는 상관 없으며 몇 개의 행이든 가능
select * from emp
limit 10

-- 1.10 테이블에서 n개의 무작위 레코드 반환
-- 연속 실행 시 각기 다른 5개 행 집합을 생성하도록 구문 수정
select ename, job
from emp
order by random() limit 5

-- 1.11 null값 찾기
-- 특정 열에 대해 값이 null인 모든 행을 찾기
select *
from emp
where comm is null

-- 1.12 null을 실제값으로 변환하기
select ename, coalesce(comm,0) as comm
from emp

select ename, case when 
			comm is not null then comm
			else 0
		end comm
from emp

-- 1.13 패턴 검색
select ename, job
from emp
where deptno in(10, 20)

-- 부서 10과 20의 사원들 중 이름에 'I'가 있거나 직급명이 'ER'로 끝나는 사원만 반환
select ename, job
from emp
where deptno in (10, 20)
	and (ename like '%I%' or job like '%ER')
