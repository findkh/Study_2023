//콜백 함수
function increase(number, callback){
    setTimeout(() => {
        const result = number + 10;
        if(callback){
            callback(result);
        }
    }, 1000)
}

// increase(0, result => {
//     console.log(result);
// })

// 순차 처리
console.log('작업 시작')
increase(0, result => {
    console.log(result);
    increase(result, result => {
        console.log(result);
        increase(result, result => {
            console.log(result);
            increase(result, result => {
                console.log(result);
                console.log('작업 완료');
            })
        })
    })
})