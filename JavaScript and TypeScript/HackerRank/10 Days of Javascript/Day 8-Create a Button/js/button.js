let btn = document.getElementById("btn");
document.addEventListener("click", function () {
  let newText = Number(btn.innerText);
  newText += 1;
  btn.innerText = newText;
});
