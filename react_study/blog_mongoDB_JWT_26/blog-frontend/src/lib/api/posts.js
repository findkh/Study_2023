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
	console.log(page, username);
	return client.get(`/api/posts`, {
		params: { page, username, tag },
	});
};
