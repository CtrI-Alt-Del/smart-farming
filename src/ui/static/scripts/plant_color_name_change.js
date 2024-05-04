const colorPicker = document.getElementById("create-plant-form-hex-color");
const changeColorBtn = document.getElementById("buttonNativeColor");
const plantInput = document.getElementById("create-plant-name");
const exempleText = document.getElementById("exempleText");

colorPicker.addEventListener("input", () => {
  changeColorBtn.style.backgroundColor = colorPicker.value;
});

plantInput.addEventListener("input", () => {
  exempleText.textContent = plantInput.value;
});