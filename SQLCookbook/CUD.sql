-- 4.1 새로운 레코드 삽입
-- DEPT 테이블에 새 레코드 삽입, DEPTNO:50, DNAME:PROGRAMMING, LOC:BALTIMORE
insert into dept (deptno, dname, loc)
values(50, 'PROGRAMMING', 'BALTIMORE')

-- 4.2 기본값 삽입하기
create table D(id integer default 0)

select * from D
-- insert문의 값 목록에서 0을 명시적으로 지정하지 않고 0을 삽입
insert into D (id) values (default)

insert into D default values

select * from D

-- null로 기본값 오버라이딩하기
create table E(id integer default 0, foo varchar(10))

-- ID 값에 대해 null 값을 삽입
insert into E(id, foo) values(null, 'Brighten') -- 기본값 null

select * from E

insert into E(foo) values('Brighten') -- 기본값 0

-- 4.4 한 테이블에서 다른 테이블로 행 복사하기
-- dept 테이블에서 dept_east 테이블로 행을 복사

CREATE TABLE public.dept_east (
    deptno int4 NULL,
    dname varchar(14) NULL,
    loc varchar(13) NULL
);

insert into dept_east (deptno, dname, loc)
select deptno, dname, loc
from dept 
where loc in ('NEW YORK', 'BOSTON')

select * from dept_east de 

-- 테이블 정의 복사하기
-- 테이블의 행은 복사하지 않고 열구조만 복사한다.
create table dept_2
as select *
from dept d 
where 1 = 0
-- CTAS(Create Table As Select)문을 사용하는 경우 where절에 거짓 조건을 지정하지 않으면 쿼리의 모든 행으로 생성 중인 새 테이블을 체운다.
-- where 절에 있는 1 = 0 표현식으로 인해 행이 반환되지 않는다.
-- CTAS 문의 결과는 쿼리의 select 절에 있는 열에 기반을 두는 빈 테이블이다.

select * from dept_2

-- 4.6 한 번에 여러 테이블에 삽입하기
-- 쿼리에서 반환된 행을 가져와서 여러 대상 테이블에 삽입
-- dept의 행을 dept_east, dept_west, dept_mid 테이블에 삽입, 이 테이블은 비어 있다.
-- -> MySQL, PostgreSQL, SQL Server는 다중 테이블 삽입을 지원하지 않는다.

-- 4.7 특정 열에 대한 삽입 차단
-- 사용자 또는 잘못된 sw가 특정 테이블 열에 값을 삽입하는 것을 방지
-- emp 테이블에 값을 삽입하도록 허용하되, empno, ename, job 열에만 삽입하도록 한다.
create view new_emps as
select empno, ename, job
from emp

-- 테이블에 표시할 열만 노출되는 뷰를 만들고, 모든 삽입 내용이 해당 뷰룰 통과하도록 한다.
insert into new_emps(empno, ename, job)
values(1, 'Jonathan', 'Editor')

-- 4.8 테이블에서 레코드 수정하기
-- 부서 20에 속한 모든 사원의 급여를 10% 인상한다.
update emp
set sal = sal * 1.10
where deptno = 20

select deptno, ename, sal
from emp
where deptno = 20
order by 1, 3

-- 4.9 일치하는 행이 있을 때 업데이트하기
-- emp_bonus 테이블에 사원 정보가 있다면 해당 사원의 급여를 20% 인상
select *
from emp_bonus

update emp
set sal = sal * 1.20
where empno in (select empno from emp_bonus)

select empno, ename
from emp
where empno in (select empno from emp_bonus)

-- 4.10 다른 테이블 값으로 업데이트 하기
CREATE TABLE public.new_sal (
    deptno int4 NOT NULL,
    sal int4 NULL,
    CONSTRAINT new_sal_pk PRIMARY KEY (deptno)
);

select *
from new_sal

-- emp.deptno와 new_sal.deptno 값이 일치하는 경우, new_sal 테이블을 사용하여 emp 테이블에 특정 사원의 급여 및 커미션 업데이트
-- emp.sal을 new_sal.sal로 업데이트한 뒤 emp.comm을 new_sal.sal의 50%로 업데이트
select deptno, ename, sal, comm
from emp
order by 1

-- new_Sal과 emp를 조인하여 새 comm 값을 찾아 update로 반환한다.
update emp 
set sal = ns.sal,
    comm = ns.sal/2
from new_sal ns
where ns.deptno = emp.deptno

-- 4.11 레코드 병합하기
-- emp_commocmition 테이블 수정
-- - emp_commision의 사원이 emp 테이블에 있을 때 해당 사원의 커미션을 1000으로 업데이트
-- - comm을 1000으로 업데이트할 가능성이 있는 모든 사원에 대해 sal이 2000미만이면 해당 사원을 삭제(emp_commision에 존재하지 않아야함)
-- - 그렇지 않으면 emp 테이블의 empno, ename, deptno 값을 emp_commision 테이블에 삽입

select deptno, empno, ename, comm
from emp
order by 1

CREATE TABLE public.emp_commision (
    empno int4 NOT NULL,
    ename varchar(10) NULL,
    comm int4 NULL,
    deptno int4 NULL
);

select deptno, empno, ename, comm
from emp_commision
order by 1

-- 동작 안함...
--merge into emp_commision ec 
--using (select * from emp) emp on (ec.empno = emp.empno)
--when matched then 
--    update set ec.comm = 1000
--    delete where (sal < 2000)
--when not matched then 
--    insert (ec.empno, ec.ename, ec.deptno, ec.comm)
--    values(emp.empno, emp.ename, emp.deptno, emp.comm)

-- 4.12 테이블에서 모든 레코드 삭제하기
-- delete from emp

-- 4.13 특정 레코드 삭제
delete from emp where deptno = 10

-- 4.14 단일 레코드 삭제
delete from emp where empno = 7782

-- 4.15 참조 무결성 위반 삭제
delete from emp
where not exists (
    select * from dept
    where dept.deptno = emp.deptno
)

delete from emp
where deptno not in (select deptno from dept)

-- 4.16 중복 레코드 삭제
create table dupes (id integer, name varchar(10))

insert into dupes values (1, 'NAPOLEON')
insert into dupes values (2, 'DYNAMITE')
insert into dupes values (3, 'DYNAMITE')
insert into dupes values (4, 'SHE SELLS')
insert into dupes values (5, 'SEA SHELLS')
insert into dupes values (6, 'SEA SHELLS')
insert into dupes values (7, 'SEA SHELLS')

select * from dupes

delete from dupes 
where id not in (select min(id) from dupes group by name)


-- 4.17 다른 테이블에서 참조된 레코드 삭제
create table dept_accidents
( deptno         integer,
  accident_name  varchar(20) )
  
insert into dept_accidents values (10,'BROKEN FOOT')
insert into dept_accidents values (10,'FLESH WOUND')
insert into dept_accidents values (20,'FIRE')
insert into dept_accidents values (20,'FIRE')
insert into dept_accidents values (20,'FLOOD')
insert into dept_accidents values (30,'BRUISED GLUTE')

select * from dept_accidents 

delete from emp
where deptno in ( select deptno
                  from dept_accidents
                  group by deptno
                  having count(*) >= 3 )

select deptno
from dept_accidents
group by deptno
having count(*) >= 3