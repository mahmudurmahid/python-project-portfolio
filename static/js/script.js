<script>
document.querySelectorAll(".btn-show-more").forEach(function (button) {
  button.addEventListener("click", function (event) {
    event.preventDefault(); // Prevents page from jumping to the top
    const modalId = button.getAttribute("data-bs-target"); // Get the modal ID from the button
    var myModal = new bootstrap.Modal(document.querySelector(modalId));
    myModal.show();
  });
});
</script>