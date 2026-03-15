let nums = [1, 2, 3, 6, 9, 8, 4];
const ids = [1, 2, 3, 6, 9, 8, 4];

btn5 = document.getElementById("btn5");
btn5.addEventListener("click", function () {
  nums.unshift(nums.pop());
  for (let i = 0; i < ids.length; i += 1) {
    document.getElementById(`btn${ids[i]}`).innerText = nums[i];
  }
});
