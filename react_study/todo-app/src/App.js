import TodoTemplate from './components/TodoTemplate';
import TodoInsert from './components/TodoInsert';

const App = () => {
    return(
        <TodoTemplate>
            <TodoInsert />
        </TodoTemplate>
    )
}

// const App = () => {
//     return <TodoTemplate>Todo App을 만들자</TodoTemplate>
// };

export default App;