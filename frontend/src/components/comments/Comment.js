const Comment = ({ comment }) => {

    return (
        <div class="p-4 rounded-2 bg-light mb-3">
            <div class="d-flex align-items-center gap-3">
                <img src={`https://bootdey.com/img/Content/avatar/avatar${comment.user.id % 8}.png`} alt="" class="rounded-circle" width="33" height="33"></img>
                <h6 class="fw-semibold mb-0 fs-4">{comment.user.login}</h6>
                {/* <span class="fs-2"><span class="p-1 bg-muted rounded-circle d-inline-block"></span> 8 min ago</span> */}
            </div>
            <p class="my-3">{comment.content}
            </p>
            <div class="d-flex align-items-center">
                <div class="d-flex align-items-center gap-2">
                    <a class="text-white d-flex align-items-center justify-content-center bg-primary p-2 fs-4 rounded-circle" href="javascript:void(0)" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Like">
                        <i class="fa fa-thumbs-up"></i>
                    </a>
                    <span class="text-dark fw-semibold">55</span>
                </div>
                <div class="d-flex align-items-center gap-2 ms-4">
                    <a class="text-white d-flex align-items-center justify-content-center bg-secondary p-2 fs-4 rounded-circle" href="javascript:void(0)" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Reply">
                        <i class="fa fa-arrow-up"></i>
                    </a>
                    <span class="text-dark fw-semibold">0</span>
                </div>
            </div>
        </div>
    );
}

export default Comment;