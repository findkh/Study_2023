-- emp_bonus 테이블 생성 후 데이터값 변경하면서 해야함
CREATE TABLE public.emp_bonus (
	empno int4 NULL,
	received date NULL,
	"TYPE" int4 NULL
);

-- 행 집합을 다른 행 위에 추가하기
-- EMP 테이블에 있는 부서 10의 사원명 및 부서 번호와 함께, DEPT 테이블에 있는 각 부서명 및 부서 번호를 표시
select ename as ename_and_dname, deptno 
from emp 
where deptno = 10
union all
select '----------', null
from t1
union all
select dname, deptno 
from dept

-- union all : 여러 행 소스의 행들을 하나의 결과셋으로 결합한다.
--			   주의할 점은 중복 항목도 포함한다. 중복을 필터링하려면 union 연산자를 사용한다.
select deptno from emp
union
select deptno from dept

-- union all 대신 union을 지정하면 중복 제거하는 정렬 작업이 발생한다.
-- union all의 출력에 distinct를 적용하는 것과 결과는 같다.
-- 필수가 아니라면 distinct는 가능한한 사용하지 않는 것이 좋다.
select distinct deptno
from (
	select deptno 
	from emp e
	union all
	select deptno
	from dept
) as x

-- 3.2 연관된 여러 행 결합하기
-- 부서 10의 모든 사원명과 각 사원의 부서 위치를 함께 표시
select e.ename, e.deptno, d.loc 
from emp e, dept d
where e.deptno = d.deptno and e.deptno = 10

select e.ename, d.loc,
	   e.deptno as emp_deptno,
	   d.deptno as delpt_deptno
from emp e, dept d
where e.deptno = d.deptno and e.deptno = 10

-- join 사용
select e.ename, d.loc
from emp e 
	inner join dept d on (e.deptno = d.deptno)
where e.deptno = 10

-- 3.3 두 테이블의 공통 행 찾기
create view v2  
as
select ename, job, sal
from emp
where job = 'CLERK'

select * from v2

-- 뷰 v2의 행과 일치하는 EMP 테이블의 모든 사원의 EMPNO, ENAME, JOB, SAL, DEPTNO를 반환
-- 뷰 v2에서 값을 반환할 때 사용하는 방법: join 사용
select e.empno, e.ename, e.job, e.sal, e.deptno
from emp e
	join v2 v on(e.ename = v.ename)

-- 뷰 v2에서 값을 반환할 때 사용하는 방법: 다중 조인 조건 사용
select e.empno, e.ename, e.job, e.sal, e.deptno
from emp e, v2
where e.ename = v2.ename
	and e.job = v2.job
	and e.sal = v2.sal
	
-- 뷰 v2에서 열을 반환할 필요가 없다면 In과 함께 INTERSECT 사용 가능
-- INTERSECT는 두 행 소스에 공통된 행을 반환한다. 중복행은 반환하지 않는다.
select empno, ename, job, sal, deptno
from emp 
where (ename, job, sal) 
	in (
	select ename, job, sal
	from emp
	intersect
	select ename, job, sal
	from v2
	)
	
-- 한 테이블에서 다른 테이블에 존재하지 않는 값 검색
-- emp 테이블에 없는 dept 테이블의 부서 정보 찾기
select deptno from dept
except
select deptno from emp
-- except 연산자는 첫번째 결과셋을 가져와서 두번째 결과셋에 중복된 행을 모두 제거한다.
-- 비교할 데이터 유형 및 값 개수는 두 select 목록에서 일치해야 한다. 
-- 중복 항목은 반환하지 않는다.
-- 서브쿼리에 없는 상위 쿼리에서 행을 반환한다.

-- 3.5 다른 테이블 행과 일치하지 않는 행 검색
-- 사원이 없는 부서 찾기
select d.*
from dept d 
	left outer join emp e on (d.deptno = e.deptno)
where e.deptno is null

-- 3.6 다른 조인을 방해하지 않고 쿼리에 조인 추가하기
select * from emp_bonus

select e.ename, d.loc
from emp e, dept d
where e.deptno = d.deptno

select e.ename, d.loc, eb.received
from emp e, dept d, emp_bonus eb
where e.deptno=d.deptno 
	and e.empno = eb.empno
	
-- 외부 조인을 사용하여 데이터의 손실 없이 추가 정보 얻기
select e.ename, d.loc, eb.received
from emp e 
	join dept d on (e.deptno = d.deptno)
	left join emp_bonus eb on (eb.empno = e.empno)
order by 2
	
-- 스칼라 서브쿼리(select 목록에 있는 서브쿼리)를 사용하여 외부 조인을 흉내낼 수 있다.
select e.ename, d.loc,
	(select eb.received from emp_bonus eb
	 where eb.empno = e.empno
	) as received 
from emp e, dept d
where e.deptno  = d.deptno
order by 2

-- 3.7 두 테이블에 같은 데이터가 있는지 확인
create view v3
as
select * from emp where deptno != 10
union all 
select * from emp where ename = 'WARD'

select * from v3

-- v3와 emp 테이블이 정확히 같은 지 확인
-- 집합 연산 except와 union all을 사용하여 v3에서 emp 테이블과 다른 점을 찾고 emp 테이블에서 뷰 v와 다른점을 찾아서 조합한다.
(
	select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
	from v3
	group by empno, ename, job, mgr, hiredate, sal, comm, deptno
	except
	select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
	from emp
	group by empno, ename, job, mgr, hiredate, sal, comm, deptno
)
union all 
(
	select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
	from emp
	group by empno, ename, job, mgr, hiredate, sal, comm, deptno
	except
	select empno, ename, job, mgr, hiredate, sal, comm, deptno, count(*) as cnt
	from v3
	group by empno, ename, job, mgr, hiredate, sal, comm, deptno
)

select count(*)
from emp
union
select count(*)
from dept

-- 3.9 집계를 사용할 때 조인 수행하기
-- 부서 10에 해당하는 사원의 급여 합계와 보너스 합계
select * from emp_bonus eb 

select e.empno, e.empno, e.sal, e.deptno,
	   e.sal * case when eb."TYPE" = 1 then .1
	   				when eb."TYPE" = 2 then .2
	   				else .3
	   		   end as bonus
from emp e, emp_bonus eb
where e.empno = eb.empno and e.deptno = 10

-- 보너스 금액 합산 emp_bonus 조인
select deptno, sum(sal) as total_sal, sum(bonus) as total_bonus
from (
	select e.empno, e.empno, e.sal, e.deptno,
	   e.sal * case when eb."TYPE" = 1 then .1
	   				when eb."TYPE" = 2 then .2
	   				else .3
	   		   end as bonus
	from emp e, emp_bonus eb
	where e.empno = eb.empno and e.deptno = 10
) as x
group by deptno

select sum(sal)
from emp e where deptno = 10

-- 급여의 합계가 맞지 않는다.
-- 조인에 의해 생성된 sal 열의 중복 행때문에 합계가 맞는 않는다.
-- -> distinct를 사용하여 급여의 합계만 수행한다.
select deptno, sum(distinct sal) as total_sal, sum(bonus) as total_bonus
from (
	select e.empno, e.empno, e.sal, e.deptno,
	   e.sal * case when eb."TYPE" = 1 then .1
	   				when eb."TYPE" = 2 then .2
	   				else .3
	   		   end as bonus
	from emp e, emp_bonus eb
	where e.empno = eb.empno and e.deptno = 10
) as x
group by deptno

-- 다른 방법 : 부서 10의 모든 급여 합계를 먼저 계산하고 EMP 테이블에 조인한 다음 EMP_BONUS 테이블에 조인한다
select d.deptno, d.total_sal,
	   sum(e.sal * case when eb."TYPE" = 1 then .1
	   					when eb."TYPE" = 2 then .2
	   					else .3 end) as total_bonus
from emp e,
	 emp_bonus eb,
	 (
	 	select deptno, sum(sal) as total_sal
	 	from emp
	 	where deptno = 10
	 	group by deptno
	 ) as d
where e.deptno = d.deptno
	and e.empno = eb.empno
group by d.deptno, d.total_sal

-- 3.10 집계 시 외부 조인 수행하기
-- 부서 10의 모든 사원에게 보너스가 주어지지 않도록 EMP_BONUS 테이블을 수정
-- EMP_BONUS 테이블과 부서 10의 모든 급여 합계와 부서 10의 모든 사원에 대한 모든 보너스 합계를 찾기
select * from emp_bonus eb 

-- EMP_BOUNS에 외부 조인한 다음 부서 10의 각 급여에 대해서만 합계 수행
select deptno, sum(distinct sal) as total_sal, sum(bonus) as total_bonus
from (
	select e.empno, e.empno, e.sal, e.deptno,
	   e.sal * case when eb."TYPE" is null then 0
		   			when eb."TYPE" = 1 then .1
	   				when eb."TYPE" = 2 then .2
	   				else .3
	   		   end as bonus
	from emp e
		left outer join emp_bonus eb on (eb.empno = e.empno)
	where e.deptno = 10
) as x
group by deptno

-- 윈도우 함수 SUM OVER 사용 : 윈도우 함수에 대해 DISTINCT가 구현되지 않음 에러 발생....
select distinct deptno, total_sal, total_bonous
from (
	select 
	   e.empno, 
	   e.ename, 
	   sum(distinct e.sal) over (partition by e.deptno) as total_sal,
	   e.deptno,
	   sum(e.sal * case when eb."TYPE" is null then 0
			   			when eb."TYPE" = 1 then .1
		   				when eb."TYPE" = 2 then .2
		   				else .3
		   		   end) over
		(partition by deptno) as total_bonus
	from emp e 
		left outer join emp_bonus eb on (e.empno = eb.empno)
	where e.deptno = 10
) as x

-- 다른 방법
select d.deptno,
       d.total_sal,
       sum(e.sal * case when eb."TYPE" = 1 then .1
                        when eb."TYPE" = 2 then .2
                        else .3 
                   end) as total_bonus
from emp e,
     emp_bonus eb,
     (
        select deptno, sum(sal) as total_sal
        from emp
        where deptno = 10
        group by deptno
     ) as d
where e.deptno = d.deptno and e.empno = eb.empno
group by d.deptno, d.total_sal


-- 3.11 여러 테이블에서 누락되는 데이터 반환
select d.deptno, d.dname, e.ename
from dept d 
    left outer join emp e on (d.deptno=e.deptno)

-- 데이터 추가
insert into emp (empno,ename,job,mgr,hiredate,sal,comm,deptno)
select 1111,'YODA','JEDI',null,hiredate,sal,comm,null
from emp
where ename = 'KING'

select d.deptno,d.dname,e.ename
from dept d 
    right outer join emp e on (d.deptno=e.deptno)
    
-- YODA와 OPERATIONS에 대한 행도 반환하게 만들기
-- 전체 외부 조인을 사용하여 공통 값 기준으로 두 테이블에서 누락된 데이터를 반환한다.
select d.deptno, d.dname, e.ename
from dept d 
full outer join emp e on (d.deptno = e.deptno)

-- 3.12 연산 및 비교에서 null 사용하기
-- 커미션이 사원 ward의 커미션보다 적은 모든 사원을 emp 테이블에서 찾는다. 이때 커미션이 null인 사원도 포함해야 한다.
select ename, comm
from emp
where coalesce(comm, 0) < (select distinct comm from emp where ename = 'WARD')

select ename, comm, coalesce(comm, 0)
from emp
where coalesce(comm, 0) < ( select distinct comm from emp where ename = 'WARD')
