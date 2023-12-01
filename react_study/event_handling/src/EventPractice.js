import { useState } from 'react'
// 문자열 아닌 객체 넣기
const EventPractice = () => {
    const [form, setForm] = useState({
        username: '',
        message: ''
    });
    const {username, message} = form;
    const onChange = e => {
        const nextForm = {
            ...form,
            [e.target.name]: e.target.value
        };
        setForm(nextForm);
    };
    const onClick = () => {
        alert(username + ': ' + message);
        setForm({
            username: '',
            message: ''
        });
    };
    const onKeyPress = e => {
        if(e.key === 'Enter'){
            onClick();
        }
    };
        return (
        <div>
            <input 
                type='text'
                name='username'
                placeholder='사용자명'
                value={username}
                onChange={onChange}
            />
            <input
                type='text'
                name='message'
                placeholder='아무거나 입력'
                value={message}
                onChange={onChange}
                onKeyPress={onKeyPress}
            />
            <button onClick={onClick}>확인</button>
        </div>
    )
}

// 함수 컴포넌트로 구현
// const EventPractice = () => {
//     const [username, setUsername] = useState('');
//     const [message, setMessage] = useState('');
//     const onChangeUsername = e => setUsername(e.target.value);
//     const onChangeMessage = e => setMessage(e.target.value);
//     const onClick = () => {
//         alert(username + ': ' + message);
//         setUsername('');
//         setMessage('');
//     };
//     const onKeyPress = e => {
//         if(e.key === 'Enter'){
//             onClick();
//         }
//     };

//     return (
//         <div>
//             <input 
//                 type='text'
//                 name='username'
//                 placeholder='사용자명'
//                 value={username}
//                 onChange={onChangeUsername}
//             />
//             <input
//                 type='text'
//                 name='message'
//                 placeholder='아무거나 입력'
//                 value={message}
//                 onChange={onChangeMessage}
//                 onKeyPress={onKeyPress}
//             />
//             <button onClick={onClick}>확인</button>
//         </div>
//     )
// }

//import { Component } from 'react';

// Propertly Initializer Syntax를 사용한 메서드 작성
// class EventPractice extends Component {
//     state = {
//         username: '',
//         message: ''
//     }

//     handleChange = (e) => {
//         this.setState({
//             [e.target.name]: e.target.value
//         });
//     }

//     handleClick = (e) => {
//         alert(this.state.username + ': ' + this.state.message);
//         this.setState({
//             username: '',
//             message: ''
//         });
//     }

//     handleKeyPress = (e) => {
//         if(e.key === 'Enter'){
//             this.handleClick();
//         }
//     }

//     render(){
//         return(
//             <div>
//                 <h1>이벤트 연습3</h1>
//                 <input
//                     type='text'
//                     name='username'
//                     placeholder='이름을 입력하세요'
//                     value={this.state.name}
//                     onChange={this.handleChange}
//                 />
//                 <input
//                     type='text'
//                     name='message'
//                     placeholder='아무거나 입력해보세요'
//                     value={this.state.message}
//                     onChange={this.handleChange}
//                     onKeyPress={this.handleKeyPress}
//                 />
//                 <button onClick={this.handleClick}>확인</button>
//             </div>
//         )
//     }
// }

// 임의 메서드 만들기
// 기본 방식
// class EventPractice extends Component{
//     state = {
//         message: ''
//     }

//     constructor(props){
//         super(props);
//         this.handleChange = this.handleChange.bind(this);
//         this.handleClick = this.handleClick.bind(this);
//     }

//     handleChange(e){
//         this.setState({
//             message: e.target.value
//         });
//     }

//     handleClick(e){
//         alert(this.state.message);
//         this.setState({
//             message: ''
//         });
//     }

//     render(){
//         return(
//             <div>
//                 <h1>이벤트 연습2</h1>
//                 <input
//                     type='text'
//                     name='message'
//                     placeholder='입력하세요'
//                     value={this.state.message}
//                     onChange={this.handleChange}
//                 />
//                 <button onClick={this.handleClick}>확인</button>
//             </div>
//         )
//     }
// }

// class EventPractice extends Component {

//     state = {
//         message: ''
//     }

//     render(){
//         return(
//             <div>
//                 <h1>이벤트 연습</h1>
//                 <input
//                     type="text"
//                     name="message"
//                     placeholder='아무거나 입력해보세요'
//                     value={this.state.message}
//                     onChange={
//                         (e) => {
//                             //console.log(e.target.value);
//                             this.setState({
//                                 message: e.target.value
//                             })
//                         }
//                     }
//                 />

//                 <button onClick={
//                     () => {
//                         alert(this.state.message)
//                         this.setState({
//                             message: ''
//                         });
//                     }
//                 }>확인</button>
//             </div>
//         )
//     }
// }

export default EventPractice;