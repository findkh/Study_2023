import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useNavigate } from 'react-router-dom';
import { readPost, unloadPost } from '../../modules/post';
import PostViewer from '../../components/post/PostViewer';
import PostActionButtons from '../../components/post/PostActionButtons';
import { setOriginalPost } from '../../modules/write';
import { removePost } from '../../lib/api/posts';

const PostViewerContainer = () => {
	const { postId } = useParams();
	const navigate = useNavigate();
	const dispatch = useDispatch();
	const { post, error, loading, user } = useSelector(
		({ post, loading, user }) => ({
			post: post.post,
			error: post.error,
			loading: loading['post/READ_POST'],
			user: user.user,
		}),
	);

	useEffect(() => {
		dispatch(readPost(postId));
		//console.log('PostViewerContainer - useEffect - postId:', postId);
		return () => {
			dispatch(unloadPost());
		};
	}, [dispatch, postId]);

	const onEdit = () => {
		// console.log('onEdit!!!');
		dispatch(setOriginalPost(post));
		navigate('/write');
	};

	const onRemove = async () => {
		try {
			await removePost(postId);
			navigate('/');
		} catch (e) {
			console.log(e);
		}
	};

	const ownPost = (user && user.data._id) === (post && post.user._id);
	//console.log(user && user.data._id);
	console.log(ownPost);

	return (
		<PostViewer
			post={post}
			loading={loading}
			error={error}
			actionButtons={
				ownPost && (
					<PostActionButtons onEdit={onEdit} onRemove={onRemove} />
				)
			}
		/>
	);
};

export default PostViewerContainer;
