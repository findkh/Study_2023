-- 6.11 구분된 데이터를 다중 값 in 목록으로 변환하기
select ename, sal, deptno
from emp e where empno in (7654, 7698, 7782, 7788)

select ename, sal, deptno
from emp
where empno in (
    select cast(empno as integer) as empno
        from (
            select split_part(list.vals,',',iter.pos) as empno
            from (select id as pos from t10) iter,
                 (select ','||'7654,7698,7782,7788'||',' as vals
                  from t1) list
                  where iter.pos <= length(list.vals) - length(replace(list.vals,',',''))
        ) z
        where length(empno) > 0
)

select list.vals, split_part(list.vals,',',iter.pos) as empno, iter.pos
from (select id as pos from t10) iter, 
     (select ','||'7654,7698,7782,7788'||',' as vals from t1) list
where iter.pos <= length(list.vals) - length(replace(list.vals,',',''))

-- 6.12 문자열을 알파벳 순서로 정렬 : 값 안나옴
select ename, string_agg(c, '' order by ename)
from (
    select a.ename, substr(a.ename, iter.pos, 1) as c
    from emp a, (select id pos from t10) as iter
    where iter.pos <= length(a.ename)
    order by 1, 2
) x
group by x.ename, c


-- 6.13 숫자로 취급할 수 있는 문자열 식별
create view v6 as
    select replace(mixed,' ','') as mixed
      from (
    select substr(ename,1,2)||
           cast(deptno as char(4))||
           substr(ename,3,2) as mixed
      from emp
     where deptno = 10
     union all
    select cast(empno as char(4)) as mixed
      from emp
     where deptno = 20
     union all
    select ename as mixed
      from emp
     where deptno = 30
           ) x
           
select * from v6

-- 숫자만 있거나 하나 이상의 숫자를 포함하는 행 반환
select cast(
     case when replace(translate(mixed,'0123456789','9999999999'),'9','') is not null
          then replace(translate(mixed, replace(translate(mixed, '0123456789', '9999999999'),'9', ''), rpad('#', length(mixed), '#')), '#', '')
          else mixed
          end as integer ) as mixed
from v6
where strpos(translate(mixed, '0123456789', '9999999999'), '9') > 0

select mixed as orig,
        translate(mixed,'0123456789','9999999999') as mixed1,
        replace(translate(mixed,'0123456789','9999999999'),'9','') as mixed2,
        translate(mixed,  replace(translate(mixed,'0123456789','9999999999'),'9',''), rpad('#',length(mixed),'#')) as mixed3,
        replace(translate(mixed, replace(translate(mixed,'0123456789','9999999999'),'9',''), rpad('#',length(mixed),'#')),'#','') as mixed4
from v6
where strpos(translate(mixed,'0123456789','9999999999'),'9') > 0

--6.14 n번째로 구분된 부분 문자열 추출하기
create view v7 as
    select 'mo,larry,curly' as name from t1
    union all
    select 'tina,gina,jaunita,regina,leena' as name from t1
    
select * from v7

-- 각행에서 두번쨰 이름을 추출
select iter.pos, src.name as name1, split_part(src.name, ',', iter.pos) as name2
from (select id as pos from t10) iter,
     (select cast(name as text) as name from v7) src
where iter.pos <= length(src.name) - length(replace(Src.name, ',', '')) +1

--6.15 IP 주소 파싱하기
select split_part(y.ip, '.', 1) as a,
       split_part(y.ip, '.', 2) as b,
       split_part(y.ip, '.', 3) as c,
       split_part(y.ip, '.', 4) as d
from (select cast('92.111.0.2' as text) as ip from t1) as y

--6.17 패턴과 일치하지 않는 텍스트 찾기 : 안나옴
select emp_id, text from employee_comment

--select emp_id, "text"
--from employee_comment
--where regexp_like('text', '[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}')
--      and 
--      regexp_like(regexp_replace('text', '[0-9]{3}([-. ])[0-9]{3}\1[0-9]{4}','***'), '[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}')
