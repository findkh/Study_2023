import TodoListItem from "./TodoListItem";
import './TodoList.scss';

const TodoList = ({todos, onRemove, onToggle}) => {
    return(
        <div className="todoList">
            {todos.map(todo => (
                <TodoListItem todo={todo} key={todo.id} onRemove={onRemove} onToggle={onToggle}/>
            ))}
        </div>
    )
}

// const TodoList = () => {
//     return (
//         <div className="TodoList">
//             <TodoListItem />
//             <TodoListItem />
//             <TodoListItem />
//         </div>
//     );
// };

export default TodoList;