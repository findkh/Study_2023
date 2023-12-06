import AskModal from '../common/AskModal';

const AskRemoveModal = ({ visible, onConfirm, onCancel }) => {
	return (
		<AskModal
			visible={visible}
			title="포스트 삭제"
			discription="포스트를 정말 삭제하시겠습니까?"
			onConfirm={onConfirm}
			onCancel={onCancel}
		/>
	);
};

export default AskRemoveModal;