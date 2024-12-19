document.addEventListener("DOMContentLoaded", function() {
  
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");
  const editButtons = document.querySelectorAll(".btn-edit");

  
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let postSlug = e.target.getAttribute("data-slug");  
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      let textarea = document.getElementById(`id_body_${commentId}`);
      let form = document.getElementById(`editForm${commentId}`);

      console.log("Comment ID:", commentId);
      console.log("Post Slug:", postSlug);
      console.log("Comment Content:", commentContent);

      if (form) {
        console.log(form.action);  
      } else {
        console.log("Form not found.");
      }

      textarea.value = commentContent;

      form.classList.remove('d-none');

      const submitButton = form.querySelector("button[type='submit']");
      submitButton.innerText = "Update";

      const commentForm = form.closest("form");

      commentForm.setAttribute("action", `/post/${postSlug}/edit_comment/${commentId}/`);
    });
  }

 
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let postSlug = e.target.getAttribute("data-slug"); 
      console.log("Deleting comment ID:", commentId);

      
      deleteConfirm.href = `/post/${postSlug}/delete_comment/${commentId}/`;  
      
     
      deleteModal.show();
    });
  }
});
