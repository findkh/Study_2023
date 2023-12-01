import logo from './logo.svg';
import './App.css';
import { Fragment } from 'react';


function App() {
  const name = '리액트';
  const name2 = '수달';
  const name3 = '뤼엑트';
  const name4 = undefined;
  const style = {
    backgroundColor : 'black', //카멜 표기법으로 변경
    color: 'aqua',
    fontSize: '48px',
    fontWeight: 'bold',
    padding: 16
  }
  return (
    // <div>
    //<Fragment>
    <>
      <h1>리택트 동작 확인3</h1>
      <h2>정상 동작하는가?</h2>
      <h3>{name}</h3>
      {name2 === '수달' ? (
        <h3>개발자</h3>
      ) : (
        <h3>코더</h3>
      )}
      {name3 === '리액트' ? <h1>리액트 입니다</h1> : null}
      <div>{name3 === '리액트' && <h1>리액트입니다</h1>}</div>
      <div>{name4}</div>
      <div>{name4 || 'undefined야'}</div>
      <div style={style}>{name}</div>
      <div className='react'>{name}</div>
      <div className='react'>{name}</div>
      <input></input>
      <input />
      {/* 주석 작성 */}
      // 주석 아님
      /* 주석 아님 */
    </>
    //</Fragment>
    // </div>

    
  );
}

export default App;
