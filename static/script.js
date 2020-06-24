var modal = document.getElementById("currModal");
var btns = document.getElementsByClassName("modalBtn");
var span = document.getElementsByClassName("close")[0];

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", () => {
    modal.style.display = "block";
  });
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
