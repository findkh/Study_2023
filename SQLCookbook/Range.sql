-- 10. 범위 관련 작업
-- 10.1 연속 값의 범위 찾기
create view v9 as
    select proj_id, proj_start, proj_end 
    from emp_project
    order by proj_id 
    limit 14
    
select * from v9

select *
from (
    select proj_id, proj_start, proj_end, lead(proj_start)over(order by proj_id) next_proj_start
    from v9
) a
where proj_id in ( 1, 4 )

-- 10.2 같은 그룹 또는 파티션의 행 간 차이 찾기
with next_sal_tab (deptno, ename, sal, hiredate, next_sal)
    as
        (select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) as next_sal
         from emp
        )
select deptno, ename, sal, hiredate, coalesce(cast(sal-next_sal as char), 'N/A') as diff
from next_sal_tab

select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) as next_sal
from emp

select deptno,ename,sal,hiredate, sal-next_sal diff
from (
        select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) next_sal
        from emp
) a

-- postgresql에 nvl이 없어서 coalesce로 변경
select deptno, ename, sal, hiredate, coalesce((sal-next_sal), 0) diff 
from (
        select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) next_sal
        from emp
) a

select deptno, ename, sal, hiredate, coalesce((sal-next_sal), 0) diff
from (
    select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) next_sal
    from emp
    where deptno=10 and empno > 10
) a

insert into emp (empno, ename, deptno, sal, hiredate)
values (1, 'ant' , 10, 1000, '2006-11-17')

insert into emp (empno,ename,deptno,sal,hiredate)
values (2,'joe',10,1500,'2006-11-17')

insert into emp (empno,ename,deptno,sal,hiredate)
values (3,'jim',10,1600,'2006-11-17')

insert into emp (empno,ename,deptno,sal,hiredate)
values (4,'jon',10,1700,'2006-11-17')

select deptno, ename, sal, hiredate, coalesce((sal-next_sal), 0) diff
from ( 
        select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) next_sal
        from emp
        where deptno=10
) a

-- 안나옴..
--select deptno, ename, sal, hiredate, coalesce((sal-next_sal), 0) diff
--from (
--        select deptno, ename, sal, hiredate, lead(sal, cnt-rn+1) over(partition by deptno order by hiredate) next_sal
--        from (
--                select deptno, ename, sal, hiredate, count(*)over(partition by deptno,hiredate) cnt, row_number() over(partition by deptno,hiredate order by sal) rn
--                from emp
--                where deptno=10
--        ) a
--) b

select deptno, ename, sal, hiredate, count(*)over(partition by deptno,hiredate) cnt, row_number()over(partition by deptno,hiredate order by sal) rn
from emp
where deptno=10

--select deptno, ename, sal, hiredate, lead(sal)over(partition by deptno order by hiredate) incorrect, cnt-rn+1 distance, 
--       lead(sal,cnt-rn+1)over(partition by deptno order by hiredate) correct
--from (
--        select deptno, ename, sal, hiredate, count(*)over(partition by deptno,hiredate) cnt,
--               row_number()over(partition by deptno,hiredate order by sal) rn
--        from emp
--        where deptno=10
--) a

--10.3 연속 값 범위의 시작과 끝 찾기 : 값이 이상하게 나옴
select * from v9

select proj_grp, min(proj_start), max(proj_end)
from (
        select proj_id, proj_start, proj_end, sum(flag) over(order by proj_id) proj_grp
        from (
                select proj_id, proj_start, proj_end,
                       case when lag(proj_end)over(order by proj_id) = proj_start then 0 else 1 end flag
                from V9
        ) alias1
) alias2
group by proj_grp

select proj_id, proj_start, proj_end, lag(proj_end) over(order by proj_id) prior_proj_end
from v9

select proj_id, proj_start, proj_end, sum(flag)over(order by proj_id) proj_grp
from (
        select proj_id, proj_start, proj_end, case when lag(proj_end) over(order by proj_id) = proj_start then 0 else 1 end flag
        from v9
) a

-- 10.4 값 범위에서 누락된 값 채우기 : 안나옴
--select y.yr, coalesce(x.cnt,0) as cnt
--from (
--        selectmin_year-mod(cast(min_year as int),10)+rn as yr
--        from (
--                select (select min(extract(year from hiredate)) from emp) as min_year, id-1 as rn
--                from t10
--         ) a
--) y
--left join
--(
--    select extract(year from hiredate) as yr, count(*) as cnt
--    from emp
--    group by extract(year from hiredate)
--) x on ( y.yr = x.yr )

--select year(min(hiredate)over()) - mod(year(min(hiredate)over()),10) + row_number()over()-1 yr, year(min(hiredate)over()) min_year, mod(year(min(hiredate)over()),10) mod_yr, row_number()over()-1 rn
--from emp fetch first 10 rows only

select DATE_PART('year', min(hiredate)::date)
from emp fetch first 10 rows only

--select min_year-mod(min_year,10)+rn as yr, min_year, mod(min_year,10) as mod_yr, rn
--from (
--        select (select min(extract(year from hiredate)) from emp) as min_year, id-1 as rn
--        from t10
--) x

select DATE_PART('year', hiredate) yr, count(*) cnt
from emp
group by DATE_PART('year', hiredate)

-- 10.5 연속된 숫자값 생성
select id from generate_series (1, 10) x(id)

select id
from generate_series((select min(deptno) from emp), (select max(deptno) from emp), 5 ) x(id)