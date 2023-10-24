// ES8 문법
function increase(number){
    console.log('increase 호출');
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            const result = number + 10;
            if(result > 50){
                const e = new Error('Number Too Big');
                return reject(e);
            }
            resolve(result);
        }, 1000)
    });
    return promise;
}

async function runTasks(){
    try{
        let result = await increase(0);
        console.log(result);
        result = await increase(result);
        console.log(result);
        result = await increase(result);
        console.log(result);
        result = await increase(result);
        console.log(result);
        result = await increase(result);
        console.log(result);
        result = await increase(result);
        console.log(result);
    } catch(e){
        console.log(e);
    }
}

runTasks();