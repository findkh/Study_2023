import client from './client';

export const writePost = ({ title, body, tags }) => {
	//console.log(title, body, tags);
	return client.post('/api/posts', { title, body, tags });
};

export const readPost = (id) => {
	console.log('readPost - before API call - id:', id);
	return client.get(`/api/posts/${id}`).then((response) => {
		//console.log('readPost - after API call - response:', response);
		//console.log(response.data);
		return response.data;
	});
};

export const listPosts = ({ page, username, tag }) => {
	// console.log('리스트 호출전: ', page, username);
	return client.get(`/api/posts`, {
		params: { page, username, tag },
	});
};

export const updatePost = ({ id, title, body, tags }) =>
	client.patch(`/api/posts/${id}`, {
		title,
		body,
		tags,
	});

export const removePost = (id) => client.delete(`/api/posts/${id}`);
