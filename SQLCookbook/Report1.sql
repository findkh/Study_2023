-- 12. 보고서 작성과 재구성
-- 12.1 결과셋을 하나의 행으로 피벗하기
select deptno,
        case when deptno=10 then 1 else 0 end as deptno_10,
        case when deptno=20 then 1 else 0 end as deptno_20,
        case when deptno=30 then 1 else 0 end as deptno_30
from emp
order by 1

select deptno,
       sum(case when deptno=10 then 1 else 0 end) as deptno_10,
       sum(case when deptno=20 then 1 else 0 end) as deptno_20,
       sum(case when deptno=30 then 1 else 0 end) as deptno_30
from emp
group by deptno 
order by 1

select sum(case when deptno=10 then 1 else 0 end) as deptno_10,
       sum(case when deptno=20 then 1 else 0 end) as deptno_20,
       sum(case when deptno=30 then 1 else 0 end) as deptno_30
from emp

select max(case when deptno=10 then empcount else null end) as deptno_10,
       max(case when deptno=20 then empcount else null end) as deptno_20,
       max(case when deptno=10 then empcount else null end) as deptno_30
from (
    select deptno, count(*) as empcount
    from emp
    group by deptno
) x

-- 12.2 결과셋을 여러 행으로 피벗하기
select job, ename, row_number() over (partition by job order by ename) rn
from emp

select max(case when job='CLERK' then ename else null end) as clerks,
       max(case when job='ANALYST' then ename else null end) as analysts,
       max(case when job='MANAGER' then ename else null end) as mgrs,
       max(case when job='PRESIDENT' then ename else null end) as prez,
       max(case when job='SALESMAN' then ename else null end) as sales
from emp

select rn,
       case when job='CLERK' then ename else null end as clerks,
       case when job='ANALYST' then ename else null end as analysts,
       case when job='MANAGER' then ename else null end as mgrs,
       case when job='PRESIDENT' then ename else null end  as prez,
       case when job='SALESMAN' then ename else null end as sales
from (
    select job, ename, row_number()over(partition by job order by ename) rn
    from emp
) x

select max(case when job='CLERK' then ename else null end) as clerks,
       max(case when job='ANALYST' then ename else null end) as analysts,
       max(case when job='MANAGER' then ename else null end) as mgrs,
       max(case when job='PRESIDENT' then ename else null end) as prez,
       max(case when job='SALESMAN' then ename else null end) as sales
from (
    select job, ename, row_number()over(partition by job order by ename) rn
    from emp
) x
group by rn

select deptno dno, job,
       max(case when deptno=10 then ename else null end) as d10,
       max(case when deptno=20 then ename else null end) as d20,
       max(case when deptno=30 then ename else null end) as d30,
       max(case when job='CLERK' then ename else null end) as clerks,
       max(case when job='ANALYST' then ename else null end) as anals,
       max(case when job='MANAGER' then ename else null end) as mgrs,
       max(case when job='PRESIDENT' then ename else null end) as prez,
       max(case when job='SALESMAN' then ename else null end) as sales
from (
    select deptno, job, ename,
       row_number()over(partition by job order by ename) rn_job,
       row_number()over(partition by deptno order by ename) rn_deptno
    from emp
) x
group by deptno, job, rn_deptno, rn_job
order by 1

-- 12.3 결과셋 역피벗
create view emp_cnts as(
    select sum(case when deptno=10 then 1 else 0 end) as deptno_10,
           sum(case when deptno=20 then 1 else 0 end) as deptno_20,
           sum(case when deptno=30 then 1 else 0 end) as deptno_30
    from emp
)

select * from emp_cnts

select dept.deptno, emp_cnts.deptno_10, emp_cnts.deptno_20, emp_cnts.deptno_30
from (
    select sum(case when deptno=10 then 1 else 0 end) as deptno_10,
           sum(case when deptno=20 then 1 else 0 end) as deptno_20,
           sum(case when deptno=30 then 1 else 0 end) as deptno_30
    from emp
) emp_cnts, (select deptno from dept where deptno <= 30) dept

select dept.deptno,
        case dept.deptno 
        when 10 then emp_cnts.deptno_10
        when 20 then emp_cnts.deptno_20
        when 30 then emp_cnts.deptno_30 end as counts_by_dept
from emp_cnts cross join (select deptno from dept where deptno <= 30) dept

-- 12.4 결과셋을 한 열로 역피벗하기
select e.ename, e.job, e.sal, row_number() over(partition by e.empno order by e.empno) rn
from emp e
where e.deptno = 10

with recursive four_rows (id) as
(
    select 1
    union all
    select id+1 from four_rows where id < 4
),
x_tab (ename,job,sal,rn) as
(
    select  e.ename, e.job, e.sal, row_number() over (partition by e.empno order by e.empno)
    from emp e
    join four_rows on 1=1
)
select
    case rn when 1 then ename
        when 2 then job
        when 3 then cast(sal as char(4)) end emps
from x_tab

-- 12.5 결과셋에서 반복값 숨기기
-- emp 테이블에서 deptno 및 ename을 리턴하되 각 deptno에 대한 모든 행을 그룹화하여 deptno를 한번만 표시
select lag(deptno) over (order by deptno) lag_deptno, deptno, ename
from emp

select case when lag(deptno) over (order by deptno) = deptno then null else deptno end DEPTNO, ename
from emp

-- 12.6 행 간 계산하는 결과셋 피벗
select deptno, sum(sal) as sal from emp group by deptno order by 1

select d20_sal - d10_sal as d20_10_diff, d20_sal - d30_sal as d20_30_diff
from (
    select sum(case when deptno=10 then sal end) as d10_sal,
           sum(case when deptno=20 then sal end) as d20_sal,
           sum(case when deptno=30 then sal end) as d30_sal
    from emp
) totals_by_dept

with totals_by_dept (d10_sal, d20_sal, d30_sal)
as
(select
    sum(case when deptno=10 then sal end) as d10_sal,
    sum(case when deptno=20 then sal end) as d20_sal,
    sum(case when deptno=30 then sal end) as d30_sal
from emp)
select d20_sal - d10_sal as d20_10_diff, d20_sal - d30_sal as d20_30_diff 
from totals_by_dept

select case when deptno=10 then sal end as d10_sal,
       case when deptno=20 then sal end as d20_sal,
       case when deptno=30 then sal end as d30_sal
from emp

select sum(case when deptno=10 then sal end) as d10_sal,
       sum(case when deptno=20 then sal end) as d20_sal,
       sum(case when deptno=30 then sal end) as d30_sal
from emp

-- 12.7 고정 크기의 데이터 버킷 생성
select ceil(row_number() over (order by empno) / 5.0) grp, empno, ename
from emp

select row_number() over (order by empno) grp, empno, ename
from emp

select row_number()over(order by empno) rn,
       row_number()over(order by empno)/5.0 division,
       ceil(row_number()over(order by empno)/5.0) grp,
       empno,
       ename
from emp

-- 12.8 사전 정의된 수의 버킷 생성
select ntile(4) over(order by empno) gp, empno, ename
from emp

-- 12.9 수평 히스토그램 생성 : 안나옴
--select deptno, lpad('*', count('*'), '*') as cnt
--from emp
--group by deptno

select deptno, count(*)
from emp
group by deptno

select deptno, lpad('*',count(*)::integer,'*') as cnt
from emp
group by deptno

--12.10 수직 히스토그램 생성
select max(deptno_10) d10, max(deptno_20) d20, max(deptno_30) d30
from (
        select row_number()over(partition by deptno order by empno) rn,
            case when deptno=10 then '*' else null end deptno_10,
            case when deptno=20 then '*' else null end deptno_20,
            case when deptno=30 then '*' else null end deptno_30
        from emp
) x
group by rn
order by 1 desc, 2 desc, 3 desc

select row_number()over(partition by deptno order by empno) rn,
       case when deptno=10 then '*' else null end deptno_10,
       case when deptno=20 then '*' else null end deptno_20,
       case when deptno=30 then '*' else null end deptno_30
from emp

select max(deptno_10) d10, max(deptno_20) d20, max(deptno_30) d30
from (
        select row_number()over(partition by deptno order by empno) rn,
            case when deptno=10 then '*' else null end deptno_10,
            case when deptno=20 then '*' else null end deptno_20,
            case when deptno=30 then '*' else null end deptno_30
        from emp
) x
group by rn
order by 1 desc, 2 desc, 3 desc

