document.addEventListener("DOMContentLoaded", () => {
  const startDateInput = document.getElementById("start-date");
  const endDateInput = document.getElementById("end-date");
  let previousEndDateValue = endDateInput.value;

  endDateInput.style.opacity = "0.5";
  endDateInput.style.cursor = "not-allowed";

  endDateInput.disabled = true; 

  function setEndDateToStartDate() {
    if (!endDateInput.value) {
      endDateInput.value = startDateInput.value;
    }
  }

  startDateInput.addEventListener("blur", () => {
    setEndDateToStartDate();
  });

  endDateInput.addEventListener("input", () => {
    if (new Date(startDateInput.value) > new Date(endDateInput.value)) {
      endDateInput.value = previousEndDateValue;
    } else {
      previousEndDateValue = endDateInput.value;
    }
  });

  startDateInput.addEventListener("change", (event) => {
    const selectedDate = new Date(event.target.value);
    if (selectedDate > new Date()) {
      event.target.value = ""; 
      alert("Datas futuras não são permitidas."); 
      return; 
    }
    selectedDate.setDate(selectedDate.getDate() + 1); 
    endDateInput.min = selectedDate.toISOString().split("T")[0];
    endDateInput.disabled = false; 
    endDateInput.style.opacity = "1"; 
    endDateInput.style.cursor = "auto"; 
  });
});
