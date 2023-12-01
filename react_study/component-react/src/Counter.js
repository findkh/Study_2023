import { Component } from 'react'

// state를 constructor에서 꺼내기
class Counter extends Component {
    state = {
        number: 0,
        fixedNumber: 0
    };
    render(){
        const { number, fixedNumber } = this.state;

        return (
            <div>
                <h1>{number}</h1>
                <h2>바뀌지 않는 값: {fixedNumber}</h2>
                <button
                    onClick={() => {
                        //this.setState가 끝난 후 특정 작업 실행하기
                        this.setState({
                            number: number+1
                        }, () =>{
                            console.log('방금 setState가 호출되었습니다.')
                            console.log(this.state);
                        })

                        // this.setState(prevState => {
                        //     return {
                        //         number: prevState.number + 1
                        //     };
                        // });

                        // this.setState(prevState => ({
                        //     number: prevState.number+1
                        // }));
                    }}    
                >
                    +1
                </button>
            </div>
        );
    }
}

// 클래스형 컴포넌트의 state
// class Counter extends Component {
//     constructor(props) {
//         super(props);

//         this.state = {
//             number: 0,
//             fixedNumber: 0
//         };
//     }

//     render() {
//         const { number, fixedNumber } = this.state;
//         return (
//             <div>
//                 <h1>{number}</h1>
//                 <h2>바뀌지 않는 값: {fixedNumber}</h2>
//                 <button onClick={() => {this.setState({number: number+1});}}>+1</button>
//             </div>
//         );
//     }
// }

export default Counter;