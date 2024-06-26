window.RevealPassword = function(passwordID,iconID){

      let eyeicon = document.getElementById(iconID);
      let password = document.getElementById(passwordID);

      eyeicon.onclick = function () {
        if (password.type === "password") {
          password.type = "text";
          eyeicon.classList.remove("ph-eye-closed"); // Remove the 'ph-eye' class
          eyeicon.classList.add("ph-eye"); // Add the 'ph-eye-closed' class
        } else {
          password.type = "password";
          eyeicon.classList.remove("ph-eye"); // Remove the 'ph-eye-closed' class
          eyeicon.classList.add("ph-eye-closed"); // Add the 'ph-eye' class
        }
      };
}
