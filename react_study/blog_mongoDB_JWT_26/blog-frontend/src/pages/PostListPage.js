import HeaderContainer from '../containers/common/HeaderContainer';
import PostListContainer from '../containers/posts/PostListContainer';
import PaginationContainer from '../containers/posts/PaginationContainer';

const PostPage = () => {
	return (
		<>
			<HeaderContainer />
			<PostListContainer />
			<PaginationContainer />
		</>
	);
};

export default PostPage;
