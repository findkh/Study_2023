-- 11. 고급 검색
-- 11.1 결과셋을 페이지로 매기기
select sal
from (
    select row_number() over (order by sal) as rn, sal
    from emp
)x
where rn between 1 and 5

select sal
from (
    select row_number() over (order by sal) as rn, sal
    from emp
)x
where rn between 6 and 10

-- 11.2 테이블에서 n개 행 건너뛰기
select ename
from (
    select row_number() over (order by ename) rn, ename
    from emp
) x
where mod(rn, 2) = 1

-- 11.3 외부 조인을 사용할 때 OR 로직 통합하기
-- 부서 30 및 40에 대한 부서 정보와 함께 부서 10, 20의 모든 사원명 및 부서 정보 반환
select e.ename, d.deptno, d.dname, d.loc
from dept d, emp e
where d.deptno = e.deptno and (e.deptno = 10 or e.deptno = 20)
order by 2

select e.ename, d.deptno, d.dname, d.loc
from dept d left join emp e on (d.deptno = e.deptno)
where e.deptno = 10 or e.deptno = 20
order by 2

select e.ename, d.deptno, d.dname, d.loc
from dept d left join emp e on (d.deptno = e.deptno and (e.deptno=10 or e.deptno=20))
order by 2

select e.ename, d.deptno, d.dname, d.loc 
from dept d left join (
    select ename, deptno from emp where deptno in ( 10, 20 ) ) e on ( e.deptno = d.deptno )
order by 2

-- 11.5 상위 n개 레코드 선택하기
select ename, sal 
from (
    select ename, sal, dense_rank() over (order by sal desc) dr
    from emp
) x 
where dr <= 5

select ename, sal, dense_rank() over(order by sal desc) dr
from emp

-- 11.6 최댓값과 최솟값을 가진 레코드 찾기
select ename, sal
from (
    select ename, sal, min(sal) over() min_sal, max(sal) over() max_sal
    from emp
) x 
where sal in (min_sal, max_sal)

-- 11.7 이후 행 조사하기
-- 최근 고용된 사원보다 수입이 적은 사원
select ename, sal, hiredate
from (
    select ename, sal, hiredate, lead(sal) over(order by hiredate) next_sal
    from emp
) x
where sal < next_sal

select ename, sal, hiredate, lead(sal) over(order by hiredate) next_sal
from emp

-- 11.8 행 값 이동
-- 사원명과 급여를 다음으로 높은 그병와 가장 낮은 급여와 함께 반환(?)
select ename, sal, 
        coalesce(lead(sal) over (order by sal), min(sal) over()) as forward,
        coalesce(lag(sal) over(order by sal), max(sal) over()) as rewind
from emp

select ename, sal, 
        lead(sal) over (order by sal) as forward,
        lag(sal) over(order by sal) as rewind
from emp

-- 11.9 순위 결과
select dense_rank() over(order by sal) rnk, sal
from emp

-- 11.10 중복 방지
select job
from (
    select job, row_number() over(partition by job order by job) rn
    from emp
) x 
where rn = 1

select distinct job from emp

select job from emp group by job

select job, row_number() over(partition by job order by job) rn from emp

select distinct job, deptno from emp

-- 11.11 기사값 찾기
-- 각 부서에서 각 사원명, 근무하는 부서, 급여, 고용된 날짜 및 마지막으로 고용된 사원의 급여가 포함된 결과셋을 반환
select deptno, ename, sal, hiredate, max(latest_sal)over(partition by deptno) latest_sal
from (
    select deptno, ename, sal, hiredate, 
            case when hiredate = max(hiredate) over(partition by deptno) then sal else 0 end latest_sal
    from emp
) x
order by 1, 4 desc

select deptno, ename, sal, hiredate,
       case when hiredate = max(hiredate)over(partition by deptno) then sal else 0 end latest_sal
from emp

-- 11.12 간단한 예측 생성
select id, order_date, process_date,
        case when gs.n >= 2 then process_date+1 else null end as verified,
        case when gs.n = 3 then process_date+2 else null end as shipped
from (
    select gs.id, current_date+gs.id as order_date, current_date+gs.id+2 as process_date
    from generate_series(1,3) gs (id) 
) orders, generate_series(1,3) gs(n)

select gs.id, current_date+gs.id as order_date, current_date+gs.id+2 as process_date
from generate_series(1,3) gs (id)

select gs.n, orders.*
from (
    select gs.id, current_date+gs.id as order_date, current_date+gs.id+2 as process_date
    from generate_series(1,3) gs (id)
) orders, generate_series(1,3) gs(n)

select id, order_date, process_date, 
       case when gs.n >= 2 then process_date+1 else null end as verified,
       case when gs.n = 3 then process_date+2 else null end as shipped
from (
    select gs.id, current_date+gs.id as order_date, current_date+gs.id+2 as process_date
    from generate_series(1,3) gs(id)
) orders, generate_series(1,3)gs(n)
