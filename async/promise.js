console.log('?')
// 콜백 지옥 회피
function increase(number){
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            const result = number+10;
            if(result > 50){
                const e = new Error('Number Too Big');
                return reject(e);
            }
            resolve(result);
        }, 1000);
    });
    return promise;
}

increase(0)
.then(number => {
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.then(number => {
    console.log(number);
    return increase(number);
})
.catch(e => {
    console.log(e)
})