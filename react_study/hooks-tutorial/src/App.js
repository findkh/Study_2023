import Average from "./Average";

// const App = () => {
//     return <Average />;
// };

import { useState } from 'react';
import Info from './Info';

const App = () => {
    //return <Info />;
    const [visible, setVisible] = useState(false);
    return(
        <div>
            <button onClick={() => {
                setVisible(!visible);
            }}>
                {visible ? '숨기기' : '보이기'}
            </button>
            <hr />
            {visible && <Info />}
        </div>
    );
};

// import Counter from './Counter';

// const App = () => {
//   return <Counter />;
// };

export default App;