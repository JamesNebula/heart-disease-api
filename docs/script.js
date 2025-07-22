// frontend/script.js

document.getElementById("predictForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = {};

  for (let [key, value] of formData.entries()) {
    data[key] = parseFloat(value);
  }

  fetch("https://heart-disease-api-s4d3.onrender.com/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      const resultDiv = document.getElementById("result");
      resultDiv.style.display = "block";

      if (result.prediction === 1) {
        resultDiv.className = "danger";
        resultDiv.innerText = "⚠️ Heart Disease Detected!";
      } else {
        resultDiv.className = "success";
        resultDiv.innerText = "✅ No Heart Disease Detected.";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Something went wrong. Check the console for details.");
    });
});
