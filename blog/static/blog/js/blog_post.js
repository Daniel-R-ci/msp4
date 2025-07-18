$(document).ready(function () {

    // Hide the new comment form and add event listener to show button
    $('#newComment').hide();
    $('#showCommentForm').click(function () {
        $('#newComment').toggle();
    });
  
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const commentHeadline = document.getElementById("commentHeadline");

    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");
    
    const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
    
    /**
    * Initializes edit functionality for the provided edit buttons.
    * Code taken from Code Institute I think terefore I blog code along project
    * Modified in MS3 project and adapted slightly for this project 
    */
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let articleId = e.target.getAttribute("data-article_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;

            commentText.value = commentContent;
            commentHeadline.innerText="Edit your comment";
            submitButton.innerText = "Update";

            document.getElementById("new-comment").scrollIntoView();

            commentForm.setAttribute("action", `${articleId}/edit_comment/${commentId}`);
        });
    }

    /**
    * Initializes deletion functionality for the provided delete buttons.
    * Code taken from Code Institute I think terefore I blog code along project
    * Modified in MS3 project and adapted slightly for this project 
    */
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let articleId = e.target.getAttribute("data-article_id");
            let commentId = e.target.getAttribute("data-comment_id");
            document.getElementById("submitButton").getAttribute("data-article-id");
            deleteCommentConfirm.href = `${articleId}/delete_comment/${commentId}`;
            deleteCommentModal.show();
        });
    }
});