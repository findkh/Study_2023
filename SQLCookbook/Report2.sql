-- 12.11 비 group by 열 반환
select ename, max(sal) from emp group by ename

select deptno, ename, job, sal,
       case when sal = max_by_dept then 'TOP SAL IN DEPT'
            when sal = min_by_dept then 'LOW SAL IN DEPT' end dept_status,
       case when sal = max_by_job then 'TOP SAL IN JOB' 
            when sal = min_by_job then 'LOW SAL IN JOB' end job_status
from (
        select deptno,ename,job,sal,
            max(sal)over(partition by deptno) max_by_dept,
            max(sal)over(partition by job)   max_by_job,
            min(sal)over(partition by deptno) min_by_dept,
            min(sal)over(partition by job)   min_by_job
        from emp
) emp_sals
where sal in (max_by_dept, max_by_job, min_by_dept,min_by_job)

select deptno, ename, job, sal,
       max(sal)over(partition by deptno) maxDEPT,
       max(sal)over(partition by job) maxJOB,
       min(sal)over(partition by deptno) minDEPT,
       min(sal)over(partition by job) minJOB
from emp

select deptno, ename, job, sal,
       case when sal = max_by_dept then 'TOP SAL IN DEPT'
            when sal = min_by_dept then 'LOW SAL IN DEPT' end dept_status,
       case when sal = max_by_job then 'TOP SAL IN JOB' 
            when sal = min_by_job then 'LOW SAL IN JOB' end job_status
from (
        select deptno,ename,job,sal,
            max(sal)over(partition by deptno) max_by_dept,
            max(sal)over(partition by job) max_by_job,
            min(sal)over(partition by deptno) min_by_dept,
            min(sal)over(partition by job) min_by_job
        from emp
) x
where sal in (max_by_dept, max_by_job, min_by_dept,min_by_job)

-- 12.12 단순 소계 계산
select coalesce(job, 'TOTAL') job, sum(sal) sal
from emp
group by rollup(job)

-- 12.13 가능한 모든 식 조합의 소계 계산
select deptno, job, 
        case concat(cast(grouping(deptno) as char(1)), cast (grouping(job) as char(1)))
            when '00' then 'total by dept and job' when '10' then 'total by job'
            when '01' then 'total by dept'
            when '11' then 'grand total for table' end category,
        sum(sal) as sal
from emp
group by cube(deptno, job)

-- 12.14 소계가 아닌 행 식별
select deptno, job, sal, grouping(deptno) deptno_subtotals, grouping(job) job_subtotals
from emp
group by cube(deptno, job, sal)

-- 12.15 Case 표현식으로 행 플래그 지정
select ename,
        case when job = 'CLERK' then 1 else 0 end as is_clerk,
        case when job = 'SALESMAN' then 1 else 0 end as is_sales,
        case when job = 'MANAGER' then 1 else 0 end as is_mgr,
        case when job = 'ANALYST' then 1 else 0 end as is_analyst,
        case when job = 'PRESIDENT' then 1 else 0 end as is_prez
from emp
order by 2,3,4,5,6

-- 12.16 희소행렬
select case deptno when 10 then ename end as d10,
       case deptno when 20 then ename end as d20,
       case deptno when 30 then ename end as d30,
       case job when 'CLERK' then ename end as clerks,
       case job when 'MANAGER' then ename end as mgrs,
       case job when 'PRESIDENT' then ename end as prez,
       case job when 'ANALYST' then ename end as anals,
       case job when 'SALESMAN' then ename end as sales
from emp

select max(case deptno when 10 then ename end) d10,
       max(case deptno when 20 then ename end) d20,
       max(case deptno when 30 then ename end) d30,
       max(case job when 'CLERK' then ename end) clerks,
       max(case job when 'MANAGER' then ename end) mgrs,
       max(case job when 'PRESIDENT' then ename end) prez, 
       max(case job when 'ANALYST' then ename end) anals, 
       max(case job when 'SALESMAN' then ename end) sales
from ( 
    select deptno, job, ename, row_number()over(partition by deptno order by empno) rn 
    from emp 
) x 
group by rn

-- 12.18 여러 그룹/파티션 집계를 동시 수행
select ename,
       deptno,
       count(*)over(partition by deptno) deptno_cnt,
       job,
       count(*)over(partition by job) job_cnt,
       count(*)over() total
from emp

-- 12.19 값의 이동 범위에 대한 집계 수행
select e.hiredate, e.sal, d.sal, d.hiredate
from emp e, emp d

select e.hiredate, e.sal, d.sal sal_to_sum, d.hiredate within_90_days
from emp e, emp d
where d.hiredate between e.hiredate-90 and e.hiredate
order by 1

select e.hiredate, e.sal,
         (select sum(sal) 
          from emp d
          where d.hiredate between e.hiredate-90 and e.hiredate) as spending_pattern
from emp e
order by 1

select e.hiredate, e.sal, sum(d.sal) as spending_pattern
from emp e, emp d
where d.hiredate between e.hiredate-90 and e.hiredate
group by e.hiredate,e.sal
order by 1

-- 12.20 소계를 사용한 결과셋 피벗
select mgr,
       sum(case deptno when 10 then sal else 0 end) dept10,
       sum(case deptno when 20 then sal else 0 end) dept20,
       sum(case deptno when 30 then sal else 0 end) dept30,
       sum(case flag when '11' then sal else null end) total
from (
    select deptno, mgr, sum(sal) sal, concat(cast (grouping(deptno) as char(1)), cast(grouping(mgr) as char(1))) flag
    from emp
    where mgr is not null
    group by rollup (deptno,mgr)
) x
group by mgr








